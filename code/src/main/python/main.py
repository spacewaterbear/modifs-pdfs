import os
import sys
from functools import cached_property

from PySide6 import QtWidgets, QtGui

from package.main_window import MainWindow


def _resource(relative_path):
    # sys._MEIPASS is set by PyInstaller when running as a frozen executable
    if hasattr(sys, '_MEIPASS'):
        base = os.path.join(sys._MEIPASS, 'resources')
    else:
        base = os.path.join(os.path.dirname(__file__), '..', 'resources', 'base')
    return os.path.normpath(os.path.join(base, relative_path))


class AppContext:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)

    def get_resource(self, relative_path):
        return _resource(relative_path)

    def run(self):
        window = MainWindow(ctx=self)
        window.resize(1920 / 4, 1200 / 2)
        window.show()
        return self.app.exec()

    @cached_property
    def img_checked(self):
        return QtGui.QIcon(self.get_resource("images/checked.png"))

    @cached_property
    def img_unchecked(self):
        return QtGui.QIcon(self.get_resource("images/unchecked.png"))

    @cached_property
    def upload_pdf_icon(self):
        return QtGui.QIcon(self.get_resource("pdf-book.png"))


if __name__ == '__main__':
    appctxt = AppContext()
    sys.exit(appctxt.run())
