from PyQt5.QtCore import pyqtProperty, QRectF
from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5.QtQuick import QQuickPaintedItem


class PieSlice(QQuickPaintedItem):

    @pyqtProperty(QColor)
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = QColor(color)

    @pyqtProperty(int)
    def fromAngle(self):
        return self._fromAngle

    @fromAngle.setter
    def fromAngle(self, fromAngle):
        self._fromAngle = fromAngle

    @pyqtProperty(int)
    def angleSpan(self):
        return self._angleSpan

    @angleSpan.setter
    def angleSpan(self, angleSpan):
        self._angleSpan = angleSpan

    def __init__(self, parent=None):
        super(PieSlice, self).__init__(parent)

        self._color = QColor()
        self._fromAngle = 0
        self._angleSpan = 0

    def paint(self, painter):
        painter.setPen(QPen(self._color, 2))
        painter.setRenderHints(QPainter.Antialiasing, True)

        rect = QRectF(0, 0, self.width(), self.height()).adjusted(1, 1, -1, -1)
        painter.drawPie(rect, self._fromAngle * 16, self._angleSpan * 16)
