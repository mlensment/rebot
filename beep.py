from pygame import mixer

mixer.init()
alert = mixer.Sound('sound/beep-short.wav')
alert.play()
