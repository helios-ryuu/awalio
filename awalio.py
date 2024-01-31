from subprocess import PIPE, run
from time import time
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QIcon, QPalette
from PyQt6.QtCore import Qt
from widgets.w_button import ButtonDarkMode, ButtonSystemInfo, ButtonMonitoring, ButtonAbout
from widgets.w_font import font_bold, font_bold_italic_title
from widgets.w_color import *
from widgets.w_app import set_theme


class MainScreen(QMainWindow):
    def __init__(self, _app):
        super().__init__()

        # Window setting
        self.primary_screen = QApplication.screens()[0]
        screen = self.primary_screen.availableGeometry().size()
        multiplier = 4 / 5
        self.position_x = int(screen.width() * (1 - multiplier) / 2)
        self.position_y = int(screen.height() * (1 - multiplier) / 2)
        self.size_x = int(screen.width() * multiplier)
        self.size_y = int(screen.height() * multiplier)

        self.setGeometry(self.position_x, self.position_y, self.size_x, self.size_y)
        self.setWindowTitle("Awalio")
        self.setWindowIcon(QIcon("logo.png"))

        #menu = self.menuBar()
        #self.file_menu = menu.addMenu("&File")

        # Level 1: Central widget (Parent: MainScreen)
        self.central_widget = QWidget(self)
        self.layout = QVBoxLayout(self.central_widget)

        # Level 2.1: Title widget (Parent: central_widget)
        self.title_widget = QWidget(self.central_widget)
        self.title_layout = QHBoxLayout(self.title_widget)

        # Level 2.2: Data widget (Parent: central_widget)
        self.data_widget = QWidget(self.central_widget)
        self.data_layout = QGridLayout(self.data_widget)

        # Level 2.2.1: Utility widget (Parent: data_widget)
        self.utility_widget = QWidget(self.data_widget)
        self.utility_layout = QVBoxLayout(self.utility_widget)
        self.utility_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Level 2.2.2: Display widget (Parent: data_widget)
        self.display_widget = QWidget(self.data_widget)
        self.display_layout = QVBoxLayout(self.display_widget)

        # Initial components
        self.title_bar = QLabel("Awalio version Beta 0.1")
        self.title_bar.setFont(font_bold_italic_title)
        self.title_utility = QLabel("     [Features]\n")
        self.title_utility.setFont(font_bold)

        self.button_dark_mode = ButtonDarkMode("Dark mode", _app, self.utility_widget)
        self.button_monitoring = ButtonMonitoring("Monitoring", self.display_layout)
        self.button_system_info = ButtonSystemInfo("System Information", self.display_layout)
        self.button_about = ButtonAbout("About")

        # Layout
        self.layout.addWidget(self.title_widget, stretch=0)
        self.layout.addWidget(self.data_widget, stretch=1)
        self.title_layout.addWidget(self.title_bar)
        self.data_layout.addWidget(self.utility_widget, 0, 0)
        self.data_layout.addWidget(self.display_widget, 0, 1, 1, 4)
        self.utility_layout.addWidget(self.title_utility)
        self.utility_layout.addWidget(self.button_monitoring)
        self.utility_layout.addWidget(self.button_system_info)
        self.utility_layout.addWidget(self.button_dark_mode)
        self.utility_layout.addWidget(self.button_about)

        self.setCentralWidget(self.central_widget)

        try:
            with open("system.txt", "r") as file1:
                pass
            with open("time.txt", "r") as file3:
                times = file3.readline()
                if float(time()) - float(times) >= 600000.0:
                    raise Exception

        except Exception as e:
            with open("time.txt", "w") as file3:
                file3.writelines(str(time()))
                # Run the command and capture its output
            result = run(
                ['systeminfo'],
                stdout=PIPE, stderr=PIPE, text=True)

            # Check if the command was successful (return code 0)
            if result.returncode == 0:
                print("Command executed successfully.")
                # Access the output using result.stdout
                with open("system.txt", "w") as file3:
                    file3.writelines(result.stdout)
            else:
                print("Command failed.")
                # Access the error output using result.stderr
                print("Error:\n", result.stderr)
            print(e)


if __name__ == "__main__":
    app = QApplication([])
    app.setStyle("Fusion")
    set_theme(app, "light")
    window = MainScreen(app)
    window.show()
    app.exec()
