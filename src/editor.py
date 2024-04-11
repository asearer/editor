class CodeEditor:
    def __init__(self):
        # Initialize code editor
        self.current_file = ""

    def open_file(self, file_path):
        # Open file in code editor
        with open(file_path, "r") as file:
            self.current_file = file.read()

    def save_file(self, file_path):
        # Save file from code editor
        with open(file_path, "w") as file:
            file.write(self.current_file)

