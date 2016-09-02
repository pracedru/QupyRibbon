from PyQt5.QtWidgets import *
from GUI.RibbonTab import RibbonTab
from GUI import gui_scale
from GUI.StyleSheets import get_stylesheet

__author__ = 'magnus'


class RibbonWidget(QToolBar):
    def __init__(self, parent):
        QToolBar.__init__(self, parent)
        self.setStyleSheet(get_stylesheet("ribbon"))
        self.setObjectName("ribbonWidget")
        self.setWindowTitle("Ribbon")
        self._ribbon_widget = QTabWidget(self)
        self._ribbon_widget.setMaximumHeight(120*gui_scale())
        self._ribbon_widget.setMinimumHeight(110*gui_scale())
        self.setMovable(False)
        self.addWidget(self._ribbon_widget)

    def add_ribbon_tab(self, name):
        ribbon_tab = RibbonTab(self, name)
        self._ribbon_widget.addTab(ribbon_tab, name)
        return ribbon_tab
