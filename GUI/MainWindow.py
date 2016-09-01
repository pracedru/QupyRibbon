from PyQt5.QtCore import *
from PyQt5.QtGui import QKeySequence
from GUI.RibbonButton import RibbonButton
from GUI.Icons import get_icon
from GUI.RibbonWidget import *
from GUI.StyleSheets import get_stylesheet

__author__ = 'mamj'


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.resize(1280, 800)
        self.setWindowTitle("Main Window")
        self.setDockNestingEnabled(True)
        self.setWindowIcon(get_icon("icon"))
        self._main_dock_widget = QDockWidget(self)
        self._main_dock_widget.setObjectName("MainDock");
        self._main_dock_widget.setWindowTitle("Main dock")
        self.addDockWidget(Qt.LeftDockWidgetArea, self._main_dock_widget)

        # -------------      actions       -----------------

        self._open_action = QAction(get_icon("open"), "Open\nFile...", self)
        self._open_action.setShortcuts(QKeySequence.Open)
        self._open_action.setStatusTip("Open file")
        self._open_action.triggered.connect(self.on_open_file)
        self._open_action.setIconVisibleInMenu(True)
        self.addAction(self._open_action)

        # _save_action
        self._save_action = QAction(get_icon("save"), "Save", self)
        self._save_action.setShortcuts(QKeySequence.Save)
        self._save_action.setStatusTip("Save these data")
        self._save_action.triggered.connect(self.on_save)
        self._save_action.setIconVisibleInMenu(True)
        self.addAction(self._save_action)

        self._copy_action = QAction(get_icon("copy"), "Copy", self)
        self._copy_action.setShortcuts(QKeySequence.Copy)
        self._copy_action.setStatusTip("Copy selection")
        self._copy_action.triggered.connect(self.on_copy)
        self._copy_action.setIconVisibleInMenu(True)
        self.addAction(self._copy_action)

        self._paste_action = QAction(get_icon("paste"), "Paste", self)
        self._paste_action.setShortcuts(QKeySequence.Copy)
        self._paste_action.setStatusTip("Paste from clipboard")
        self._paste_action.triggered.connect(self.on_paste)
        self._paste_action.setIconVisibleInMenu(True)
        self.addAction(self._paste_action)

        self._zoom_action = QAction(get_icon("zoom"), "Zoom", self)
        self._zoom_action.setStatusTip("Zoom in on document")
        self._zoom_action.triggered.connect(self.on_zoom)
        self._zoom_action.setIconVisibleInMenu(True)
        self.addAction(self._zoom_action)

        self._about_action = QAction(get_icon("about"), "About", self)
        self._about_action.setStatusTip("About QupyRibbon")
        self._about_action.triggered.connect(self.on_about)
        self._about_action.setIconVisibleInMenu(True)
        self.addAction(self._about_action)

        self._license_action = QAction(get_icon("license"), "License", self)
        self._license_action.setStatusTip("Licence for this software")
        self._license_action.triggered.connect(self.on_license)
        self._license_action.setIconVisibleInMenu(True)
        self.addAction(self._license_action)

        # Ribbon

        self._ribbon = QToolBar(self)
        self._ribbon.setStyleSheet(get_stylesheet("ribbon"))
        self._ribbon.setObjectName("ribbonWidget")
        self._ribbon.setWindowTitle("Ribbon")
        self.addToolBar(self._ribbon)
        self._ribbon.setMovable(False)
        self._ribbon_widget = RibbonWidget(self)
        self._ribbon.addWidget(self._ribbon_widget)
        self.init_ribbon()

    def init_ribbon(self):
        home_tab = self._ribbon_widget.add_ribbon_tab("Home")
        file_pane = home_tab.add_ribbon_pane("File")
        file_pane.add_ribbon_widget(RibbonButton(self, self._open_action, True))
        file_pane.add_ribbon_widget(RibbonButton(self, self._save_action, True))

        edit_panel = home_tab.add_ribbon_pane("Edit")
        edit_panel.add_ribbon_widget(RibbonButton(self, self._copy_action, True))
        edit_panel.add_ribbon_widget(RibbonButton(self, self._paste_action, True))
        grid = edit_panel.add_grid_widget(200)
        grid.addWidget(QLabel("Text box 1"), 1, 1)
        grid.addWidget(QLabel("Text box 2"), 2, 1)
        grid.addWidget(QLabel("Text box 3"), 3, 1)
        text_box1 = QLineEdit()
        text_box1.setText("Text 1")
        text_box1.textChanged.connect(self.on_text_box1_changed)
        text_box1.setStyleSheet("border: 1px solid rgba(0,0,0,30%);")
        grid.addWidget(text_box1, 2, 2)
        text_box2 = QLineEdit()
        text_box2.setText("Text 2")
        text_box2.textChanged.connect(self.on_text_box2_changed)
        text_box2.setStyleSheet("border: 1px solid rgba(0,0,0,30%);")
        grid.addWidget(text_box2, 1, 2)
        text_box3 = QLineEdit()
        text_box3.setText("Text 3")
        text_box3.textChanged.connect(self.on_text_box3_changed)
        text_box3.setStyleSheet("border: 1px solid rgba(0,0,0,30%);")
        grid.addWidget(text_box3, 3, 2)

        view_panel = home_tab.add_ribbon_pane("View")
        view_panel.add_ribbon_widget(RibbonButton(self, self._zoom_action, True))
        home_tab.add_spacer()

        about_tab = self._ribbon_widget.add_ribbon_tab("About")
        info_panel = about_tab.add_ribbon_pane("Info")
        info_panel.add_ribbon_widget(RibbonButton(self, self._about_action, True))
        info_panel.add_ribbon_widget(RibbonButton(self, self._license_action, True))

    def closeEvent(self, close_event):
        pass

    def on_open_file(self):
        pass

    def on_save_to_excel(self):
        pass

    def on_save(self):
        pass

    def on_text_box1_changed(self):
        pass

    def on_text_box2_changed(self):
        pass

    def on_text_box3_changed(self):
        pass

    def on_copy(self):
        pass

    def on_paste(self):
        pass

    def on_zoom(self):
        pass

    def on_about(self):
        text = "QupyRibbon\n"
        text += "This program was made by Magnus Jørgensen.\n"
        text += "Copyright © 2016 Magnus Jørgensen"
        QMessageBox().about(self, "About QupyRibbon", text)

    def on_license(self):
        file = open('LICENSE', 'r')
        lic = file.read()
        QMessageBox().information(self, "License", lic)
