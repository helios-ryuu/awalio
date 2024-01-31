from PyQt6.QtWidgets import QLabel
from widgets.w_font import font_bold_header


def clear_referenced_display(obj):
    for i in reversed(range(obj.display.count())):
        widget = obj.display.itemAt(i).widget()
        if widget is not None:
            obj.display.removeWidget(widget)
            widget.setParent(None)


def add_spacer_display(layout):
    label = QLabel("_" * 80)
    label.setFont(font_bold_header)
    layout.addWidget(label)
