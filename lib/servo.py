from multiprocessing import Process, Value
import time
import math
import os
import config

class Servo(Process):
    def __init__(self, servo):
        Process.__init__(self)
        self.servo = servo

        self.angle = Value('f', 0.0)
        self.angle_to = Value('f', 0.0)

        self.daemon = True
        self.stop_signal = Value('b', False)

    def run(self):
        print 'entered run'

        while(1):
            if self.angle.value != self.angle_to.value:
                print 'STARTING MOVING'
                self.rotate()

        print 'thread end'
        return 0

    def stop(self):
        self.stop_signal.value = True

    def rotate(self):
        start_angle = self.angle.value
        end_angle = self.angle_to.value
        start_time = Servo.time_in_millis()

        while(1):
            elapsed_time = Servo.time_in_millis() - start_time
            self.angle.value = Servo.ease_in_out_sine(elapsed_time, start_angle, end_angle, 15000)
            self.cap_angle()
            if self.cannot_move(end_angle): break
            self.alter_pwm()

    def cap_angle(self):
        if self.angle.value > 180:
            self.angle.value = 180
        elif self.angle.value < 0:
            self.angle.value = 0

    def cannot_move(self, end_angle):
        direction = 'asc' if self.angle.value < end_angle else 'desc'

        cond = math.ceil(self.angle.value) >= end_angle and direction == 'asc'
        cond = cond or math.floor(self.angle.value) <= end_angle and direction == 'desc'
        cond = cond or self.stop_signal.value == True

        if cond:
            self.angle_to.value = self.angle.value
            self.stop_signal.value = False
            return True
        return False

    def alter_pwm(self):
        pwm = self.angle.value * ((config.SERVO_MAX_WIDTH - config.SERVO_MIN_WIDTH) / 180.0) # 1 degree = max high pulse time / 180
        pwm += config.SERVO_MIN_WIDTH  # add minimum high pulse time

        if os.path.exists('/dev/servoblaster'):
            os.system("echo " + str(self.servo) + "=" + str(math.ceil(pwm)) + " > /dev/servoblaster")
        else:
            raise Exception('Servo driver was not found. Is servoblaster loaded?')


    @staticmethod
    def ease_in_out_sine(elapsed_time, begin, end, timeframe):
        b = begin
        c = math.fabs(end - begin)
        begin = 0

        pos = -c / 2 * (math.cos(math.pi * elapsed_time / timeframe) - 1)

        if b > end:
            return math.fabs(pos - b)
        else:
            return pos + b

    @staticmethod
    def time_in_millis():
        return int(round(time.time() * 1000))
