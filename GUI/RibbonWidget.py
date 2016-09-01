from PyQt5.QtWidgets import *
from GUI.RibbonTab import RibbonTab
from GUI import gui_scale

__author__ = 'magnus'


class RibbonWidget(QTabWidget):
    def __init__(self, main_window):
        QWidget.__init__(self, main_window)
        self.setMaximumHeight(120*gui_scale())
        self.setMinimumHeight(110*gui_scale())

    def add_ribbon_tab(self, name):
        ribbon_tab = RibbonTab(self, name)
        self.addTab(ribbon_tab, name)
        return ribbon_tab
