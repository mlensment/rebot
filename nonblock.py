from multiprocessing import Process, Queue, Value
import time
import math
import os
import config

class Servo(Process):
    def __init__(self, servo, angle):
        Process.__init__(self)
        self.servo = servo

        self.angle = angle
        self.angle_to = angle

        self.daemon = True
        self.moving = False

    def run(self):
        print 'entered run'

        while(1):
            if self.angle != self.angle_to and not self.moving:
                print 'STARTING MOVING'
                self.ease()

        print 'thread end'
        return 0

    def ease(self):
        self.moving = True
        start_angle = self.angle.value
        end_angle = self.angle_to
        start_time = Servo.time_in_millis()

        # one line if here
        direction = 'asc'
        if self.angle.value > self.angle_to:
            direction = 'desc'

        while(1):
            elapsed_time = Servo.time_in_millis() - start_time

            self.angle.value = Servo.ease_in_out_sine(elapsed_time, start_angle, end_angle, 15000)

            if math.ceil(self.angle.value) >= self.angle_to and direction == 'asc':
                break

            if math.floor(self.angle.value) <= self.angle_to and direction == 'desc':
                break

            if self.angle.value > 180:
                self.angle.value = 180
            elif self.angle.value < 0:
                self.angle.value = 0

            self.rotate()
        self.moving = False

    def rotate(self):
        pwm = self.angle.value * ((config.SERVO_MAX_WIDTH - config.SERVO_MIN_WIDTH) / 180.0) # 1 degree = max high pulse time / 180
        pwm += config.SERVO_MIN_WIDTH  # add minimum high pulse time

        if os.path.exists('/dev/servoblaster'):
            os.system("echo " + str(self.servo) + "=" + str(math.ceil(pwm)) + " > /dev/servoblaster")
        else:
            raise Exception('Servo driver was not found. Is servoblaster loaded?')

    def validate_angle(self):
        pass

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

class App:
    def __init__(self):
        self.spoon_angle = Value('f', 0.0) # shared memory between sub and main process
        self.init_servos()

    def init_servos(self):
        self.spoon_servo = Servo(2, self.spoon_angle)
        self.spoon_servo.start()

    def run(self):
        i = 0
        self.ease_spoon(180)
        while(1):
            pass
            # is_alive()
            # time.sleep(5)
            # self.spoon_servo.terminate()
            # time.sleep(5)
            # self.ease_spoon(180)
            # i += 1


    def ease_spoon(self, deg):
        self.spoon_servo.angle_to = deg
        print 'setting angle'
        print deg
        # self.spoon_servo.start()

a = App()
a.run()
# a.ease_to(10)

# if __name__ == '__main__':
# num = Value('i', 0)
# spoon_servo = Servo(2, num)
# spoon_servo.daemon = True
# spoon_servo.start()
#
# i = 0
# while(1):
#     # print num.value
#     print spoon_servo.angle.value
#     i += 1
#     if i > 1000:
#         break
#


# if __name__ == '__main__':
#     num = Value('d', 0.0)
#
#     p = Process(target=f, args=(num))
#     p.start()
#     p.join()
#
#     time.sleep(3)
#     print num.value

# from multiprocessing import Process, Queue
# import time
#
# class Worker(Process):
#     def __init__(self, queue):
#         Process.__init__(self)
#         self.queue = queue
#         self.running = True
#
#     def run(self):
#         print 'entered run'
#         while self.running:
#             print 'thread time:', time.time()
#             time.sleep(.6)
#         print 'thread end'
#         return 0
# #
# if __name__ == '__main__':
#     queue = Queue()
#     p = Worker(queue)
#     p.daemon = True
#     p.start()
#     time.sleep(3)
#     p.running = False
#     print 'Main end'
