from multiprocessing import Process, Value, Manager
import time
import math
import os
import config

class Servo(Process):
    def __init__(self):
        Process.__init__(self)
        self.spoon = Spoon()

    def run(self):
        print 'entered run'

        while(1):
            self.spoon.process_queue()

        print 'thread end'
        return 0

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


class Spoon:
    def __init__(self):
        self.angle = Value('f', 0.0)
        self.target_angle = Value('f', 0.0)
        manager = Manager()
        self.command_queue = manager.list([])

    def rotate(self, deg, timeframe = None):
        self.command_queue.append({'rotate': deg, 'timeframe': timeframe})

    def process_queue(self):
        if len(self.command_queue) == 0: return
        command = self.command_queue.pop(0)

        if 'rotate' in command:
            self.__rotate(command.get('rotate'), command.get('timeframe'))
        elif 'sleep' in command:
            print 'SLEEPING'
            time.sleep(command.get('sleep') / 1000)
