from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *

from GUI import gui_scale
from GUI.StyleSheets import get_stylesheet

__author__ = "magnus"


class RibbonButton(QToolButton):
    def __init__(self, owner, action, is_large):
        QPushButton.__init__(self, owner)
        # sc = 1
        sc = gui_scale()
        self._actionOwner = action
        self.update_button_status_from_action()
        self.clicked.connect(self._actionOwner.trigger)
        self._actionOwner.changed.connect(self.update_button_status_from_action)

        if is_large:
            self.setMaximumWidth(int(80 * sc))
            self.setMinimumWidth(int(50 * sc))
            self.setMinimumHeight(int(75 * sc))
            self.setMaximumHeight(int(80 * sc))
            self.setStyleSheet(get_stylesheet("ribbonButton"))
            self.setToolButtonStyle(3)
            self.setIconSize(QSize(int(32 * sc), int(32 * sc)))
        else:
            self.setToolButtonStyle(2)
            self.setMaximumWidth(int(120 * sc))
            self.setIconSize(QSize(int(16 * sc), int(16 * sc)))
            self.setStyleSheet(get_stylesheet("ribbonSmallButton"))

    def update_button_status_from_action(self):
        self.setText(self._actionOwner.text())
        self.setStatusTip(self._actionOwner.statusTip())
        self.setToolTip(self._actionOwner.toolTip())
        self.setIcon(self._actionOwner.icon())
        self.setEnabled(self._actionOwner.isEnabled())
        self.setCheckable(self._actionOwner.isCheckable())
        self.setChecked(self._actionOwner.isChecked())
