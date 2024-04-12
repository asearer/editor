import os

def create_flask_project(project_name, directory):
    # Create project directory
    project_path = os.path.join(directory, project_name)
    os.makedirs(project_path)
    
    # Create Flask app file
    with open(f"{project_path}/app.py", "w") as file:
        file.write(f"from flask import Flask\n\napp = Flask(__name__)\n\n@app.route('/')\ndef index():\n    return 'Hello, Flask!'\n\nif __name__ == '__main__':\n    app.run(debug=True)")

    return f"Flask project '{project_name}' created successfully!"
