from PyQt6.QtGui import QFont

main_font = "Trebuchet MS"

font = QFont(main_font)
font.setPointSize(12)

font_bold = QFont(main_font)
font.setPointSize(12)
font_bold.setBold(True)

font_header = QFont(main_font)
font_header.setPointSize(13)

font_bold_header = QFont(main_font)
font_bold_header.setBold(True)
font_bold_header.setPointSize(14)

font_bold_italic_title = QFont(main_font)
font_bold_italic_title.setBold(True)
font_bold_italic_title.setPointSize(14)
font_bold_italic_title.setItalic(True)
