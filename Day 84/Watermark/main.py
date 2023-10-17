import logging
import random
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon, QImage, QPixmap
from PyQt6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow, QPushButton, QSlider, QVBoxLayout, QWidget,
                             QFileDialog, QLineEdit)

from PIL import Image, ImageDraw, ImageFont

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 200
WINDOW_TITLE = "WaterMarker"
WINDOW_ICON_PATH = 'icon.png'
DEFAULT_OPACITY = 128
DEFAULT_FONT_SIZE = 40
DEFAULT_SPACING = 10
LOAD_IMAGE_TEXT = "Load Image"
PLACEHOLDER_TEXT = "Enter your watermark text here"
WATERMARK_REPETITIONS = 30
WATERMARK_FONT_PATH = "arial.ttf"
SAVE_IMAGE_TEXT = "Save Watermarked Image"
PNG_FILES_FILTER = "PNG Files (*.png)"
IMAGE_PREVIEW_TEXT = "Image Preview"
OPACITY_LABEL_TEXT = "Opacity:"
FONT_SIZE_LABEL_TEXT = "Font Size:"
SPACING_LABEL_TEXT = "Spacing:"
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
DEFAULT_LOG_LEVEL = logging.INFO


class WatermarkWindow(QMainWindow):
    """Main window class for the Watermarking application."""

    def __init__(self) -> None:
        """Initialize the WatermarkWindow."""

        super().__init__()
        self.setGeometry(200, 200, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setWindowTitle(WINDOW_TITLE)
        self.setWindowIcon(QIcon(WINDOW_ICON_PATH))

        self.label_preview = None
        self.label_image = None
        self.btn_load = None
        self.watermark_input = None
        self.opacity_slider = None
        self.opacity = DEFAULT_OPACITY
        self.fontSize_slider = None
        self.font_size = DEFAULT_FONT_SIZE
        self.spacing_slider = None
        self.spacing = DEFAULT_SPACING
        self.btnWatermark = None

        self.pixmap = None
        self.image_path = None

        logging.info("Initializing WatermarkWindow...")
        self.initUI()

    def initUI(self) -> None:
        """Initialize the user interface."""

        # Initialize main layout
        layout = QVBoxLayout()

        # Setup Image Preview
        self.setupImagePreview(layout)

        # Setup Button for loading images
        self.setupLoadImageButton(layout)

        # Setup watermark input field
        self.setupWatermarkInput(layout)

        # Setup Sliders for adjusting watermark properties
        self.setupSliders(layout)

        # Setup watermark button
        self.setupWatermarkButton(layout)

        # Set central widget
        centralWidget = QWidget(self)
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
        self.setWindowTitle('Watermark App')
        self.show()

    def setupImagePreview(self, layout: QVBoxLayout) -> None:
        """Set up the image preview components."""
        self.label_preview = QLabel(IMAGE_PREVIEW_TEXT)
        self.configureLabel(self.label_preview, 18, True, Qt.AlignmentFlag.AlignCenter, False)
        self.label_image = QLabel(self)
        self.label_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label_preview)
        layout.addWidget(self.label_image)

    def setupLoadImageButton(self, layout: QVBoxLayout) -> None:
        """Set up the load image button."""
        self.btn_load = self.createButton(LOAD_IMAGE_TEXT, layout, self.loadImage)

    def setupWatermarkInput(self, layout: QVBoxLayout) -> None:
        """Set up the watermark input field."""
        self.watermark_input = QLineEdit(self)
        self.watermark_input.setPlaceholderText(PLACEHOLDER_TEXT)
        self.watermark_input.textChanged.connect(lambda: self.updatePreview(self.addWatermark()))
        self.watermark_input.setEnabled(False)
        layout.addWidget(self.watermark_input)

    def setupSliders(self, layout: QVBoxLayout) -> None:
        """Set up sliders for watermark properties."""
        self.opacity_slider = self.createSlider(Qt.Orientation.Horizontal, 0, 255, 128, layout, OPACITY_LABEL_TEXT)
        self.fontSize_slider = self.createSlider(Qt.Orientation.Horizontal, 20, 50, 40, layout, FONT_SIZE_LABEL_TEXT)
        self.spacing_slider = self.createSlider(Qt.Orientation.Horizontal, 0, 50, 10, layout, SPACING_LABEL_TEXT)

    def setupWatermarkButton(self, layout: QVBoxLayout) -> None:
        """Set up the watermark button."""
        self.btnWatermark = QPushButton('Save Image', self)
        self.btnWatermark.clicked.connect(lambda: self.saveWatermarkedImage(self.addWatermark()))
        self.btnWatermark.setEnabled(False)
        layout.addWidget(self.btnWatermark)

    @staticmethod
    def configureLabel(label: QLabel, font_size: int, is_bold: bool, alignment: Qt.AlignmentFlag, visibility: bool) \
            -> None:
        """Configure a QLabel widget."""
        font = QFont()
        font.setPointSize(font_size)
        font.setBold(is_bold)
        label.setFont(font)
        label.setAlignment(alignment)
        label.setVisible(visibility)

    def createButton(self, text: str, layout: QVBoxLayout, function: callable, visibility: bool = True) -> QPushButton:
        """Create a QPushButton widget."""
        btn = QPushButton(text, self)
        btn.clicked.connect(function)
        btn.setEnabled(visibility)
        layout.addWidget(btn)
        return btn

    def createSlider(self, orientation: Qt.Orientation, min_val: int, max_val: int, default_val: int,
                     layout: QVBoxLayout, label_text: str) -> QSlider:
        """Helper function to create and return a slider."""
        # Create the slider
        slider = QSlider(orientation, self)
        slider.setMinimum(min_val)
        slider.setMaximum(max_val)
        slider.setValue(default_val)
        slider.valueChanged.connect(self.updateWatermarkProperties)
        slider.valueChanged.connect(lambda: self.updatePreview(self.addWatermark()))
        slider.setVisible(False)

        # Create the label for the slider
        label = QLabel(label_text)

        # Create a horizontal layout to hold the label and the slider
        sliderLayout = QHBoxLayout()
        sliderLayout.addWidget(label)
        sliderLayout.addWidget(slider)
        layout.addLayout(sliderLayout)

        return slider

    def loadImage(self) -> None:
        """Load an image using QFileDialog and update UI accordingly."""
        f_name, _ = QFileDialog.getOpenFileName(self, 'Open Image', '', 'Image files (*.jpg *.jpeg *.png)')
        if f_name:
            self.pixmap = QPixmap(f_name)
            self.label_image.setPixmap(self.pixmap.scaled(400, 400))
            self.image_path = f_name
            self.activateWatermarkControls()
            logging.info(f"Image loaded from path: {f_name}")

    def activateWatermarkControls(self) -> None:
        """Activate watermark related controls."""
        self.label_preview.setVisible(True)
        self.watermark_input.setEnabled(True)
        self.btnWatermark.setEnabled(True)
        self.opacity_slider.setVisible(True)
        self.fontSize_slider.setVisible(True)
        self.spacing_slider.setVisible(True)
        logging.info("Watermark controls activated.")

    def updateWatermarkProperties(self) -> None:
        """Update watermark properties based on slider values."""
        self.opacity = self.opacity_slider.value()
        self.font_size = self.fontSize_slider.value()
        self.spacing = self.spacing_slider.value()
        logging.info(
            f"Watermark properties updated: Opacity={self.opacity}, Font Size={self.font_size}, Spacing={self.spacing}")

    def addWatermark(self) -> Image:
        """Add watermark to the loaded image."""
        image = Image.open(self.image_path)
        custom_text = self.watermark_input.text() or ''

        watermark_text = self.generateWatermarkText(custom_text)
        text_image = self.createTextImage(custom_text, watermark_text, image.size)
        rotated_text_image = self.rotateAndCropTextImage(text_image, image.size)

        logging.info(f"Added watermark: {custom_text}")
        return Image.alpha_composite(image.convert('RGBA'), rotated_text_image)

    @staticmethod
    def generateWatermarkText(custom_text: str) -> str:
        """Generate the watermark text."""
        space = 2 * ' '
        return space.join([custom_text] * WATERMARK_REPETITIONS)

    def createTextImage(self, custom_text: str, watermark_text: str, image_size: tuple) -> Image:
        """Create an image with the watermark text."""
        width, height = image_size

        diagonal_length = int((width ** 2 + height ** 2) ** 0.5)
        text_image = Image.new('RGBA', (diagonal_length, diagonal_length), (255, 255, 255, 0))

        try:
            font = ImageFont.truetype(WATERMARK_FONT_PATH, self.font_size)
        except IOError:
            font = ImageFont.load_default()

        draw = ImageDraw.Draw(text_image)
        t_height = font.getbbox('A')[3] - font.getbbox('A')[1]
        position = (0, 0)

        for _ in range(0, int(diagonal_length / t_height)):
            draw.text((position[0], position[1]), watermark_text[random.randint(0, len(custom_text)):],
                      fill=(255, 255, 255, self.opacity), font=font)  # Use the opacity slider value
            position = (position[0], position[1] + t_height + self.spacing)  # Use the spacing slider value

        return text_image

    @staticmethod
    def rotateAndCropTextImage(text_image: Image, image_size: tuple) -> Image:
        """Rotate the watermark text image and crop to match original image size."""
        width, height = image_size

        rotated_text_image = text_image.rotate(45, expand=True)
        x_offset = (rotated_text_image.width - width) // 2
        y_offset = (rotated_text_image.height - height) // 2

        return rotated_text_image.crop((x_offset, y_offset, x_offset + width, y_offset + height))

    def updatePreview(self, watermarked: Image) -> None:
        """Update the image preview with the watermarked image."""
        # Convert PIL image to QImage
        mode = watermarked.mode
        if mode == 'RGBA':
            data = watermarked.tobytes('raw', 'BGRA')
            image_format = QImage.Format.Format_ARGB32
        elif mode == 'RGB':
            data = watermarked.tobytes('raw', 'BGR')
            image_format = QImage.Format.Format_RGB888
        else:
            raise ValueError("Unsupported image mode!")

        image = QImage(data, watermarked.width, watermarked.height, image_format)
        pixmap = QPixmap.fromImage(image)
        self.label_image.setPixmap(pixmap)

    def saveWatermarkedImage(self, watermarked: Image) -> None:
        """Save the watermarked image to a user-selected path."""
        f_name, _ = QFileDialog.getSaveFileName(self, SAVE_IMAGE_TEXT, "", PNG_FILES_FILTER)
        if f_name:
            watermarked.save(f_name)
            logging.info(f"Watermarked image saved to: {f_name}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    logging.basicConfig(level=DEFAULT_LOG_LEVEL, format=LOG_FORMAT)
    main_window = WatermarkWindow()
    main_window.show()
    app.exec()
