import sys
from PyQt5.QtWidgets import *
from GUI.MainWindow import MainWindow

__author__ = 'mamj'


def main():
    a = QApplication(sys.argv)
    a.setQuitOnLastWindowClosed(True)
    main_window = MainWindow()
    main_window.show()
    sys.exit(a.exec_())


main()
