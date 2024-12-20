import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class HelloWorldApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Create a label
        self.label = QLabel('Hello, World!', self)

        # Create a button
        self.button = QPushButton('Click Me', self)
        self.button.clicked.connect(self.on_click)

        # Layout for the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # Set the layout for the main window
        self.setLayout(layout)

        # Window settings
        self.setWindowTitle('Hello World PyQt App')
        self.resize(300, 200)

    def on_click(self):
        # Update the label text when the button is clicked
        self.label.setText('Button Clicked!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = HelloWorldApp()
    main_window.show()
    sys.exit(app.exec_())
