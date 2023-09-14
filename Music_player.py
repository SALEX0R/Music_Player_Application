#USING PYTHON-QT
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
import pygame

class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()

        self.playlist = []
        self.current_song_index = 0

        pygame.mixer.init()

        self.setWindowTitle("Music Player")
        self.layout = QVBoxLayout(self)

        # Set the wallpaper image
        wallpaper_label = QLabel(self)
        wallpaper_pixmap = QPixmap("wallpaper.jpg")  # Replace with the path to your wallpaper image
        wallpaper_label.setPixmap(wallpaper_pixmap)
        self.layout.addWidget(wallpaper_label)

        self.label = QLabel("Welcome to the Music Player!", self)
        self.layout.addWidget(self.label)

        self.play_button = QPushButton("Play", self)
        self.next_button = QPushButton("Next", self)
        self.previous_button = QPushButton("Previous", self)
        self.stop_button = QPushButton("Stop", self)

        self.layout.addWidget(self.play_button)
        self.layout.addWidget(self.next_button)
        self.layout.addWidget(self.previous_button)
        self.layout.addWidget(self.stop_button)

        self.play_button.clicked.connect(self.play)
        self.next_button.clicked.connect(self.next)
        self.previous_button.clicked.connect(self.previous)
        self.stop_button.clicked.connect(self.stop)

    def play(self):
        # Add code for playing the music
        pygame.mixer.music.load(self.playlist[self.current_song_index])
        pygame.mixer.music.play()

    def next(self):
        # Add code for playing the next song in the playlist
        self.current_song_index += 1
        if self.current_song_index >= len(self.playlist):
            self.current_song_index = 0
        self.play()

    def previous(self):
        # Add code for playing the previous song in the playlist
        self.current_song_index -= 1
        if self.current_song_index < 0:
            self.current_song_index = len(self.playlist) - 1
        self.play()

    def stop(self):
        # Add code for stopping the music
        pygame.mixer.music.stop()

app = QApplication(sys.argv)
player = MusicPlayer()
player.show()
sys.exit(app.exec_())