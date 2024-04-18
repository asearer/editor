import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QMessageBox, QFileDialog, QInputDialog
from PyQt5.QtCore import Qt, pyqtSlot
import subprocess

# Adjusted import statement for the create_project function
from src.project_creator.dart_creator import create_project  

class CodeEditor:
    def __init__(self):
        self.current_file = ""

    def open_file(self, file_path):
        with open(file_path, "r") as f:
            self.current_file = f.read()

    def save_file(self, file_path):
        with open(file_path, "w") as f:
            f.write(self.current_file)

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

        self.process = subprocess.Popen(
            ['/bin/bash'],
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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Alonza's Pretty OK IDE")
        self.setGeometry(100, 100, 800, 600)

        self.editor = CodeEditor()
        self.init_ui()

    def init_ui(self):
        self.create_actions()
        self.create_menus()
        self.create_editor()
        self.create_status_bar()

        # Set dark mode style sheet
        self.setStyleSheet("""
            QMainWindow {
                background-color: #333;
                color: #fff;
            }
            QMenuBar {
                background-color: #666;
                color: #fff;
            }
            QMenuBar::item {
                background-color: #666;
                color: #fff;
            }
            QMenuBar::item:selected {
                background-color: #888;
            }
            QMenu {
                background-color: #666;
                color: #fff;
            }
            QMenu::item {
                background-color: #666;
                color: #fff;
            }
            QMenu::item:selected {
                background-color: #888;
            }
            QTextEdit {
                background-color: #444;
                color: #fff;
                selection-background-color: #888;
            }
            QTextEdit:focus {
                border: 2px solid #fff;
            }
            QTextEdit::selection {
                background-color: #888;
            }
            """)

    def create_actions(self):
        self.open_action = QAction("&Open", self)
        self.open_action.setShortcut("Ctrl+O")
        self.open_action.setStatusTip("Open file")
        self.open_action.triggered.connect(self.open_file_dialog)

        self.save_action = QAction("&Save", self)
        self.save_action.setShortcut("Ctrl+S")
        self.save_action.setStatusTip("Save file")
        self.save_action.triggered.connect(self.save_file_dialog)

        self.font_size_action = QAction("&Font Size", self)
        self.font_size_action.setStatusTip("Adjust font size")
        self.font_size_action.triggered.connect(self.set_font_size)

        self.project_creator_action = QMenu("&Project Creator", self)
        self.add_project_options()

    def add_project_options(self):
        projects = [
            "Dart", 
            "Flask",
            "Django",
            "Go", 
            "Java", 
            "JavaScript", 
            "Julia", 
            "Kotlin", 
            "Node", 
            "Nim", 
            "PHP", 
            "Python", 
            "Rust"
        ]
        projects.sort()
        for project in projects:
            action = QAction(project, self)
            action.triggered.connect(lambda _, project=project: self.create_project(project))
            self.project_creator_action.addAction(action)

    def create_menus(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("&File")
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)

        edit_menu = menubar.addMenu("&Edit")
        edit_menu.addAction(self.font_size_action)  

        view_menu = menubar.addMenu("&View")

        project_menu = menubar.addMenu("&Projects")
        project_menu.addMenu(self.project_creator_action)  

        help_menu = menubar.addMenu("&Help")

    def create_editor(self):
        self.terminal_emulator = TerminalEmulator()  # Create TerminalEmulator widget
        self.setCentralWidget(self.terminal_emulator)  # Set central widget to the terminal emulator

    def create_status_bar(self):
        self.statusBar().showMessage("Ready")

    @pyqtSlot()
    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)")
        if file_path:
            self.editor.open_file(file_path)

    @pyqtSlot()
    def save_file_dialog(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "All Files (*);;Text Files (*.txt)")
        if file_path:
            self.editor.current_file = self.editor_textedit_1.toPlainText()
            self.editor.save_file(file_path)

    @pyqtSlot()
    def set_font_size(self):
        font_size, ok = QInputDialog.getInt(self, "Font Size", "Enter font size:", value=12, min=6, max=72)
        if ok:
            font = self.editor_textedit_1.font()
            font.setPointSize(font_size)
            self.editor_textedit_1.setFont(font)
            self.editor_textedit_2.setFont(font)

    @pyqtSlot(str)
    def create_project(self, project):
        create_project(project)
        QMessageBox.information(self, "Project Created", f"{project} project created successfully.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

