import os

def create_project(project_name, save_location):
    if not project_name:
        raise ValueError("Please enter a project name.")

    if not save_location:
        raise ValueError("Please select a save location.")

    # Create project directory
    project_dir = os.path.join(save_location, project_name)
    os.makedirs(project_dir, exist_ok=True)

    # Create lib directory
    lib_dir = os.path.join(project_dir, "lib")
    os.makedirs(lib_dir, exist_ok=True)

    # Create main Dart file
    main_file = os.path.join(lib_dir, project_name + ".dart")
    with open(main_file, "w") as f:
        f.write('void main() {\n  print("Hello, ' + project_name + '!");\n}')

    return f"Project '{project_name}' created successfully."

