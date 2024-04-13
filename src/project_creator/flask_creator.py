import os

def create_project(project_name, save_location):
    if not project_name:
        raise ValueError("Please enter a project name.")

    if not save_location:
        raise ValueError("Please select a save location.")

    # Create project directory
    project_dir = os.path.join(save_location, project_name)
    os.makedirs(project_dir, exist_ok=True)
    
    # Create Flask app file
    with open(f"{project_path}/app.py", "w") as file:
        file.write(f"from flask import Flask\n\napp = Flask(__name__)\n\n@app.route('/')\ndef index():\n    return 'Hello, Flask!'\n\nif __name__ == '__main__':\n    app.run(debug=True)")

    return f"Flask project '{project_name}' created successfully!"
