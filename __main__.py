from doc_writer import DocumentationWriter
import os

def main():
    # Ask the user for the project directory to generate docs for
    project_dir = input("Enter the path to the project folder: ")

    # Check if directory exists
    if not os.path.exists(project_dir):
        print(f"Error: Directory '{project_dir}' does not exist.")
        return
    # Initialize the DocumentationWriter with the project directory
    writer = DocumentationWriter(project_dir)

    # Generate the Documentation
    writer.generate_docs()
    print(f"Documentation has been generated for the project at: {project_dir}")

if __name__=="__main__":
    main()
