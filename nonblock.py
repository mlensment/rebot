from multiprocessing import Process, Value, Manager
import time
import math
import os
import config

class ServoProcess(Process):
    def __init__(self):
        Process.__init__(self)
        self.spoon = Servo()

    def run(self):
        print 'entered run'

        while(1):
            self.spoon.update()
            self.spoon.alter_pwm()

        print 'thread end'
        return 0


class Servo:
    def __init__(self):
        self.angle = Value('f', 0.0)

        manager = Manager()
        self.command_queue = manager.list([])

        self.current_command = None

    def update(self):
        if not self.current_command: return

        elapsed_time = Servo.time_in_millis() - self.current_command['start_time']

        if 'rotate' in self.current_command:
            self.angle.value = Servo.ease_in_out_sine(
                elapsed_time, self.current_command['start_angle'], self.current_command['target_angle'], self.current_command['timeframe']
            )

            self.cap_angle()
            self.can_rotate()
        # elif: 'sleep' in self.current_command:
        # if elapsed_time > self.current_command['timeframe']: self.next_command()

    def next_command(arg):
        if len(self.command_queue) == 0: return
        self.current_command = self.command_queue.pop(0)

        if 'rotate' in self.current_command:
            self.current_command['start_angle'] = self.angle.value

        self.current_command['start_time'] = Servo.time_in_millis()

    def can_rotate(self, command):
        direction = 'asc' if self.angle.value < command['target_angle'] else 'desc'

        cond = math.ceil(self.angle.value) >= command['target_angle'] and direction == 'asc'
        cond = cond or math.floor(self.angle.value) <= command['target_angle'] and direction == 'desc'

        # cond = cond or self.stop_signal.value == True

        if cond: self.next_command()

    def rotate(self, deg, timeframe = None):
        self.command_queue.append({'rotate': deg, 'timeframe': timeframe})

    def alter_pwm(self):
        pwm = self.angle.value * ((config.SERVO_MAX_WIDTH - config.SERVO_MIN_WIDTH) / 180.0) # 1 degree = max high pulse time / 180
        pwm += config.SERVO_MIN_WIDTH  # add minimum high pulse time

        if os.path.exists('/dev/servoblaster'):
            os.system("echo " + str(2) + "=" + str(math.ceil(pwm)) + " > /dev/servoblaster")
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
