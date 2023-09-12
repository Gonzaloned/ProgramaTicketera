import sys

from PyQt6.QtCore import QUrl,QTimer
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer
from PyQt6.QtWidgets import QApplication

app = QApplication([])
def play():
    filename = "timbrecasa.mp3"
    player = QMediaPlayer()
    audio_output = QAudioOutput()
    player.setAudioOutput(audio_output)
    player.setSource(QUrl.fromLocalFile(filename))
    audio_output.setVolume(50)
    QTimer.singleShot(2000, lambda:player.play())

sys.exit(app.exec())