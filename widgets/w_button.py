from PyQt6.QtWidgets import QPushButton, QWidget, QLabel, QScrollArea, QVBoxLayout, QTextEdit
from PyQt6.QtGui import QPalette
from PyQt6.QtCore import Qt

from widgets.w_font import font, font_bold, font_header, font_bold_header
from widgets.w_color import *
from widgets.w_lineedit import LineEditUpdate
from widgets.w_dialog import DialogAbout
from widgets.w_app import set_theme
from widgets.s_feature import clear_referenced_display, add_spacer_display


class ButtonDarkMode(QPushButton):
    def __init__(self, text, app, parent=None):
        super().__init__(parent)
        self.app = app
        self.setText(text)
        self.clicked.connect(self.on_click)
        self.setFont(font)
        self.state = "Light"

    def on_click(self):
        if self.state == "Light":
            self.setText("Light mode")
            self.state = "Dark"
            set_theme(self.app, "dark")
        else:
            self.setText("Dark mode")
            self.state = "Light"
            set_theme(self.app, "light")


class ButtonMonitoring(QPushButton):
    def __init__(self, text: str, display, parent=None):
        super().__init__(parent)
        self.display = display
        self.setText(text)
        self.clicked.connect(self.on_click)
        self.setFont(font)

    def on_click(self):
        clear_referenced_display(self)

        title_monitoring = QLabel("     [Monitor view]")
        title_monitoring.setFont(font_bold)

        label_cpu = QLabel("CPU")
        label_cpu.setFont(font_bold_header)
        label_cpu_percent = QLabel("CPU usage (%)")
        label_cpu_percent.setFont(font_bold)
        label_cpu_core = QLabel("CPU physical cores")
        label_cpu_core.setFont(font_bold)
        label_cpu_lcore = QLabel("CPU logical processors")
        label_cpu_lcore.setFont(font_bold)

        label_ram = QLabel("RAM")
        label_ram.setFont(font_bold_header)
        label_ram_usage = QLabel("RAM usage (MB)")
        label_ram_usage.setFont(font_bold)
        label_ram_percent = QLabel("RAM usage (%)")
        label_ram_percent.setFont(font_bold)

        label_vram = QLabel("Virtual Ram")
        label_vram.setFont(font_bold_header)
        label_vram_usage = QLabel("Virtual RAM usage (MB)")
        label_vram_usage.setFont(font_bold)
        label_vram_percent = QLabel("Virtual RAM usage (%)")
        label_vram_percent.setFont(font_bold)

        lineedit_update_cpu_percent = LineEditUpdate("cpu%", 1000)
        lineedit_update_cpu_core = LineEditUpdate("cpu_core", 1000)
        lineedit_update_cpu_lcore = LineEditUpdate("cpu_lcore", 1000)
        lineedit_update_ram_usage = LineEditUpdate("ram#", 1000)
        lineedit_update_ram_percent = LineEditUpdate("ram%", 1000)
        lineedit_update_vram_usage = LineEditUpdate("vram#", 1000)
        lineedit_update_vram_percent = LineEditUpdate("vram%", 1000)

        vertical_layout = QVBoxLayout()
        vertical_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        vertical_layout.addWidget(label_cpu)
        vertical_layout.addWidget(label_cpu_percent)
        vertical_layout.addWidget(lineedit_update_cpu_percent)
        vertical_layout.addWidget(label_cpu_core)
        vertical_layout.addWidget(lineedit_update_cpu_core)
        vertical_layout.addWidget(label_cpu_lcore)
        vertical_layout.addWidget(lineedit_update_cpu_lcore)

        add_spacer_display(vertical_layout)

        vertical_layout.addWidget(label_ram)
        vertical_layout.addWidget(label_ram_usage)
        vertical_layout.addWidget(lineedit_update_ram_usage)
        vertical_layout.addWidget(label_ram_percent)
        vertical_layout.addWidget(lineedit_update_ram_percent)

        add_spacer_display(vertical_layout)

        vertical_layout.addWidget(label_vram)
        vertical_layout.addWidget(label_vram_usage)
        vertical_layout.addWidget(lineedit_update_vram_usage)
        vertical_layout.addWidget(label_vram_percent)
        vertical_layout.addWidget(lineedit_update_vram_percent)

        vertical_view = QWidget()
        vertical_view.setLayout(vertical_layout)
        scroll_view = QScrollArea()
        scroll_view.setWidget(vertical_view)
        scroll_view.setWidgetResizable(True)
        scroll_view.setMinimumWidth(650)

        self.display.addWidget(title_monitoring)
        self.display.addWidget(scroll_view)


class ButtonSystemInfo(QPushButton):
    def __init__(self, text, display, parent=None):
        super().__init__(parent)
        self.display = display
        self.setText(text)
        self.clicked.connect(self.on_click)
        self.setFont(font)

    def on_click(self):
        clear_referenced_display(self)
        system_info_text = ""
        try:
            with open("./system.txt", "r") as file:
                lines = file.readlines()
            lines.pop(0)
            for i in lines:
                system_info_text += i
        except Exception as e:
            print(e)

        system_title = QLabel("[Information obtained by systeminfo command]")
        system_title.setFont(font_bold)

        system_info_textedit = QTextEdit()
        system_info_textedit.setFont(font_header)
        system_info_textedit.setText(system_info_text)
        system_info_textedit.setReadOnly(True)
        system_info_textedit.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        scroll_view = QScrollArea()
        scroll_view.setWidget(system_info_textedit)
        scroll_view.setWidgetResizable(True)
        scroll_view.setMinimumWidth(650)

        self.display.addWidget(system_title)
        self.display.addWidget(scroll_view)


class ButtonAbout(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setText(text)
        self.clicked.connect(self.on_click)
        self.setFont(font)

    def on_click(self):
        about = DialogAbout(self)
        about.exec()
