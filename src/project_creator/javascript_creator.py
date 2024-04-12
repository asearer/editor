# generate_javascript.py
import os

def generate_javascript(project_name):
    # Create project directory
    os.makedirs(project_name)
    os.chdir(project_name)

    # Create script.js
    with open("script.js", "w") as f:
        f.write("// JavaScript\n\nconsole.log('Hello, World!');")

    return f"JavaScript project '{project_name}' created successfully!"
