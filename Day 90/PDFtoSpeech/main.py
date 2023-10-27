import json
import logging
import sys
import threading
import time

import PyPDF2
import pygame.mixer
import requests
from PyQt6.QtWidgets import (QApplication, QMainWindow, QHBoxLayout, QVBoxLayout,
                             QPushButton, QFileDialog, QTextEdit, QWidget, QMessageBox)
from PyQt6.QtGui import QIcon

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
WINDOW_TITLE = "PDF to Speech"
WINDOW_ICON_PATH = 'icon.png'
TTS_URL = "http://api.voicerss.org/"
CREDS = "creds.json"
AUDIO_FILE_PATH = "output_audio.mp3"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DEFAULT_LOG_LEVEL = logging.INFO


class PDFtoSpeech(QMainWindow):
    """Main window class for the PDF to Speech application."""

    def __init__(self) -> None:
        """Initialize the PDFtoSpeechWindow."""
        super().__init__()

        self.convert_text_button = None
        self.text = ""
        self._stop_music = threading.Event()

        self.open_button = None
        self.text_display = None
        self.play_sound_button = None
        self.stop_sound_button = None

        self.init_ui()

    def init_ui(self) -> None:
        """Sets up the user interface and layout of the main window."""
        # Set main window properties
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setWindowTitle(WINDOW_TITLE)
        self.setWindowIcon(QIcon(WINDOW_ICON_PATH))

        # Create the main layout
        main_layout = QVBoxLayout()

        # Add a button to open a PDF file
        self.open_button = QPushButton('Open PDF', self)
        self.open_button.clicked.connect(self.open_pdf)
        main_layout.addWidget(self.open_button)

        # Add a QTextEdit to show PDF content
        self.text_display = QTextEdit(self)
        self.text_display.setReadOnly(True)
        main_layout.addWidget(self.text_display)

        # Add buttons for converting the text and playing the sound
        button_layout = QHBoxLayout()
        self.convert_text_button = QPushButton('Generate TSS', self)
        self.convert_text_button.clicked.connect(self.convert_text_to_speech)
        self.convert_text_button.setEnabled(False)
        self.play_sound_button = QPushButton('Play TTS', self)
        self.play_sound_button.clicked.connect(self.start_play_mp3)
        self.play_sound_button.setEnabled(False)
        self.stop_sound_button = QPushButton('Stop TTS', self)
        self.stop_sound_button.clicked.connect(self.stop_playing)
        self.stop_sound_button.setEnabled(False)
        button_layout.addWidget(self.convert_text_button)
        button_layout.addWidget(self.play_sound_button)
        button_layout.addWidget(self.stop_sound_button)
        main_layout.addLayout(button_layout)

        # Set layout to central widget
        central_widget = QWidget(self)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def open_pdf(self) -> None:
        """Opens a dialog for the user to select a PDF file and then extracts its text."""
        file_name, _ = QFileDialog.getOpenFileName(self, "Open PDF", "", "PDF Files (*.pdf);;All Files (*)")
        if file_name:
            logging.info(f"PDF file {file_name} selected.")
            self.extract_text_from_pdf(file_name)

    def extract_text_from_pdf(self, path: str) -> None:
        """Extracts text from the given PDF file path and displays it in the UI."""
        self.text = ""
        logging.info(f"Extracting text from {path}.")
        with open(path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)

            num_pages = len(pdf_reader.pages)
            logging.info(f"{num_pages} pages found in the PDF.")
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                self.text += page.extract_text()

        self.text_display.setPlainText(self.text)
        self.convert_text_button.setEnabled(True)
        logging.info("Text extraction completed.")

    def convert_text_to_speech(self) -> None:
        """Converts the extracted text to speech using an external API and saves the audio."""
        key = ""
        try:
            with open(file=CREDS, mode="r") as f:
                data = json.load(f)
        except FileNotFoundError:
            logging.error("Credentials file not found.")
        else:
            key = data["API_KEY"]

        logging.info("Converting text to speech.")
        payload = {
            "key": key,
            "src": self.text,
            "hl": "en-us",
            "r": '0',
            "c": 'mp3',
            "f": 'ulaw_44khz_stereo'
        }

        try:
            response = requests.post(TTS_URL, params=payload)
            response.raise_for_status()
        except requests.ConnectionError:
            logging.error("Failed to establish a connection to the server.")
            QMessageBox.warning(self, "Error", "Failed to establish a connection to the server.")
        except requests.Timeout:
            logging.error("The request timed out.")
            QMessageBox.warning(self, "Error", "The request timed out.")
        except requests.RequestException as error:
            logging.error(f"An error occurred while making the request: {error}")
            QMessageBox.warning(self, "Error", "Could not convert the text to speech. Please try again.")
        else:
            with open(AUDIO_FILE_PATH, 'wb') as audio_file:
                audio_file.write(response.content)
            logging.info("Audio file generated and saved.")
            self.play_sound_button.setEnabled(True)

    def start_play_mp3(self) -> None:
        """Initializes a thread to start the audio playback."""
        logging.info("Starting playback of the audio file.")
        self._stop_music.clear()
        thread = threading.Thread(target=self.play_mp3)
        thread.start()
        self.stop_sound_button.setEnabled(True)

    def play_mp3(self) -> None:
        """Plays the converted audio using pygame until it ends or is stopped."""
        pygame.mixer.init()
        pygame.mixer.music.load(AUDIO_FILE_PATH)
        pygame.mixer.music.play()

        logging.info("Audio playback initialized.")
        while not self._stop_music.is_set() and pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.music.stop()
        logging.info("Audio playback finished.")

    def stop_playing(self) -> None:
        """Stops the audio playback on user command."""
        logging.info("Stopping playback on user command.")
        self._stop_music.set()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    logging.basicConfig(level=DEFAULT_LOG_LEVEL, format=LOG_FORMAT)
    window = PDFtoSpeech()
    window.show()
    sys.exit(app.exec())
