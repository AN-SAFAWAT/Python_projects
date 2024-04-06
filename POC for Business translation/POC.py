
from openai import OpenAI
client=OpenAI()#your original API keys may need to pay for using openai

def translate_text(input_text, source_lang, target_lang):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", # Use the correct model ID
            messages=[
                {"role": "system", "content":"you are a great translator"},
                {"role": "user", "content": f"translate the next sentence from {source_lang} to {target_lang}: {input_text}"}
            ]
        )
        # Extract the translated text
        translated_text = response.choices[0].message.content
        print(translated_text)
        return translated_text.strip()
    except Exception as e:  # It's better to catch a specific exception.
        print(f"An error occurred: {e}")
        return None



def read_document(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_document(file_path, content):
    if content is not None:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    else:
        print("No content to write")

# Your file paths, source and target languages remain the same
# ...
input_file_path = '/Users/leo_mac/Documents/demotxtfile/demo.txt'
output_file_path = '/Users/leo_mac/Documents/demotxtfile/tran.txt'
source_language = 'Spanish'
target_language = 'English'

# Read the content of the document
original_text = read_document(input_file_path)
#print(original_text)
# Translate the text
translated_text = translate_text(original_text, source_language, target_language)
print(translated_text)
if translated_text is not None:
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(translated_text)
    print(f"Translated text written to {output_file_path}")
else:
    print("Translation failed, no output written.")


# Execute your file operations as before
# ...





