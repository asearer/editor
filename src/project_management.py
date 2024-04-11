import os

class ProjectManagement:
    def __init__(self):
        # Initialize project management features
        pass

    def create_project(self, project_name):
        # Create a new project
        project_path = os.path.join(os.getcwd(), project_name)
        if not os.path.exists(project_path):
            os.makedirs(project_path)
            return f"Project '{project_name}' created successfully at '{project_path}'."
        else:
            return f"Project '{project_name}' already exists."

    # Add more methods as needed
