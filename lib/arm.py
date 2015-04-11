import os

class Arm:
    def __init__(self):
        # load driver, redirect stdout to /dev/null
        # although servoblaster seems to be writing errors to stdout too, instead of stderr...
        os.system("sudo killall servod && sudo ./../bin/servod 1> /dev/null")

    def move_to(self, deg):
        pwm = deg * 1.11 # 1 degree = 0.011ms high pulse time
        pwm += 50  # minimum high pulse time is 0.5 milliseconds


        if os.path.exists('/dev/servoblaster'):
            os.system("echo 2=" + str(ceil(deg)) + " > /dev/servoblaster")
            os.system("echo 5=" + str(ceil(deg)) + " > /dev/servoblaster")
        else:
            raise 'ERROR: Servo driver was not found. Is servoblaster loaded?'

a = Arm()
a.move_to(120)
