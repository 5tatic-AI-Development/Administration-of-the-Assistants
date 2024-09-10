import openai
import os
import json

# Ensure that your OpenAI API key is set as an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_documentation_json(prompt: str, file_path: str):
    """
    Function to generate documentation in JSON format based on a prompt using the OpenAI API
    and save it to a specified file.
    
    Args:
    - prompt (str): The input prompt to generate documentation from.
    - file_path (str): The path to the file where the JSON documentation should be saved.
    
    The generated JSON format could look like this:
    {
        "title": "Generated Documentation Title",
        "description": "Generated description of the document",
        "sections": [
            {
                "heading": "Section Heading",
                "content": "Generated content for this section."
            },
            {
                "heading": "Another Section",
                "content": "Additional content here."
            }
        ]
    }
    """
    
    try:
        # OpenAI API call to generate document content
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Adjust model as needed
            messages=[
                {"role": "system", "content": "You are an assistant that helps to generate documentation."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extract the generated text from the response
        generated_content = response.choices[0].message['content']

        # Prepare the JSON structure for the document
        document_json = {
            "title": "Generated Documentation",
            "description": f"Documentation generated based on the prompt: {prompt}",
            "sections": [
                {
                    "heading": "Introduction",
                    "content": generated_content  # Here the generated content is inserted
                }
                # You can add more sections or split generated_content further based on your needs
            ]
        }

        # Write the JSON data to a file
        with open(file_path, 'w') as json_file:
            json.dump(document_json, json_file, indent=4)
        
        print(f"Documentation successfully generated and saved to {file_path}")

    except Exception as e:
        print(f"Error generating documentation: {e}")

if __name__ == "__main__":
    prompt = "Please generate documentation for a basic API with CRUD operations."
    file_path = "./generated_doc.json"
    generate_documentation_json(prompt, file_path)
