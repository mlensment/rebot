from multiprocessing import Process, Value, Manager
from multiprocessing.managers import SyncManager
import time
import math
import os
import config
import signal

class Servo:
    def __init__(self, servo_id):
        self.servo_id = servo_id
        self.angle = Value('f', 0.0)
        self.stop_signal = Value('b', False)

        # http://jtushman.github.io/blog/2014/01/14/python-|-multiprocessing-and-interrupts/
        manager = SyncManager() # instead of regular Manager because we want to ignore kb interrupt
        manager.start(Servo.init_mgr) # start the manager explicitly
        self.command_queue = manager.list([])
        self.current_command = manager.dict()

        self.finished = Value('b', False)

    def rotate(self, deg, timeframe = None):
        self.command_queue.append({'target_angle': deg, 'timeframe': timeframe})
        if not self.current_command: self.next_command()

    def sleep(self, timeframe):
        self.command_queue.append({'timeframe': timeframe})
        if not self.current_command: self.next_command()

    def is_finished(self):
        return self.finished.value

    def stop(self):
        del self.command_queue[:]
        self.stop_signal.value = True

    def update(self):
        if not self.current_command and len(self.command_queue) == 0:
            self.finished.value = True
        else:
            self.finished.value = False

        try:
            elapsed_time = Servo.time_in_millis() - self.current_command['start_time']

            if 'target_angle' in self.current_command:
                self.angle.value = Servo.ease_in_out_sine(
                    elapsed_time, self.current_command['start_angle'], self.current_command['target_angle'], self.current_command['timeframe']
                )

                self.cap_angle()
                self.can_rotate()

            if elapsed_time > self.current_command['timeframe']:
                self.next_command()
        except:
            pass

        if self.stop_signal.value:
            self.next_command()

        # if not self.current_command and len(self.command_queue) == 0:
        #     self.finished.value = True
        # else:
        #     self.finished.value = False

    def cap_angle(self):
        if self.angle.value > 180:
            self.angle.value = 180
        elif self.angle.value < 0:
            self.angle.value = 0

    def next_command(self):
        self.stop_signal.value = False
        self.current_command.clear()
        if len(self.command_queue) == 0: return
        self.current_command.update(self.command_queue.pop(0))

        if 'target_angle' in self.current_command:
            self.current_command['start_angle'] = self.angle.value

        self.current_command['start_time'] = Servo.time_in_millis()

    def can_rotate(self):
        direction = 'asc' if self.angle.value < self.current_command['target_angle'] else 'desc'

        cannot = math.ceil(self.angle.value) >= self.current_command['target_angle'] and direction == 'asc'
        cannot = cannot or math.floor(self.angle.value) <= self.current_command['target_angle'] and direction == 'desc'

        if cannot: self.stop_signal.value = True

        return cannot

    def alter_pwm(self):
        if self.is_finished(): return
        pwm = self.angle.value * ((config.SERVO_MAX_WIDTH - config.SERVO_MIN_WIDTH) / 180.0) # 1 degree = max high pulse time / 180
        pwm += config.SERVO_MIN_WIDTH  # add minimum high pulse time

        os.system("echo " + str(self.servo_id) + "=" + str(math.ceil(pwm)) + " > /dev/servoblaster")

    def decrease_pwm(self, val):
        os.system("echo " + str(self.servo_id) + "=-" + str(val) + " > /dev/servoblaster")

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

    @staticmethod
    def init_mgr():
        # ignore kb interrupt in SyncManager
        signal.signal(signal.SIGINT, signal.SIG_IGN)
