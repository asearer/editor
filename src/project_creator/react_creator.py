# generate_react.py
import os

def generate_react(project_name):
    # Create React project using create-react-app
    os.system(f"npx create-react-app {project_name}")
    return f"React project '{project_name}' created successfully!"
