import platform

class TerminalEmulator(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        self.input_entry = QLineEdit()
        self.input_entry.returnPressed.connect(self.execute_command)
        layout.addWidget(self.input_entry)

        self.setLayout(layout)

        if platform.system() == "Windows":
            shell = "cmd.exe"
        else:
            shell = "/bin/bash"

        self.process = subprocess.Popen(
            [shell],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            bufsize=1,
            universal_newlines=True
        )

        self.update_output()

    def execute_command(self):
        command = self.input_entry.text()
        self.input_entry.clear()
        self.process.stdin.write(command + '\n')
        self.process.stdin.flush()
        self.update_output()

    def update_output(self):
        output = self.process.stdout.readline()
        self.output_text.append(output.strip())

