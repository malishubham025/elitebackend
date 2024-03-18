from openai import OpenAI
import os
def generate_explanations(slide_contents, topic_name):
    # Initialize the OpenAI client with your secure API key
    client = OpenAI(api_key=os.environ.get("openai_three"))

    # List to store unique titles
    unique_titles = []

    # List to store explanations
    explanations = []

    # Iterate over the titles
    for i in slide_contents:
        # title=(Title[i].lower())
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "this text  is related to " + topic_name + ". explain it  " + slide_contents[i]}
            ]
        )
        explanation = completion.choices[0].message.content
        # Append the explanation to the list of explanations
        explanations.append(explanation)
        print("slide number"+str(i))
    return explanations

# # Example usage:
# Title = {"1": "Title1", "2": "Title2", "3": "Title3"}  # Example Title dictionary
# topic_name = "Example Topic"  # Example topic name
# explanations = generate_explanations(Title, topic_name)
# print(explanations)  # Print explanations
