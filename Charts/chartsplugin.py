from PyQt5.QtQml import qmlRegisterType, QQmlExtensionPlugin

from piechart import PieChart
from pieslice import PieSlice


class ChartsPlugin(QQmlExtensionPlugin):

    def registerTypes(self, uri):
        qmlRegisterType(PieChart, "Charts", 1, 0, "PieChart")
        qmlRegisterType(PieSlice, "Charts", 1, 0, "PieSlice")
