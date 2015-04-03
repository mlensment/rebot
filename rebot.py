import camera
import eye
import frame
import arm

class Rebot:
    def __init__(self):
        self.camera = Camera()

    def run:
        while(1):
            frame = camera.read()
            eye = frame.find_eye()
            if eye.looks_at_target():
                arm.eat()
            else:
                arm.take_food()
