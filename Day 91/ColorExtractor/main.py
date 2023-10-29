from itertools import islice
import logging
import sys

from PIL import Image
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap, QColor
from PyQt6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel, QMainWindow,
                             QPushButton, QFileDialog, QSpinBox, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)


WINDOW_WIDTH = 500
WINDOW_HEIGHT = 700
WINDOW_TITLE = "Image Color Analyzer"
WINDOW_ICON_PATH = 'icon.png'
QUANTIZE_VALUE = 64
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
DEFAULT_LOG_LEVEL = logging.INFO


class ImageAnalyzer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.image = None

        self.load_img_btn = None
        self.image_label = QLabel(self)
        self.num_colors_spinbox = QSpinBox(self)
        self.table_widget = QTableWidget(self)
        self.percentage_label = QLabel(self)
        self.analyse_btn = None

        self.init_ui()
        logging.info("ImageAnalyzer initialized.")

    def init_ui(self) -> None:
        """Sets up the user interface and layout of the main window."""
        # Set main window properties
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setWindowTitle(WINDOW_TITLE)
        self.setWindowIcon(QIcon(WINDOW_ICON_PATH))

        # Layout setup
        main_layout = QVBoxLayout()

        # Populate layout with widgets
        self.setup_load_button(main_layout)
        self.setup_image_display(main_layout)
        self.setup_color_input(main_layout)
        self.setup_table(main_layout)
        self.setup_run_button(main_layout)

        # Set layout to central widget
        central_widget = QWidget(self)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def setup_load_button(self, layout: QVBoxLayout) -> None:
        """Initializes the button for image loading and adds it to the layout."""
        self.load_img_btn = QPushButton('Load Image', self)
        self.load_img_btn.clicked.connect(self.load_image)
        layout.addWidget(self.load_img_btn)

    def setup_image_display(self, layout: QVBoxLayout) -> None:
        """Centers and adds the image display label to the layout."""
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.image_label)

    def setup_color_input(self, layout: QVBoxLayout) -> None:
        """Sets up a horizontal layout for selecting the number of colors to display."""
        h_layout = QHBoxLayout()
        h_layout.addStretch()
        label = QLabel("Number of colors to display:")
        h_layout.addWidget(label)
        self.num_colors_spinbox.setValue(10)
        h_layout.addWidget(self.num_colors_spinbox)
        h_layout.addStretch()
        layout.addLayout(h_layout)

    def setup_table(self, layout: QVBoxLayout) -> None:
        """Initializes the table to display color information and adds it to the layout."""
        self.table_widget.setColumnCount(4)
        header = self.table_widget.horizontalHeader()
        for index in range(self.table_widget.columnCount()):
            header.setSectionResizeMode(index, QHeaderView.ResizeMode.Stretch)
        self.table_widget.setHorizontalHeaderLabels(['Color', 'Color Code', 'Number of Pixels', 'Percentage'])
        layout.addWidget(self.table_widget)
        layout.addWidget(self.percentage_label)

    def setup_run_button(self, layout: QVBoxLayout) -> None:
        """Sets up the "Analyse" button and adds it to the layout."""
        self.analyse_btn = QPushButton('Analyse', self)
        self.analyse_btn.clicked.connect(lambda: self.analyze_image_pixels(self.num_colors_spinbox.value()))
        self.analyse_btn.setEnabled(False)
        layout.addWidget(self.analyse_btn)

    def load_image(self) -> None:
        """Opens a file dialog, loads the selected image, and displays it in the label."""
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.jpg);;All Files (*)")
        if file_name:
            self.image = Image.open(file_name)
            pixmap = QPixmap(file_name)
            self.image_label.setPixmap(pixmap.scaled(400, 400, Qt.AspectRatioMode.KeepAspectRatio,
                                                     Qt.TransformationMode.SmoothTransformation))
            self.analyse_btn.setEnabled(True)
            logging.info(f"Image loaded successfully from {file_name}.")
        else:
            logging.warning("No image loaded or selected path is empty.")

    @staticmethod
    def quantize_color(r: int, g: int, b: int, quantize_level: int = QUANTIZE_VALUE) -> tuple[int, int, int]:
        """Quantize a color by rounding its RGB values to the nearest multiple of quantize_level."""
        return ((r // quantize_level) * quantize_level,
                (g // quantize_level) * quantize_level,
                (b // quantize_level) * quantize_level)

    @staticmethod
    def rgb_to_hex(rgb: tuple[int, int, int]) -> str:
        """Convert an RGB tuple to a hex color string."""
        return "#{:02x}{:02x}{:02x}".format(*rgb)

    @staticmethod
    def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
        """Convert a hex color string to an RGB tuple."""
        hex_color = hex_color.lstrip('#')
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)

        return r, g, b

    def create_pixel_count_dict(self, number: int) -> (dict, int):
        """Converts the image to RGB, quantizes colors, and returns the top occurring colors and total pixel count."""
        logging.info("Creating pixel count dictionary.")
        img_rgb = self.image.convert('RGB')

        width, height = img_rgb.size
        pixel_count = width * height
        colors = img_rgb.getcolors(pixel_count)

        # Quantize the colors and convert them to hex
        color_dict = {}
        for count, (r, g, b) in colors:
            r, g, b = self.quantize_color(r, g, b)
            hex_code = self.rgb_to_hex((r, g, b))
            color_dict[hex_code] = color_dict.get(hex_code, 0) + count

        # Sort by occurrence
        sorted_items = dict(sorted(color_dict.items(), key=lambda i: i[1], reverse=True))
        items_to_display = list(islice(sorted_items.items(), number))

        return items_to_display, pixel_count

    def populate_table(self, sorted_items:  dict[str, int], pixel_count: int, number: int) -> None:
        """Populates the table widget with color information and calculates the color percentage representation."""
        logging.info("Populating table with sorted color data.")
        self.table_widget.clear()

        data = []
        for key, value in sorted_items:
            data.append(["", key, str(value), "{:.4f}".format(value / pixel_count * 100)])

        self.table_widget.setRowCount(number)
        for row, row_data in enumerate(data):
            for col, col_data in enumerate(row_data):
                item = QTableWidgetItem(col_data)
                self.table_widget.setItem(row, col, item)
            item = QTableWidgetItem()
            self.table_widget.setItem(row, 0, item)
            item.setBackground(QColor(*self.hex_to_rgb(data[row][1])))
        self.table_widget.setHorizontalHeaderLabels(['Color', 'Color Code', 'Number of Pixels', 'Percentage'])

        total = 0
        for item in data:
            total += float(item[3])
        self.percentage_label.setText(f"Percentage of total colour represented: {total:.4f}%")

    def analyze_image_pixels(self, number: int) -> None:
        """Orchestrates the process of analyzing image pixels and updating the table with color information."""
        logging.info("Starting image pixel analysis.")
        color_dict, pixel_count = self.create_pixel_count_dict(number)
        self.populate_table(color_dict, pixel_count, number)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    logging.basicConfig(level=DEFAULT_LOG_LEVEL, format=LOG_FORMAT)
    window = ImageAnalyzer()
    window.show()
    sys.exit(app.exec())
