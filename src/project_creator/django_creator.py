import os

def create_django_project(project_name, directory):
    # Create Django project directory
    project_path = os.path.join(directory, project_name)
    os.makedirs(project_path)
    
    # Create Django project
    os.system(f"django-admin startproject {project_name} --directory {project_path}")
    
    # Create app directory and __init__.py file
    app_path = os.path.join(project_path, project_name)
    os.makedirs(app_path)
    with open(os.path.join(app_path, "__init__.py"), "w") as file:
        pass
    
    # Create views.py file with default view
    with open(os.path.join(app_path, "views.py"), "w") as file:
        file.write("from django.http import HttpResponse\n\n")
        file.write("def index(request):\n")
        file.write("    return HttpResponse('Hello, Django!')")

    return f"Django project '{project_name}' created successfully!"
