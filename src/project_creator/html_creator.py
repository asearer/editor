# generate_html.py
import os

def generate_html(project_name):
    # Create project directory
    os.makedirs(project_name)
    os.chdir(project_name)

    # Create index.html
    with open("index.html", "w") as f:
        f.write("<!DOCTYPE html>\n<html>\n<head>\n<title></title>\n</head>\n<body>\n  <script src='script.js'></script>\n</body>\n</html>")

    return f"HTML project '{project_name}' created successfully!"
