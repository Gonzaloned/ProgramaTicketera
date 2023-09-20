
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtMultimedia import (QAudioOutput, QMediaFormat,
                                  QMediaPlayer)
from PySide6.QtMultimediaWidgets import QVideoWidget
import sys

AVI = "video/x-msvideo"  # AVI
MP4 = 'video/mp4'

def get_supported_mime_types():
    result = []
    for f in QMediaFormat().supportedFileFormats(QMediaFormat.Decode):
        mime_type = QMediaFormat(f).mimeType()
        result.append(mime_type.name())
    return result


class Video(object):
    def open(self):
        self._ensure_stopped()
        file_dialog = QFileDialog(self.ventana)

        is_windows = sys.platform == 'win32'
        if not self._mime_types:
            self._mime_types = get_supported_mime_types()
            if (is_windows and AVI not in self._mime_types):
                self._mime_types.append(AVI)
            elif MP4 not in self._mime_types:
                self._mime_types.append(MP4)

        file_dialog.setMimeTypeFilters(self._mime_types)

        default_mimetype = AVI if is_windows else MP4
        if default_mimetype in self._mime_types:
            file_dialog.selectMimeTypeFilter(default_mimetype)

        movies_location = QStandardPaths.writableLocation(QStandardPaths.MoviesLocation)
        file_dialog.setDirectory(movies_location)
        if file_dialog.exec() == QDialog.Accepted:
            url = file_dialog.selectedUrls()[0]
            self._playlist.append(url)
            self._playlist_index = len(self._playlist) - 1
            self._player.setSource(url)
            self._player.play()

    @Slot()
    def _ensure_stopped(self):
        if self._player.playbackState() != QMediaPlayer.StoppedState:
            self._player.stop()



    def setupUi(self, MainWindow):

        #Save the main window
        self.ventana= MainWindow

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"#background{\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.background = QWidget(self.centralwidget)
        self.background.setObjectName(u"background")
        self.verticalLayout_2 = QVBoxLayout(self.background)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(40, 40, 40, 40)
        self.videoWidget = QWidget(self.background)
        self.videoWidget.setObjectName(u"videoWidget")

        self.verticalLayout_2.addWidget(self.videoWidget)


        self.verticalLayout.addWidget(self.background)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        #Def

        #Create a playlist
        self._playlist = []  # FIXME 6.3: Replace by QMediaPlaylist?
        self._playlist_index = -1

        #Create audio output
        self._audio_output = QAudioOutput()

        #Create a media player
        self._player = QMediaPlayer()

        #Set the audio output to player
        self._player.setAudioOutput(self._audio_output)

        #self._player.errorOccurred.connect(self._player_error)

        #Create the widget
        self._video_widget = QVideoWidget(self.videoWidget)
        self.layout_video = QVBoxLayout(self.videoWidget)
        self.layout_video.addWidget(self._video_widget)
        self._player.setVideoOutput(self._video_widget)

        self._mime_types = []

        #
        url = QUrl.fromLocalFile('VideoHospital.mp4')
        self._playlist.append(url)
        self._playlist_index = len(self._playlist) - 1
        self._player.setSource(url)
        self._player.play()
        #self.open()
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    vent=QMainWindow()
    ui= Video()
    ui.setupUi(vent)
    vent.show()
    sys.exit(app.exec())

