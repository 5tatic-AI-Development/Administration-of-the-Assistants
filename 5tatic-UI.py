import tkinter as tk
from tkinter import ttk
import openai
import os
import json

# Ensure OpenAI API key is set
openai.api_key = os.getenv("OPENAI_API_KEY")


# Function to generate documentation based on selected format
def generate_documentation(prompt, format_choice):
    sections = ["Introduction", "Setup", "Authentication", "CRUD Operations", "Examples"]
    file_path = f"./generated_doc.{format_choice}"

    if format_choice == "md":
        generate_documentation_markdown(prompt, sections, file_path)
    else:
        generate_documentation_json(prompt, sections, file_path)

    result_label.config(text=f"Documentation successfully generated at: {file_path}")


# Markdown generation function
def generate_documentation_markdown(prompt, sections, file_path):
    markdown_content = f"# Generated Documentation\n\n"
    markdown_content += f"**Prompt:** {prompt}\n\n"

    for section in sections:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an assistant that generates structured documentation in Markdown."},
                    {"role": "user", "content": f"{prompt}. Please write the section about {section}."}
                ]
            )
            generated_content = response['choices'][0]['message']['content']
            markdown_content += f"## {section}\n\n{generated_content}\n\n"
        except Exception as e:
            markdown_content += f"## {section}\n\nError: {e}\n\n"

    with open(file_path, 'w') as markdown_file:
        markdown_file.write(markdown_content)


# JSON generation function
def generate_documentation_json(prompt, sections, file_path):
    document_json = {
        "title": "Generated Documentation",
        "description": f"Documentation generated based on the prompt: {prompt}",
        "sections": []
    }

    for section in sections:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an assistant that generates structured documentation."},
                    {"role": "user", "content": f"{prompt}. Please write the section about {section}."}
                ]
            )
            generated_content = response['choices'][0]['message']['content']
            document_json["sections"].append({
                "heading": section,
                "content": generated_content
            })
        except Exception as e:
            document_json["sections"].append({
                "heading": section,
                "content": f"Error: {e}"
            })

    with open(file_path, 'w') as json_file:
        json.dump(document_json, json_file, indent=4)


# GUI setup
def setup_gui():
    window = tk.Tk()
    window.title("Documentation Generator")
    window.geometry("500x400")

    # Prompt input
    tk.Label(window, text="Enter Prompt:").pack(pady=10)
    prompt_entry = tk.Entry(window, width=50)
    prompt_entry.pack(pady=5)

    # Dropdown menu for format selection
    tk.Label(window, text="Choose Documentation Format:").pack(pady=10)
    format_var = tk.StringVar()
    format_dropdown = ttk.Combobox(window, textvariable=format_var, state="readonly")
    format_dropdown['values'] = ('md', 'json')
    format_dropdown.current(0)  # Default to markdown
    format_dropdown.pack(pady=5)

    # Generate button
    def on_generate():
        prompt = prompt_entry.get()
        format_choice = format_var.get()
        generate_documentation(prompt, format_choice)

    generate_button = tk.Button(window, text="Generate Documentation", command=on_generate)
    generate_button.pack(pady=20)

    # Result label
    global result_label
    result_label = tk.Label(window, text="")
    result_label.pack(pady=10)

    # Start the GUI loop
    window.mainloop()