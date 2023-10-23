import json
import logging
import random
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, \
    QWidget, QMessageBox
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QTimer, Qt, QEvent

import word_list

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 250
WINDOW_TITLE = "Typing Speed Test"
WINDOW_ICON_PATH = 'icon.png'
TIMER = 60
MAX_LENGTH = 30
MAX_WORDS = 100
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
DEFAULT_LOG_LEVEL = logging.INFO


class TypingTestWindow(QMainWindow):
    """Main window class for the Typing Speed Test application."""

    def __init__(self) -> None:
        """Initialize the TypingTestWindow."""
        super().__init__()

        self.timer = None
        self.wordlist = []
        self.correct_words = []
        self.word_index = 0
        self.current_word = ""
        self.counter = 0
        self.current_cpm = 0
        self.current_wpm = 0

        self.corrected_cpm_label = None
        self.wpm_label = None
        self.time_left_label = None
        self.start_button = None
        self.stop_button = None
        self.label_previous = None
        self.label_current = None
        self.label_next = None
        self.time_left = None
        self.typing_input = None

        self.init_ui()
        self.init_timer()

    def init_ui(self) -> None:
        """Initialize UI components."""
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setWindowTitle(WINDOW_TITLE)
        self.setWindowIcon(QIcon(WINDOW_ICON_PATH))
        logging.info("Initializing the TypingTestWindow.")

        # Main layout
        main_layout = QVBoxLayout()

        # Top metrics
        self.setup_metrics(main_layout)

        # Controls (Start, Stop buttons)
        self.setup_controls(main_layout)

        # Typing challenge area
        self.setup_challenge(main_layout)

        # Typing input area
        self.setup_input(main_layout)

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

    def setup_metrics(self, main_layout) -> None:
        """Set up metric labels."""
        metrics_layout = QHBoxLayout()

        self.corrected_cpm_label = QLabel("Corrected CPM: ?")
        self.wpm_label = QLabel("WPM: ?")
        self.time_left_label = QLabel(f"Time left: {TIMER}")

        for label in [self.corrected_cpm_label, self.wpm_label, self.time_left_label]:
            metrics_layout.addWidget(label)

        main_layout.addLayout(metrics_layout)

    def setup_controls(self, main_layout: QVBoxLayout) -> None:
        """Set up control buttons."""
        control_layout = QHBoxLayout()

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_game)
        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.reset_game)

        for button in [self.start_button, self.stop_button]:
            control_layout.addWidget(button)

        main_layout.addLayout(control_layout)

    def setup_challenge(self, main_layout: QVBoxLayout) -> None:
        """Set up challenge labels."""
        challenge_layout = QHBoxLayout()

        self.label_previous = QLabel("Word1")
        self.label_current = QLabel("Word2")
        self.label_current.setFont(QFont("Arial", 25, QFont.Weight.Bold))
        self.label_next = QLabel("Word3")

        for label in [self.label_previous, self.label_current, self.label_next]:
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            challenge_layout.addWidget(label)

        main_layout.addLayout(challenge_layout)

    def setup_input(self, main_layout: QVBoxLayout) -> None:
        """Set up input line edit."""
        self.typing_input = QLineEdit()
        self.typing_input.textChanged.connect(self.handle_text_changed)
        self.typing_input.textChanged.connect(self.update_label_highlight)
        self.typing_input.installEventFilter(self)
        self.typing_input.setPlaceholderText("Type the words here")
        font_metrics = self.typing_input.fontMetrics()
        width_for_characters = font_metrics.boundingRect('a' * MAX_LENGTH).width()
        self.typing_input.setFixedWidth(width_for_characters)
        self.typing_input.setEnabled(False)

        h_layout = QHBoxLayout()
        h_layout.addStretch()
        h_layout.addWidget(self.typing_input)
        h_layout.addStretch()
        main_layout.addLayout(h_layout)

    def start_timer(self) -> None:
        """Start the timer."""
        self.timer.start(1000)
        logging.info("Starting the timer.")

    def stop_timer(self) -> None:
        """Stop the timer and reset its value."""
        self.timer.stop()
        self.time_left = TIMER
        self.time_left_label.setText(f"Time left: {self.time_left}")
        logging.info("Stopping the timer.")

    def update_timer(self) -> None:
        """Update timer value on the label."""
        self.time_left -= 1
        self.time_left_label.setText(f"Time left: {self.time_left}")
        if self.time_left == 0:
            logging.warning("Timer reached zero!")
            self.check_result()
            self.reset_game()

    def handle_text_changed(self, text: str) -> None:
        """Center the text in the input."""
        actual_text = text.strip()
        spaces_needed = MAX_LENGTH - len(actual_text)
        spaces_before = spaces_needed // 2 + 7
        spaces_after = spaces_needed - spaces_before

        centered_text = ' ' * spaces_before + actual_text + ' ' * spaces_after
        self.typing_input.blockSignals(True)  # Block signals to prevent recursive call
        self.typing_input.setText(centered_text)
        self.typing_input.setCursorPosition(spaces_before + len(actual_text))
        self.typing_input.blockSignals(False)  # Unblock signals

    def start_game(self) -> None:
        """Initializes and starts the typing game."""
        logging.info("Starting the game.")
        self.wordlist = random.sample(word_list.word_list, MAX_WORDS)
        self.word_index = 0
        self.current_cpm = 0
        self.current_wpm = 0
        self.corrected_cpm_label.setText(f"Corrected CPM: 0")
        self.wpm_label.setText(f"WPM: 0")
        self.update_labels(self.wordlist, self.word_index)
        self.typing_input.setEnabled(True)
        self.start_timer()
        self.typing_input.setFocus()

    def reset_game(self) -> None:
        """Resets and stops the current game session."""
        logging.info("Stopping the game")
        self.wordlist = None
        self.word_index = 0
        self.current_word = None
        self.current_cpm = 0
        self.current_wpm = 0
        self.update_labels(["Word1", "Word2", "Word3"], 1)
        self.corrected_cpm_label.setText(f"Corrected CPM: 0")
        self.wpm_label.setText(f"WPM: 0")
        self.typing_input.setText("")
        self.typing_input.setEnabled(False)
        self.stop_timer()

    def update_counters(self) -> None:
        """Updates the typing speed counters for the game."""
        self.current_cpm = int(self.get_correct_chars() / (TIMER - self.time_left) * TIMER)
        self.current_wpm = int(self.counter / (TIMER - self.time_left) * TIMER)

        self.corrected_cpm_label.setText(f"Corrected CPM: {self.current_cpm}")
        self.wpm_label.setText(f"WPM: {self.current_wpm}")

    def get_correct_chars(self) -> int:
        """Returns the number of correctly typed characters."""
        return sum(len(word) for word in self.correct_words)

    def update_labels(self, wordlist: list[str], word_index: int, correct: int = -1) -> None:
        """Updates the displayed words based on the player's progress."""
        if word_index >= 1:
            self.label_previous.setText(wordlist[word_index - 1])
            color = "green" if correct == 1 else "red" if correct == 0 else ""
            self.label_previous.setStyleSheet(f"color: {color};")
        else:
            self.label_previous.setText("")

        self.current_word = wordlist[word_index]
        self.label_current.setText(self.current_word)

        self.label_next.setText(wordlist[word_index + 1] if word_index + 1 < len(wordlist) else "")

    def update_label_highlight(self):
        """Highlights the currently typed word based on its correctness."""
        typed_text = self.typing_input.text().strip()

        # Check how much of the typed text matches the label text
        common_length = 0
        try:
            max_length = min(len(self.current_word), len(typed_text))
        except TypeError:
            return
        for i in range(max_length):
            if self.current_word[i] == typed_text[i]:
                common_length = i + 1
            else:
                break

        # Split the label text based on the common_length
        matched_text = self.current_word[:common_length]
        unmatched_text = self.current_word[common_length:]

        # Apply HTML styling
        if matched_text == typed_text:
            html_text = f'<span style="color: green;">{matched_text}</span>{unmatched_text}'
        else:
            html_text = f'<span style="color: red;">{self.current_word}</span>'

        self.label_current.setText(html_text)

    @staticmethod
    def update_record(key: str, value: int) -> None:
        """Updates the typing records in a JSON file."""
        with open('records.json', 'r') as file:
            data = json.load(file)

        data['typing_stats'][key] = value

        with open('records.json', 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def show_record_message(title: str, message: str) -> None:
        """Displays a message box with typing records information."""
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.exec()

    def check_result(self) -> None:
        """Checks and updates if the player has set new typing records."""
        with open('records.json', 'r') as file:
            data = json.load(file)

        record_cpm = data['typing_stats']['corrected_CPM']
        record_wpm = data['typing_stats']['WPM']

        if self.current_cpm > record_cpm and self.current_wpm > record_wpm:
            self.show_record_message("You have set a new record!", "Congratulations, you have set new records!")
        elif self.current_cpm > record_cpm:
            self.update_record('corrected_CPM', self.current_cpm)
            self.show_record_message("You have set a new CCPM record!", "Congratulations on your new CCPM record!")
        elif self.current_wpm > record_wpm:
            self.update_record('WPM', self.current_wpm)
            self.show_record_message("You have set a new WPM record!", "Congratulations on your new WPM record!")
        else:
            self.show_record_message("Try again!", "You have not set any new record")

    def eventFilter(self, source, event):
        """Filters key press events for specific elements."""
        if source == self.typing_input and event.type() == QEvent.Type.KeyPress:
            self.keyPressEvent(event)
        return super().eventFilter(source, event)

    def keyPressEvent(self, event):
        """Handles space key presses to validate typed words."""
        if event.key() == Qt.Key.Key_Space:
            logging.debug("Space key pressed. Validating the word.")
            self.word_index += 1
            if self.typing_input.text().strip() == self.current_word:
                self.counter += 1
                self.correct_words.append(self.current_word)
                self.update_labels(self.wordlist, self.word_index, 1)
            else:
                self.update_labels(self.wordlist, self.word_index, 0)
            self.update_counters()
            self.typing_input.setText("")
        super().keyPressEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    logging.basicConfig(level=DEFAULT_LOG_LEVEL, format=LOG_FORMAT)
    window = TypingTestWindow()
    window.show()
    sys.exit(app.exec())
