import sys

from buttons import ButtonsGrid
from display import Display
from info import Info
from main_window import MainWindow
from paths import ICON_PATH, STYLE_PATH
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    icon = QIcon(str(ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    info = Info("Empty")
    window.addWidgetToVLayout(info)

    display = Display()
    window.addWidgetToVLayout(display)

    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    window.adjustFixedSize()
    window.show()

    with open(STYLE_PATH, "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())
