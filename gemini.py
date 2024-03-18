import google.generativeai as genai
import textwrap
import markdown

# def to_markdown(text):
#   text = text.replace('•', '  *')
#   return markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
newexplain={}



import PIL

def generate_image_explanations(Title, images_presence, file_paths, model,explanations):
    print("hi=====================")
    # title=""
    for i in range(len(images_presence)):
        # print("hi",i)
        # print(i,Title[i].lower())
        # if(len(Title[i])>0):
        # title=Title[i].lower()
        title=Title[str(i)].lower()
        print(file_paths[i])
        try:
            # temp=explain
            img = PIL.Image.open(file_paths[i])
            response = model.generate_content(["explain image which in this  image  ", img])
            response.resolve()
            # to_markdown(response.text)

            explanations[i]+=response.text
            # print(response.text)
            print("explained "+title+str(i))
        except:
            print("error while reading "+str(i))
    # print("complete")
    return explanations


# Example usage:
# explanations = generate_image_explanations(Title, images_presence, file_paths, model,to_markdown)