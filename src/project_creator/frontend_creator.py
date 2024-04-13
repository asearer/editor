import os

def generate_html(project_name):
    # Create project directory
    os.makedirs(project_name)
    os.chdir(project_name)

    # Create index.html
    with open("index.html", "w") as f:
        f.write("<!DOCTYPE html>\n<html>\n<head>\n<title></title>\n</head>\n<body>\n  <script src='script.js'></script>\n</body>\n</html>")

    return f"HTML project '{project_name}' created successfully!"

def generate_css(project_name):
    # Create project directory
    os.makedirs(project_name)
    os.chdir(project_name)

    # Create styles.css
    with open("styles.css", "w") as f:
        f.write("/* CSS */\n\nbody {\n  /* Styles */\n}")

    return f"CSS project '{project_name}' created successfully!"

def generate_javascript(project_name):
    # Create project directory
    os.makedirs(project_name)
    os.chdir(project_name)

    # Create script.js
    with open("script.js", "w") as f:
        f.write("// JavaScript\n\nconsole.log('Hello, World!');")

    return f"JavaScript project '{project_name}' created successfully!"

def generate_react(project_name):
    # Create React project using create-react-app
    os.system(f"npx create-react-app {project_name}")
    return f"React project '{project_name}' created successfully!"
