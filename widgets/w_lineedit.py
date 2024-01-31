from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtCore import QTimer
from widgets.w_font import font
from psutil import cpu_percent, cpu_count, virtual_memory, swap_memory
from threading import Lock


class LineEditUpdate(QLineEdit):
    def __init__(self, part, time, parent=None):
        super().__init__(parent)
        self.setReadOnly(True)
        self.time = time
        self.part = part
        self.setFont(font)
        self.start_updating()
        # palette = self.palette()
        self.lock = Lock()

    def start_updating(self):
        # Create a QTimer instance
        timer = QTimer(self)
        # Connect the timeout signal to the updateText method
        timer.timeout.connect(self.update_text)
        # Set the interval for the timer (in milliseconds)
        timer.start(self.time)  # Update every 1000 milliseconds (1 second)

    def update_text(self):
        with self.lock:
            if self.part == "cpu%":
                self.setText(str(cpu_percent()) + " %")

            if self.part == "cpu_core":
                self.setText(str(cpu_count(logical=False)) + " cores")

            if self.part == "cpu_lcore":
                self.setText(str(cpu_count()) + " logical processors")

            if self.part == "ram#":
                used = str(int(virtual_memory().used / 1024 / 1024))
                total = str(int(virtual_memory().total / 1024 / 1024))
                self.setText(used + " of " + total + " MB")

            if self.part == "ram%":
                self.setText(str(virtual_memory().percent) + " %")

            if self.part == "vram%":
                self.setText(str(swap_memory().percent) + " %")
            if self.part == "vram#":
                used = str(int(swap_memory().used / 1024 / 1024))
                total = str(int(swap_memory().total / 1024 / 1024))
                self.setText(used + " of " + total + " MB")
