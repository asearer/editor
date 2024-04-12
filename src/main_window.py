from PyQt5.QtWidgets import QMainWindow, QTextEdit, QVBoxLayout, QWidget, QAction, QFileDialog, QMessageBox
from src.editor import CodeEditor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multi-Language IDE")
        self.setGeometry(100, 100, 800, 600)

        self.editor = CodeEditor()
        self.init_ui()

    def init_ui(self):
        self.create_actions()
        self.create_menu()
        self.create_editor()
        self.create_status_bar()

    def create_actions(self):
        self.open_action = QAction("&Open", self)
        self.open_action.setShortcut("Ctrl+O")
        self.open_action.setStatusTip("Open file")
        self.open_action.triggered.connect(self.open_file)

        self.save_action = QAction("&Save", self)
        self.save_action.setShortcut("Ctrl+S")
        self.save_action.setStatusTip("Save file")
        self.save_action.triggered.connect(self.save_file)

    def create_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("&File")
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)

    def create_editor(self):
        self.editor_widget = QWidget()
        layout = QVBoxLayout()
        self.editor_textedit = QTextEdit()  # Change this line
        layout.addWidget(self.editor_textedit)  # Change this line
        self.editor_widget.setLayout(layout)
        self.setCentralWidget(self.editor_widget)
        self.editor_textedit.setPlainText(self.editor.current_file)  # Set contents

    def create_status_bar(self):
        self.statusBar().showMessage("Ready")

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File")
        if file_path:
            try:
                self.editor.open_file(file_path)
                self.editor_textedit.setPlainText(self.editor.current_file)
                self.statusBar().showMessage(f"Opened file: {file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to open file: {e}")

    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File")
        if file_path:
            try:
                self.editor.current_file = self.editor_textedit.toPlainText()
                self.editor.save_file(file_path)
                self.statusBar().showMessage(f"File saved: {file_path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save file: {e}")
