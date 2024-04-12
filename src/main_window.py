from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox, QMenu, QInputDialog, QSplitter
from PyQt5.QtCore import Qt
import os

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
            QSplitter::handle {
                background-color: #666;
            }
            QSplitter::handle:horizontal {
                width: 3px;
            }
            QSplitter::handle:vertical {
                height: 3px;
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
        self.open_action.triggered.connect(self.open_file)

        self.save_action = QAction("&Save", self)
        self.save_action.setShortcut("Ctrl+S")
        self.save_action.setStatusTip("Save file")
        self.save_action.triggered.connect(self.save_file)

        self.font_size_action = QAction("&Font Size", self)
        self.font_size_action.setStatusTip("Adjust font size")
        self.font_size_action.triggered.connect(self.set_font_size)

        self.project_creator_action = QMenu("&Project Creator", self)
        self.add_project_options()

    def add_project_options(self):
        projects = [
            "Dart", 
            "Flask/Django", 
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
        self.create_file_menu(menubar)
        self.create_edit_menu(menubar)
        self.create_view_menu(menubar)
        self.create_project_menu(menubar)
        self.create_help_menu(menubar)

    def create_file_menu(self, menubar):
        file_menu = menubar.addMenu("&File")
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)

    def create_edit_menu(self, menubar):
        edit_menu = menubar.addMenu("&Edit")
        edit_menu.addAction(self.font_size_action)  

    def create_view_menu(self, menubar):
        view_menu = menubar.addMenu("&View")

    def create_project_menu(self, menubar):
        project_menu = menubar.addMenu("&Projects")
        project_menu.addMenu(self.project_creator_action)  

    def create_help_menu(self, menubar):
        help_menu = menubar.addMenu("&Help")
        # Add help actions here

    def create_editor(self):
        self.editor_widget = QSplitter()
        self.editor_widget.setOrientation(Qt.Vertical)  # Default vertical layout

        # Create two text edit widgets
        self.editor_textedit_1 = QTextEdit()
        self.editor_textedit_2 = QTextEdit()

        # Add the text edit widgets to the splitter
        self.editor_widget.addWidget(self.editor_textedit_1)
        self.editor_widget.addWidget(self.editor_textedit_2)

        self.setCentralWidget(self.editor_widget)
        self.editor_textedit_1.setPlainText(self.editor.current_file)
        self.editor_textedit_2.setPlainText(self.editor.current_file)

    def create_status_bar(self):
        self.statusBar().showMessage("Ready")

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File")
        if file_path:
            try:
                self.editor.open_file(file_path)
                self.editor_textedit_1.setPlainText(self.editor.current_file)
                self.editor_textedit_2.setPlainText(self.editor.current_file)
                self.statusBar().showMessage(f"Opened file: {file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to open file: {e}")

    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File")
        if file_path:
            try:
                self.editor.current_file = self.editor_textedit_1.toPlainText()
                self.editor.save_file(file_path)
                self.statusBar().showMessage(f"File saved: {file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save file: {e}")

    def set_font_size(self):
        font_size, ok = QInputDialog.getInt(self, "Font Size", "Enter font size:", self.editor_textedit_1.font().pointSize(), 1, 100)
        if ok:
            font = self.editor_textedit_1.font()
            font.setPointSize(font_size)
            self.editor_textedit_1.setFont(font)
            self.editor_textedit_2.setFont(font)

    # Added create_project method
    def create_project(self, project_name):
        save_location = QFileDialog.getExistingDirectory(self, "Select save location")
        if save_location:
            create_project(project_name, save_location)
