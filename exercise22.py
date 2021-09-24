### Exercise 21 - Curso em Video
## Develop a program to open and reproduces a mp3 file
# You can install with pip install python-vlc
from pygame import mixer
mixer.init()
mixer.music.load('mp3file/music.mp3')
mixer.music.play()
input('Beyonce - Halo')