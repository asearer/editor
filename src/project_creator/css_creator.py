# generate_css.py
import os

def generate_css(project_name):
    # Create project directory
    os.makedirs(project_name)
    os.chdir(project_name)

    # Create styles.css
    with open("styles.css", "w") as f:
        f.write("/* CSS */\n\nbody {\n  /* Styles */\n}")

    return f"CSS project '{project_name}' created successfully!"
