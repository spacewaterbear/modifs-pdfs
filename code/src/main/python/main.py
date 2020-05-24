from fbs_runtime.application_context.PySide2 import ApplicationContext, cached_property
from PySide2 import QtGui
import sys

from package.main_window import MainWindow

class AppContext(ApplicationContext):
    def run(self):
        window = MainWindow(ctx=self)
        window.resize(1920 / 4, 1200 / 2)
        window.show()
        return self.app.exec_()

    @cached_property #permet de mettre ce que retourne la fonction dans le cache
    def img_checked(self):
        return QtGui.QIcon(self.get_resource("images/checked.png"))

    @cached_property #permet de mettre ce que retourne la fonction dans le cache
    def img_unchecked(self):
        return QtGui.QIcon(self.get_resource("images/unchecked.png"))

    @cached_property  # permet de mettre ce que retourne la fonction dans le cache
    def upload_pdf_icon(self):
        return QtGui.QIcon(self.get_resource("pdf-book.png"))

if __name__ == '__main__':
    appctxt = AppContext()       # 1. Instantiate ApplicationContext
    appctxt.run()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)