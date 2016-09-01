from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from GUI.RibbonButton import RibbonButton
from GUI.RibbonPane import RibbonPane


class RibbonTab(QWidget):
    def __init__(self, parent, name):
        QWidget.__init__(self, parent)
        layout = QHBoxLayout()
        self.setLayout(layout)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignLeft)



    def add_ribbon_pane(self, name):
        ribbon_pane = RibbonPane(self,name)
        self.layout().addWidget(ribbon_pane)
        return ribbon_pane

    def add_spacer(self):
        self.layout().addSpacerItem(QSpacerItem(1,1,QSizePolicy.MinimumExpanding))
        self.layout().setStretch(self.layout().count()-1,1)
        #
        # layout.addWidget(ActionButton(self, main_window._open_action, True), 0, Qt.AlignTop)
        # layout.addWidget(ActionButton(self, main_window._save_action, True), 0, Qt.AlignTop)
        # #layout.addWidget(ActionButton(self, main_window._save_as_action, True), 0, Qt.AlignTop)
        # layout.addWidget(ActionButton(self, main_window._save_to_excel_action, True), 0, Qt.AlignTop)
        #
        # layout.addWidget(RibbonPane(self, "File"))
        #
        # undo_layout = QVBoxLayout()
        # layout.addLayout(undo_layout, 0)
        # #undo_layout.addWidget(ActionButton(self, main_window._undo_action, False), 0, Qt.AlignTop)
        # #undo_layout.addWidget(ActionButton(self, main_window._redo_action, False), 0, Qt.AlignTop)
        #
        # analysis_layout = QHBoxLayout()
        # layout.addLayout(analysis_layout, 0)
        # #analysis_layout.addWidget(ActionButton(self, main_window._add_analysis_action, True), 0, Qt.AlignTop)
        # #analysis_layout.addWidget(ActionButton(self, main_window._add_calc_sheet_action, True), 0, Qt.AlignTop)
        # #analysis_layout.addWidget(ActionButton(self, main_window._add_geometry_action, True), 0, Qt.AlignTop)
        #
        # layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Fixed))
        # undo_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Fixed, QSizePolicy.Expanding))
