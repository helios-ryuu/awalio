from PyQt6.QtGui import QPalette
from widgets.w_color import *


def set_theme(app, theme):
    if theme == "light":
        palette = app.palette()
        palette.setColor(QPalette.ColorRole.Window, light)
        palette.setColor(QPalette.ColorRole.Button, light)
        palette.setColor(QPalette.ColorRole.Base, base_light)
        palette.setColor(QPalette.ColorRole.Highlight, highlight_light)
        palette.setColor(QPalette.ColorRole.Text, black)
        palette.setColor(QPalette.ColorRole.ButtonText, black)
        palette.setColor(QPalette.ColorRole.WindowText, black)
        palette.setColor(QPalette.ColorRole.HighlightedText, black)
        app.setPalette(palette)
    elif theme == "dark":
        palette = app.palette()
        palette.setColor(QPalette.ColorRole.Window, dark)
        palette.setColor(QPalette.ColorRole.Button, dark)
        palette.setColor(QPalette.ColorRole.Base, base_dark)
        palette.setColor(QPalette.ColorRole.Highlight, highlight_dark)
        palette.setColor(QPalette.ColorRole.Text, dark_text_color)
        palette.setColor(QPalette.ColorRole.ButtonText, dark_text_color)
        palette.setColor(QPalette.ColorRole.WindowText, dark_text_color)
        palette.setColor(QPalette.ColorRole.HighlightedText, dark_text_color)
        app.setPalette(palette)