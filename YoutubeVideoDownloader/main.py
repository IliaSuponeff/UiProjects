import os, sys
import pytube
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("YTubeDownloader")
        MainWindow.resize(600, 400)
        MainWindow.setWindowIcon(QIcon('./logo.ico'))
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        MainWindow.setStyleSheet("background-color: rgb(143, 143, 143);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setGeometry(QtCore.QRect(20, 80, 560, 120))
        self.status_label.setMaximumSize(QtCore.QSize(560, 120))
        self.status_label.setStyleSheet("background-color: rgb(77, 44, 34);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "font: 75 9pt \"Times New Roman\";")
        self.status_label.setText("")
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label.setObjectName("status_label")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(20, 10, 560, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        self.title_label.setMinimumSize(QtCore.QSize(560, 50))
        self.title_label.setStyleSheet("background-color: rgb(77, 44, 34);\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "font: 75 22pt \"Times New Roman\";")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.choosed_path_button = QtWidgets.QPushButton(self.centralwidget)
        self.choosed_path_button.setGeometry(QtCore.QRect(20, 220, 560, 50))
        self.choosed_path_button.setStyleSheet("background-color: rgb(77, 44, 34);\n"
                                               "color: rgb(255, 255, 255);\n"
                                               "font: 75 22pt \"Times New Roman\";\n"
                                               "border-color: rgb(255, 0, 0);")
        self.choosed_path_button.setObjectName("choosed_path_button")
        self.download_button = QtWidgets.QPushButton(self.centralwidget)
        self.download_button.setGeometry(QtCore.QRect(20, 340, 560, 50))
        self.download_button.setStyleSheet("background-color: rgb(77, 44, 34);\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "font: 75 22pt \"Times New Roman\";\n"
                                           "border-color: rgb(255, 0, 0);")
        self.download_button.setObjectName("download_button")
        self.inout_line = QtWidgets.QLineEdit(self.centralwidget)
        self.inout_line.setGeometry(QtCore.QRect(20, 280, 560, 50))
        self.inout_line.setStyleSheet("background-color: rgb(77, 44, 34);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "font: 75 9pt \"Times New Roman\";\n"
                                      "border-color: rgb(255, 0, 0);")
        self.inout_line.setText("")
        self.inout_line.setAlignment(QtCore.Qt.AlignCenter)
        self.inout_line.setObjectName("inout_line")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_label.setText(_translate("MainWindow", "YouTube Video Downloader"))
        self.choosed_path_button.setText(_translate("MainWindow", "Choose Path to Save Vidoes"))
        self.download_button.setText(_translate("MainWindow", "Download "))


class Downloader(QtCore.QThread):
    download_signal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.url = None

    def run(self):
        if self.check_link():
            self.download_signal.emit('Download process started!')
            if self._is_video():
                if self._download(self.url) == 'Done':
                    pass
                else:
                    self.download_signal.emit(f'Downloading error, \ncheck wi-fi and try again.')
            else:
                playlist = pytube.Playlist(self.url)
                for video in playlist.video_urls:
                    if self._download(video) == 'Done':
                        pass
                    else:
                        self.download_signal.emit(f'Downloading error, \ncheck wi-fi and try again.')
            self.download_signal.emit('Download process finished!')
        else:
            self.download_signal.emit('Invalid link to YouTube video.')
        self.download_signal.emit('finish')
        self.url = None

    def check_link(self):
        return self.url is not None and (self._is_video() or self._is_playlist())

    def init_args(self, url):
        self.url = url

    def _is_playlist(self):
        try:
            p = pytube.Playlist(self.url)
            p = p.title
            return True
        except:
            return False
        return False

    def _is_video(self):
        try:
            p = pytube.YouTube(self.url)
            p = p.title
            return True
        except:
            return False
        return False

    def _download(self, url):
        """Скачивание отдельного видео в макс разрешении"""
        try:
            video = pytube.YouTube(url)
            self.download_signal.emit(f'Start downloaded video:\n{video.title}')
            video = video.streams.get_highest_resolution()
            video.download()
            self.download_signal.emit(f'Finish downloaded video:\n{video.title}')
            return 'Done'
        except:
            return 'Error_1'
        return 'Error_2'


class UI(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.title = 'YTubeDownloader'
        self.setWindowTitle(self.title)
        self.ui.setupUi(self)

        self.download_path: os.PathLike = None
        self.ui.choosed_path_button.clicked.connect(self.get_folder)
        self.ui.download_button.clicked.connect(self.start)
        self.download_thread = Downloader()
        self.download_thread.download_signal.connect(self.handler)

    def start(self):
        if len(self.ui.inout_line.text()) > 5:
            if self.download_path is not None:
                link = self.ui.inout_line.text()
                self.download_thread.init_args(link)
                self.download_thread.start()
                self.locker(True)
            else:
                QtWidgets.QMessageBox.warning(self, 'Error!', "You don't choose folder to save.")
        else:
            QtWidgets.QMessageBox.warning(self, 'Error!', 'Link to the video is not specified.')

    def get_folder(self):
        self.download_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a folder to save videos')
        os.chdir(self.download_path)

    def handler(self, value):
        if value == 'finish':
            self.locker(False)
        else:
            self.ui.status_label.setText(value)

    def locker(self, lock_value):
        base = [self.ui.download_button, self.ui.choosed_path_button]
        for btn in base:
            btn.setDisabled(lock_value)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = UI()
    win.setWindowTitle('YTubeDownloader')
    win.show()
    sys.exit(app.exec_())
