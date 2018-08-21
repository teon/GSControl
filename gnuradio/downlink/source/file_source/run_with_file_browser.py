import os
import sys
from PyQt4 import QtGui
import file_source

class FilePathWrapper:
    def __init__(self, path):
        self.path_to_iq_file = str(path)


def file_browser():
    file_dialog = QtGui.QFileDialog()
    chosen_path = file_dialog.getOpenFileName(None, 'OpenFile')
    file_source.main(options=FilePathWrapper(chosen_path))

def application():
    app = QtGui.QApplication(sys.argv)
    file_browser()


if __name__ == "__main__":
    application()
