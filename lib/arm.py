import os

class Arm:
    def __init__(self):
        os.system("sudo ./../bin/servod 1> /dev/null")

    def move_to(self, deg):
        if os.path.exists('/dev/servoblaster'):
            os.system("echo 2=" + str(deg) + " > /dev/servoblaster")
            os.system("echo 5=" + str(deg) + " > /dev/servoblaster")
        else:
            raise 'ERROR: Servo driver was not found. Is servoblaster loaded?'

a = Arm()
a.move_to(120)
