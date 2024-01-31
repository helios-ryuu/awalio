from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

from widgets.w_font import font, font_bold_header


class DialogAbout(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowIcon(QIcon("logo.png"))
        self.setWindowTitle("About Awalio")
        self.setFixedSize(700, 400)
        self.layout = QVBoxLayout(self)
        self.central_widget = QWidget(self)
        self.central_layout = QVBoxLayout(self.central_widget)

        self.label_name = QLabel("Awalio")
        self.label_name.setFont(font_bold_header)
        self.label_name.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.label_content = QLabel("Version: Beta 0.2\tCopyright 2024 Helios\n\n"
                                    "> This program is developed with Python and PyQt6.\n\n"
                                    "> This program is an open-source project. Source code can be found at our Github "
                                    "repository: https://github.com/helios-ryuu/awalio\n\n"
                                    "> This program is free software: you can redistribute it and/or modify it "
                                    "under the terms of the GNU General Public License as published by the Free "
                                    "Software Foundation, either version 3 of the License, or (at your option) any "
                                    "later version. This program is distributed WITHOUT ANY WARRANTY; without "
                                    "even the implied warranty of MERCHANTABILITY or FITNESS FOR A "
                                    "PARTICULAR PURPOSE.\n\n"
                                    
                                    "> See the GNU General Public License for more details. You should have received "
                                    "a copy of the GNU General Public License along with this program. If not, "
                                    "see https://www.gnu.org/licenses/.")
        self.label_content.setFont(font)
        self.label_content.setWordWrap(True)
        self.label_content.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.label_content.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)  # Allow text selection

        self.central_layout.addWidget(self.label_name, stretch=0, alignment=Qt.AlignmentFlag.AlignTop)
        self.central_layout.addWidget(self.label_content, stretch=1, alignment=Qt.AlignmentFlag.AlignTop)

        self.layout.addWidget(self.central_widget)
        self.setLayout(self.layout)
