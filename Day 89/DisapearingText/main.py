import logging
import sys

from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit, QVBoxLayout, QWidget

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
WINDOW_TITLE = "Disappearing Text"
WINDOW_ICON_PATH = 'icon.png'
TIMER = 20
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
DEFAULT_LOG_LEVEL = logging.INFO


class DisappearTextWindow(QMainWindow):
    """Main window class for the Disappearing Text application."""

    def __init__(self) -> None:
        """Initialize the DisappearTextWindow."""

        super().__init__()

        self.timer = None
        self.time_left = None

        self.label_timer = None
        self.text_editor = None

        self.init_ui()
        self.init_timer()
        self.reset_timer()

    def init_ui(self) -> None:
        """Initialize UI components."""
        self.setGeometry(200, 200, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setWindowTitle(WINDOW_TITLE)
        self.setWindowIcon(QIcon(WINDOW_ICON_PATH))

        # Main layout
        main_layout = QVBoxLayout()

        # Setting up the QLabel
        self.label_timer = QLabel(f"Time left: {TIMER}")
        self.configureLabel(self.label_timer, 18, True, Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.label_timer)

        # Setting up the QTextEdit
        self.text_editor = QTextEdit(self)
        self.text_editor.textChanged.connect(self.reset_timer)
        main_layout.addWidget(self.text_editor)

        # Set main layout to central widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def init_timer(self) -> None:
        """Initialize timer related attributes and connections."""
        self.timer = QTimer(self)
        self.time_left = TIMER
        self.timer.timeout.connect(self.update_timer)
        logging.info("Initializing the timer.")

    def reset_timer(self) -> None:
        """Stop the current timer, reset the countdown, and restart the timer."""
        self.timer.stop()
        self.time_left = TIMER  # Reset the time_left to TIMER value
        self.label_timer.setStyleSheet("color: black")
        self.label_timer.setText(f"Time left: {self.time_left}")  # Reset the label
        self.timer.start(1000)  # Start the timer with an interval of 1 second
        logging.info("Reset the timer.")

    def update_timer(self) -> None:
        """Decrement the countdown by one and clear the text editor if time reaches zero."""
        self.time_left -= 1

        if self.time_left <= 5:
            self.label_timer.setStyleSheet("color: red")
        self.label_timer.setText(f"Time left: {self.time_left}")

        if self.time_left == 0:
            logging.warning("Timer reached zero!")
            self.text_editor.clear()

    @staticmethod
    def configureLabel(label: QLabel, font_size: int, is_bold: bool, alignment: Qt.AlignmentFlag) -> None:
        """Configure a QLabel widget."""
        font = QFont()
        font.setPointSize(font_size)
        font.setBold(is_bold)
        label.setFont(font)
        label.setAlignment(alignment)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    logging.basicConfig(level=DEFAULT_LOG_LEVEL, format=LOG_FORMAT)
    main_window = DisappearTextWindow()
    main_window.show()
    app.exec()
