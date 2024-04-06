                         Text Translation Utility

Description
This utility is designed to translate text from one language to another using
OpenAI's GPT-3.5 Turbo model. It reads a source text file, translates the
content, and writes the translated text to a new file. This script is useful
for quick translations of documents or any text files from Spanish to English 
or any other language pairs supported by OpenAI.

Requirements
Python 3.x
openai Python package
To install the required package, run:

bash
Copy code
pip install openai
Configuration
Before running the script, you need to set up your OpenAI API key. This can be done by setting an environment variable OPENAI_API_KEY with your API key as the value.

For Unix/Linux/macOS:

bash
Copy code
export OPENAI_API_KEY='your_api_key_here'
For Windows:

cmd
Copy code
set OPENAI_API_KEY=your_api_key_here

Usage:
Update the input_file_path and output_file_path in the script to reflect the
locations of your source and target files, respectively.
Specify the source_language and target_language in the script. The default is
set from Spanish to English.


Limitations
The accuracy of the translation may vary depending on the complexity of the text and the languages involved.
The script uses OpenAI's GPT-3.5 Turbo model, which may incur costs based on usage. Please check OpenAI's pricing details.
Troubleshooting
If you encounter any errors, ensure that:

Your API key is correctly set up and has not exceeded its usage limits.
The input and output file paths are correctly specified and accessible.
The specified languages are supported by OpenAI's translation capabilities.

