import openai
import os

# Ensure that your OpenAI API key is set as an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_documentation_markdown(prompt: str, sections: list, file_path: str):
    """
    Generates documentation based on a prompt and outputs it in Markdown format.
    
    Args:
    - prompt (str): The input prompt for generating documentation.
    - sections (list): List of sections to generate.
    - file_path (str): Path to save the generated Markdown file.
    
    Returns:
    None
    """
    
    # Create a string to hold all the Markdown content
    markdown_content = f"# Generated Documentation\n\n"
    markdown_content += f"**Prompt:** {prompt}\n\n"
    
    print("Generating documentation...")

    # Loop through sections and generate content for each in Markdown format
    for section in sections:
        try:
            print(f"Generating content for section: {section}")
            
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an assistant that generates structured documentation in Markdown."},
                    {"role": "user", "content": f"{prompt}. Please write the section about {section}."}
                ]
            )

            # Extract the generated content
            generated_content = response['choices'][0]['message']['content']
            print(f"Generated content for {section}: {generated_content[:50]}...")  # Print first 50 chars of content

            # Append each section's content with appropriate Markdown headings
            markdown_content += f"## {section}\n\n"
            markdown_content += f"{generated_content}\n\n"

        except Exception as e:
            # Handle errors and notify in the output document
            print(f"Error generating content for section '{section}': {e}")
            markdown_content += f"## {section}\n\n"
            markdown_content += f"Error generating content for this section: {e}\n\n"

    # Write the Markdown content to a file
    try:
        with open(file_path, 'w') as markdown_file:
            markdown_file.write(markdown_content)
        print(f"Markdown documentation successfully generated and saved to {file_path}")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Example usage
if __name__ == "__main__":
    prompt = "Generate comprehensive API documentation"
    sections = ["Introduction", "Setup", "Authentication", "CRUD Operations", "Examples"]
    file_path = "./generated_doc.md"
    
    generate_documentation_markdown(prompt, sections, file_path)
