from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QUrl, QTimer
import os


class Audio:
    def __init__(self):
        self.sounds = {}
        self.paused_sounds = {}

    def load_sounds_from_directory(self, directory):
        for filename in os.listdir(directory):
            if filename.endswith(".wav"):
                self._load_sound(filename, os.path.join(directory, filename))

    def _load_sound(self, name, filename):
        effect = QSoundEffect()
        effect.setSource(QUrl.fromLocalFile(filename))
        self.sounds[name] = effect

    def play_sound(self, name, duration=None, loop_count=1):
        if name in self.sounds:
            sound = self.sounds[name]
            sound.setLoopCount(loop_count)
            sound.play()
            if duration is not None:
                QTimer.singleShot(duration, sound.stop)

    def pause_music(self, name):
        if name in self.sounds and name not in self.paused_sounds:
            sound = self.sounds[name]
            sound.stop()
            self.paused_sounds[name] = True

    def resume_music(self, name):
        if name in self.paused_sounds:
            sound = self.sounds[name]
            sound.play()
            del self.paused_sounds[name]