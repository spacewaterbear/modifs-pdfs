import os
from time import sleep
from typing import List

from PySide2 import QtWidgets, QtCore, QtGui
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
from PySide2.QtWidgets import QMessageBox, QListWidgetItem
from pygame import mixer

def play_mp3(son):
    """
    son :  path du fichier audio
    joue le son
    """
    mixer.init()
    mixer.music.load(son)
    mixer.music.play()



class MainWindow(QtWidgets.QWidget):


    def __init__(self, ctx):
        super().__init__()
        self.ctx = ctx
        self.lw_items = None
        self.setWindowTitle("Fusion / Séparation de Pdfs")
        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        self.lbl_dropInfoSup = QtWidgets.QLabel("Déposer vos fichiers pdfs ci-dessous")
        self.lw_files = QtWidgets.QListWidget()
        self.lbl_dropInfo = QtWidgets.QLabel("^Déposer vos fichiers pdfs ci-dessus")
        self.lbl_fileName = QtWidgets.QLabel("Nom du nouveau fichier")
        self.le_fileName = QtWidgets.QLineEdit()
        self.btn_split = QtWidgets.QPushButton('Séparer un pdf')
        self.btn_merge = QtWidgets.QPushButton('Fusionner ces pdfs')

    def modify_widgets(self):
        css_file = self.ctx.get_resource('style.css')
        with open(css_file, "r") as f:
            self.setStyleSheet(f.read())
        self.lbl_dropInfoSup.setAlignment(QtCore.Qt.AlignHCenter)
        self.lbl_dropInfo.setAlignment(QtCore.Qt.AlignHCenter)
        self.lbl_dropInfo.setVisible(False)
        self.setAcceptDrops(True)
        self.lw_files.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.lw_files.setSortingEnabled(True)
        self.lw_files.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.lbl_fileName.setAlignment(QtCore.Qt.AlignHCenter)

    def create_layouts(self):
        self.main_layout = QtWidgets.QGridLayout(self)

    def add_widgets_to_layouts(self):
        self.main_layout.addWidget(self.lbl_dropInfoSup, 0, 0, 1, 2)
        self.main_layout.addWidget(self.lw_files, 1, 0, 1, 2)
        self.main_layout.addWidget(self.lbl_dropInfo, 2, 0, 1, 2)
        self.main_layout.addWidget(self.lbl_fileName, 3, 0, 1, 2)
        self.main_layout.addWidget(self.le_fileName, 4, 0, 1, 2)
        self.main_layout.addWidget(self.btn_split, 5, 0, 1, 1)
        self.main_layout.addWidget(self.btn_merge, 5, 1, 1,1)

    def setup_connections(self):
        QtWidgets.QShortcut(QtGui.QKeySequence("Backspace"), self.lw_files, self.delete_selected_items)
        self.btn_merge.clicked.connect(self.merging_pipeline)
        self.btn_split.clicked.connect(self.splitting_pipeline)


    def merging_pipeline(self):
        valid_input = self.merging_input_valid()
        if valid_input:
            succeed = self.pdf_merging()
            if succeed:
                self.display_succeed()

    def splitting_pipeline(self):
        valid_input = self.splitting_input_valid()
        if valid_input:
            succeed = self.pdf_splitting()
            if succeed:
                self.display_succeed()


    def merging_input_valid(self):
        if not self.lw_items:
            self.error_message_perso("Il n'y a aucun pdf à fusionner",
                                     "J'aime ma maman")
            return False

        if len(self.lw_items) == 1:
            self.error_message_perso("Impossible de fusionner un seul pdf, you stupid monkey",
                                     "Je vote pour le Front National")
            return False

        all_pdf = all([True if fileName.text().endswith(".pdf") else False for fileName in self.lw_items])
        if not all_pdf:
            self.error_message_perso(
                "Au moins un des fichiers ne se termine pas par .pdf, est-ce que tu me prendrais pas pour un con ? ",
                "ٱللَّٰهُ أَكْبَرُ")
            return False
        return True

    def splitting_input_valid(self):
        if not self.lw_items:
            self.error_message_perso("Il n'y a aucun pdf à séparer",
                                     "J'aime mon papa")
            return False

        if len(self.lw_items) > 1:
            self.error_message_perso("Un seul pdf à séparer à la fois, you moron",
                                     "J'aime le saucisson de cheval")
            return False

        if len(self.lw_items) == 1:
            filename = self.le_fileName.text()
            if not filename.endswith('.pdf'):
                self.error_message_perso(
                    "Ce fichier ne se termine pas par .pdf, est-ce que tu me prendrais pas pour un con ? ",
                    "Je crois en Dieu")
                return False
        return True


    def pdf_merging(self):
        merger = PdfFileMerger()
        for pdf in self.lw_items:
            try:
                merger.append(pdf.text())
            except:
                self.error_message_perso(
                    f"Impossible de lire le fichier \"{os.path.basename(pdf.text())}\"",
                    "Encore un fichier pdf corrompu, comme certains politiciens...")
                return False
        self.file_name = self.le_fileName.text().replace(".pdf", "")
        merger.write(os.path.join(self.first_file_path, f"{self.file_name}_fusionné.pdf"))
        merger.close()
        return True


    def pdf_splitting(self):
        path = self.lw_items[0].text()
        with open(path, "rb") as f:
            try:
                inputpdf = PdfFileReader(f, "rb")
            except:
                self.error_message_perso(f"Impossible de lire le fichier \"{self.full_name}\"",
                                         "Encore un fichier pdf corrompu, comme certains politiciens...")
                return False
            if inputpdf.numPages == 1:
                self.error_message_perso("Il n'y a qu'une seule page dans ton pdf", "愛ُしている")
                return False
            self.file_name = self.le_fileName.text().replace(".pdf", "")
            for i in range(inputpdf.numPages):
                output = PdfFileWriter()
                output.addPage(inputpdf.getPage(i))
                with open(os.path.join(self.first_file_path, f"{self.file_name}_{i + 1}.pdf"),
                          "wb") as outputStream:
                    output.write(outputStream)
        return True


    def display_succeed(self):
        for lw_item in self.lw_items:
            lw_item.setIcon(self.ctx.img_checked)
        play_mp3(self.ctx.get_resource('sons/tt.mp3'))
        sleep(1)
        self.lw_files.clear()
        self.le_fileName.clear()
        self.lw_items = []

    def delete_selected_items(self):
        for lw_item in self.lw_files.selectedItems():
            row = self.lw_files.row(lw_item)
            self.lw_files.takeItem(row)
        self.lw_items = [self.lw_files.item(index) for index in range(self.lw_files.count())]
        self.le_fileName.clear()


    def dragEnterEvent(self, event):
        self.lbl_dropInfo.setVisible(True)
        event.accept()

    def dragLeaveEvent(self, event):
        self.lbl_dropInfo.setVisible(False)

    def dropEvent(self, event):
        event.accept()
        for url in event.mimeData().urls():
            self.add_file(path=url.toLocalFile())

    def add_file(self, path):
        items = [self.lw_files.item(index).text() for index in range(self.lw_files.count())]
        self.lbl_dropInfo.setVisible(False)
        self.le_fileName.setText(os.path.basename(path)) #set the field name with the name of the first file
        self.file_name = self.le_fileName.text().replace(".pdf", "")
        self.first_file_path = os.path.dirname(path)
        if path not in items:
            lw_item = QtWidgets.QListWidgetItem(path)
            lw_item.setIcon(self.ctx.img_checked)
            lw_item.processed = False
            self.lw_files.addItem(lw_item)
        self.lw_items = [self.lw_files.item(index) for index in range(self.lw_files.count())]

    def error_message_perso(self, information_text, ok_text):
        msgbox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, "",
                                       information_text)
        msgbox.addButton(self.tr(ok_text), QMessageBox.ActionRole)
        msgbox.exec_()

