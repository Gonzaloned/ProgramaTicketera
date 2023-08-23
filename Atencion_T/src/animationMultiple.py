from PySide6.QtCore import *
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import *

class RowFadeController(QObject):
    def __init__(self, parent, buttons):
        super().__init__()
        self.buttons = buttons
        self.effects = []
        for button in buttons:
            effect = QGraphicsOpacityEffect(button, opacity=1.0)
            button.setGraphicsEffect(effect)
            self.effects.append(effect)

        self.animation = QVariantAnimation(self)
        self.animation.setStartValue(1.)
        self.animation.setEndValue(0.)
        self.animation.valueChanged.connect(self.setOpacity)

    def toggle(self, hide):
        self.animation.setDirection(
            self.animation.Forward if hide else self.animation.Backward
        )
        self.animation.start()

    def setOpacity(self, opacity):
        for effect in self.effects:
            effect.setOpacity(opacity)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout(self)
        self.fadeControllers = []
        for row in range(10):
            rowButtons = []
            for col in range(10):
                button = QPushButton(str(col + 1))
                layout.addWidget(button, row, col)
                rowButtons.append(button)

            toggleButton = QPushButton('toggle', checkable=True)
            layout.addWidget(toggleButton, row, layout.columnCount() - 1)

            fadeController = RowFadeController(self, rowButtons)
            self.fadeControllers.append(fadeController)
            toggleButton.clicked.connect(fadeController.toggle)

app = QApplication([])
test = Window()
test.show()
app.exec()