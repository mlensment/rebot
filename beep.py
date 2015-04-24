# from pygame import mixer
#
# mixer.stop()
# mixer.init()
# alert = mixer.Sound('sound/beep-short.wav')
# alert.stop()

import pyglet

music = pyglet.resource.media('sound/beep-short.wav')
music.play()

pyglet.app.run()
