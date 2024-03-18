import requests
import os 
from moviepy.editor import ImageSequenceClip, AudioFileClip, concatenate_videoclips
import os


def generate_and_save_audio_files(Title, explanations,file_paths):
    
    """
    Generate and save audio files based on the provided explanations.

    Args:
    - Title (list): List of titles.
    - explanations (list): List of explanations corresponding to the titles.
    """
    intro_Audio = {}
    api_key = os.environ.get("azure_two")
    region = 'centralindia'
    endpoint = f'https://{region}.tts.speech.microsoft.com/cognitiveservices/v1'
    def rep(text):
        headers = {
            'Ocp-Apim-Subscription-Key': api_key,
            'Content-Type': 'application/ssml+xml',
            'X-Microsoft-OutputFormat': 'audio-24khz-160kbitrate-mono-mp3',
            'User-Agent': 'faculty-voices'
        }

        ssml_template = f"""
        <speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-US'>
            <voice name='en-US-JessaNeural'>{text}</voice>
        </speak>
        """
        try:
            encoded_ssml_template = ssml_template.encode('utf-8')
            response = requests.post(endpoint, headers=headers, data=encoded_ssml_template)
            response.raise_for_status()  # Raise exception for bad response status
            return response.content
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

    def save_audio_file(file_name, content):
        if content:
            try:
                with open(file_name, 'wb') as audio:
                    audio.write(content)
                print(f"File saved: {file_name}")
            except IOError as e:
                print(f"Error saving file {file_name}: {e}")
        else:
            print("Empty content received. File not saved.")

    for i, title in enumerate(Title):
        title_lower = title.lower()
        audio_content = rep(explanations[i])
        file_name = f'audio/{i}.mp3'
        save_audio_file(file_name, audio_content)
        
    audio_folder = "audio"
    video_clips = []

    for i, image_path in enumerate(file_paths):
        # Load image file
        image_clip = ImageSequenceClip([image_path], fps=1)  # Set fps to 1 for 1 image per second

        # Load corresponding audio file if it exists
        audio_file = os.path.join(audio_folder, f"{i}.mp3")
        if os.path.exists(audio_file):
            try:
                audio_clip = AudioFileClip(audio_file)
                # Set the duration of the image clip to match the duration of the audio clip
                image_clip = image_clip.set_duration(audio_clip.duration)
                # Combine the image and audio clips
                final_clip = image_clip.set_audio(audio_clip)
                # Append the combined clip to the list
                video_clips.append(final_clip)
                # break
            except Exception as e:
                print(f"Failed to load audio for {i}: {e}")
        else:
            print(f"Audio file not found for {i}")

    # Concatenate all video clips into one
    final_video = concatenate_videoclips(video_clips, method="compose")

    # Write the final video to a file
    final_video.write_videofile("audio/final_video.mp4", codec="libx264", fps=24)

# Example usage:
# generate_and_save_audio_files(Title, explanations)
