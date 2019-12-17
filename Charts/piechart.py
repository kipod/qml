from PyQt5.QtCore import pyqtProperty
from PyQt5.QtQml import QQmlListProperty
from PyQt5.QtQuick import QQuickItem

from pieslice import PieSlice


class PieChart(QQuickItem):

    @pyqtProperty(QQmlListProperty)
    def slices(self):
        return QQmlListProperty(PieSlice, self,
                append=lambda pie_ch, pie_sl: pie_sl.setParentItem(pie_ch))

    @pyqtProperty(str)
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def __init__(self, parent=None):
        super(PieChart, self).__init__(parent)

        self._name = ''
