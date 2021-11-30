import os
import shutil
from PySide2.QtCore import QObject, Signal, QEvent
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFormLayout, QVBoxLayout, QTextEdit, \
    QProgressBar, QLineEdit, QFileDialog, QComboBox, QMessageBox
import sys


class TheFinderWin(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("The Finder By Ali Code")

        self.formLayout = QFormLayout()
        self.verticalLayout = QVBoxLayout()

        self.btnStart = QPushButton("Start")

        self.labelPath = QLabel("<b>Path: </b>")


        self.pathLine = QLineEdit()

        self.labelFileType = QLabel("<b>File Type:</b>")
        self.fileTypeComboBox = QComboBox()
        self.fileTypeComboBox.addItem("Text files")
        self.fileTypeComboBox.addItem("Audio files")
        self.fileTypeComboBox.addItem("Video files")
        self.fileTypeComboBox.addItem("Image files")
        self.fileTypeComboBox.addItem("MS Office files")
        self.fileTypeComboBox.addItem("PDF files")
        self.fileTypeComboBox.addItem("Outlook files")

        self.labelCopyTo = QLabel("<b>Copy To:</b>")
        self.copyLine = QLineEdit()

        self.result = QTextEdit()

        self.prgressBar = QProgressBar()
        self.prgressBar.setRange(0, 100)
        self.prgressBar.setValue(0)

        self.btnStart.clicked.connect(self.btnStartClicked)
        clickable(self.pathLine).connect(self.pathLineEditClicked)

        clickable(self.copyLine).connect(self.copyToFolder)

        self.formLayout.addRow(self.labelPath, self.pathLine)
        self.formLayout.addRow(self.labelFileType, self.fileTypeComboBox)
        self.formLayout.addRow(self.labelCopyTo, self.copyLine)

        self.verticalLayout.addLayout(self.formLayout)
        self.verticalLayout.addWidget(self.btnStart)

        self.verticalLayout.addWidget(self.result)
        self.verticalLayout.addWidget(self.prgressBar)
        self.setLayout(self.verticalLayout)

        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle("Message Box")
        self.msg.setText("The Operation finished !")

    def btnStartClicked(self):

        #### here Start Action######################################################################################################
        self.prgressBar.setValue(0)
        self.result.setText("Search for {" + self.fileTypeComboBox.currentText() + "} in Target Folder:  \n  " + self.pathLine.text())
        self.result.setText(self.result.toPlainText() + "\n" + "Copy To: \n " + self.copyLine.text() + "\n \n \n")
        directory = self.pathLine.text()
        copyToFolder = self.copyLine.text()
        i = 0
        totalFileType = 0

        if self.fileTypeComboBox.currentText() == "Text files":
            selectedFileType = ".txt"
            totalFileType = 1
        elif self.fileTypeComboBox.currentText() == "Audio files":
            selectedFileType = ".mp3"
            selectedFileType1 = ".aac"
            selectedFileType2 = ".m4a"
            selectedFileType3 = ".aax"
            selectedFileType4 = ".m4p"
            selectedFileType5 = ".ogg"
            totalFileType = 6
        elif self.fileTypeComboBox.currentText() == "Video files":
            selectedFileType = ".mp4"
            selectedFileType1 = ".avi"
            selectedFileType2 = ".mkv"
            selectedFileType3 = ".m4v"
            selectedFileType4 = ".mpg"
            selectedFileType5 = "wmv"
            selectedFileType6 = ".flv"
            selectedFileType7 = ".mov"
            selectedFileType8 = ".webm"
            selectedFileType9 = ".mts"
            totalFileType = 10
        elif self.fileTypeComboBox.currentText() == "Image files":
            selectedFileType = ".png"
            selectedFileType1 = ".jpg"
            selectedFileType2 = ".jpge"
            selectedFileType3 = ".bmp"
            selectedFileType4 = ".gif"
            selectedFileType5 = ".svg"
            totalFileType = 6

        elif self.fileTypeComboBox.currentText() == "MS Office files":
            selectedFileType = ".doc"
            selectedFileType1 = ".docx"
            selectedFileType2 = ".docm"
            selectedFileType3 = ".xls"
            selectedFileType4 = ".xlsx"
            selectedFileType5 = ".csv"
            selectedFileType6 = ".ppt"
            selectedFileType7 = ".pps"
            selectedFileType8 = ".pptx"
            selectedFileType9 = ".xps"
            totalFileType = 10

        elif self.fileTypeComboBox.currentText() == "PDF files":
            selectedFileType = ".pdf"
            totalFileType = 1

        elif self.fileTypeComboBox.currentText() == "Outlook files":
            selectedFileType = ".pst"
            selectedFileType1 = ".ost"
            selectedFileType2 = ".msg"
            totalFileType = 3



        if totalFileType == 1:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file.endswith(selectedFileType):
                        i = i + 1
                        shutil.copy2(os.path.join(root, file), copyToFolder, follow_symlinks=True)
                        self.result.setText(
                            self.result.toPlainText() + "\n " + str(i) + " - " + os.path.join(root, file))
                        self.prgressBar.setRange(0, i)
                        self.prgressBar.setValue(i)

        elif totalFileType == 3:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file.endswith(selectedFileType) or file.endswith(selectedFileType1) or file.endswith(selectedFileType2):
                        i = i + 1
                        shutil.copy2(os.path.join(root, file), copyToFolder, follow_symlinks=True)
                        self.result.setText(
                            self.result.toPlainText() + "\n " + str(i) + " - " + os.path.join(root, file))
                        self.prgressBar.setRange(0, i)
                        self.prgressBar.setValue(i)

        elif totalFileType == 6:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file.endswith(selectedFileType) or file.endswith(selectedFileType1) or file.endswith(selectedFileType2) or file.endswith(selectedFileType3) or file.endswith(selectedFileType4) or file.endswith(selectedFileType5):
                        i = i + 1
                        shutil.copy2(os.path.join(root, file), copyToFolder, follow_symlinks=True)
                        self.result.setText(
                            self.result.toPlainText() + "\n " + str(i) + " - " + os.path.join(root, file))
                        self.prgressBar.setRange(0, i)
                        self.prgressBar.setValue(i)

        elif totalFileType == 10:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file.endswith(selectedFileType) or file.endswith(selectedFileType1) or file.endswith(selectedFileType2) or file.endswith(selectedFileType3) or file.endswith(selectedFileType4) or file.endswith(selectedFileType5) or file.endswith(selectedFileType6) or file.endswith(selectedFileType7) or file.endswith(selectedFileType8) or file.endswith(selectedFileType9):
                        i = i + 1
                        shutil.copy2(os.path.join(root, file), copyToFolder, follow_symlinks=True)
                        self.result.setText(
                            self.result.toPlainText() + "\n " + str(i) + " - " + os.path.join(root, file))
                        self.prgressBar.setRange(0, i)
                        self.prgressBar.setValue(i)

        self.msg.exec_()




        #############################################################################################################################

    def pathLineEditClicked(self):
        openFileD = QFileDialog()
        openFileD.setFileMode(QFileDialog.DirectoryOnly)
        self.pathLine.setText(os.path.join(str(openFileD.getExistingDirectory())))


    def copyToFolder(self):
        openFileD = QFileDialog()
        openFileD.setFileMode(QFileDialog.DirectoryOnly)
        self.copyLine.setText(os.path.join(str(openFileD.getExistingDirectory())))



############################## function to make clickable widget
def clickable(widget):
    class Filter(QObject):
        clicked = Signal()

        def eventFilter(self, obj, event):
            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        return True
            return False

    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked


################################# end of function


if __name__ == "__main__":
    app = QApplication(sys.argv)
    theFinder = TheFinderWin()
    theFinder.show()
    sys.exit(app.exec_())
