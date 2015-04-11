import os

class Arm:
    def __init__(self):
        pass

    def move_to(self, deg):
        os.system("echo 2=" + str(deg) + " > /dev/servoblaster")
        os.system("echo 5=" + str(deg) + " > /dev/servoblaster")

a = Arm()
a.move_to(120)
