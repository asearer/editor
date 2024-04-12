from PyQt5.QtWidgets import QMainWindow, QTextEdit, QVBoxLayout, QWidget, QAction, QFileDialog, QMessageBox, QMenu
from src.editor import CodeEditor

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

    def create_actions(self):
        self.open_action = QAction("&Open", self)
        self.open_action.setShortcut("Ctrl+O")
        self.open_action.setStatusTip("Open file")
        self.open_action.triggered.connect(self.open_file)

        self.save_action = QAction("&Save", self)
        self.save_action.setShortcut("Ctrl+S")
        self.save_action.setStatusTip("Save file")
        self.save_action.triggered.connect(self.save_file)

        self.create_project_action = QAction("&Project Creator", self)
        self.create_project_action.setStatusTip("Create a new project")
        self.create_project_action.triggered.connect(self.create_project)

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
        # Add edit actions here

    def create_view_menu(self, menubar):
        view_menu = menubar.addMenu("&View")
        # Add view actions here

    def create_project_menu(self, menubar):
        project_menu = menubar.addMenu("&Projects")
        project_menu.addAction(self.create_project_action)  # Add project creator action here

    def create_help_menu(self, menubar):
        help_menu = menubar.addMenu("&Help")
        # Add help actions here

    def create_editor(self):
        self.editor_widget = QWidget()
        layout = QVBoxLayout()
        self.editor_textedit = QTextEdit()  
        layout.addWidget(self.editor_textedit)  
        self.editor_widget.setLayout(layout)
        self.setCentralWidget(self.editor_widget)
        self.editor_textedit.setPlainText(self.editor.current_file)  

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

    def create_project(self):
        # Implement project creation functionality here
        pass
