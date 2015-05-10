from multiprocessing import Process, Value
import os
import config
import servo
import signal

class ServoProcess(Process):
    def __init__(self):
        print '----> Checking servo driver...'
        if not os.path.exists('/dev/servoblaster'):
            raise Exception('Servo driver was not found. Is servoblaster loaded?')
        else:
            print '----> Servo driver loaded'

        Process.__init__(self)
        self.spoon = servo.Servo(config.SPOON_SERVO_ID)
        self.leg = servo.Servo(config.LEG_SERVO_ID)
        self.initialized = Value('b', False)

    def run(self):
        # signal.signal(signal.SIGINT, signal.SIG_IGN)
        try:
            print '----> Initiating servo calibration sequence...'

            i = config.SERVO_MAX_WIDTH - config.SERVO_MIN_WIDTH
            while(i > 0):
                self.spoon.decrease_pwm(10)
                self.leg.decrease_pwm(10)
                i -= 10

            print '----> Servo calibration complete'
            self.initialized.value = True

            while(1):
                self.spoon.update()
                self.spoon.alter_pwm()

                self.leg.update()
                self.leg.alter_pwm()
        except KeyboardInterrupt:
            print "Keyboard interrupt in SP"
