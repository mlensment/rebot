import argparse
import os
import math
import time
import servo_process as sp

class Arm:
    def __init__(self):
        self.init_servos()
        # 'scooping', ''
        self.spoon_status = ''
        self.status = ''

    def init_servos(self):
        self.sp = sp.ServoProcess()
        self.sp.start()

    def run(self):
        i = 0
        # self.ease_spoon(180)
        # self.sp.spoon.rotate(180, 2000)
        # self.sp.spoon.sleep(2000)
        # self.sp.spoon.rotate(90, 2000)
        # self.sp.leg.rotate(180, 2000)
        # self.sp.leg.rotate(90, 2000)
        # self.leg_servo.rotate(180, 2000)
        # self.reset_position()
        while(1):
            # pass
            self.scoop()
            self.update_spoon_status()

            if self.spoon_status == 'finished_scooping':
                self.reset_position();
            #
            # if self.status == 'reset':
            #     print 'SHUTTING DOWN'
            #     break
            #
            # self.update_status()

            # if self.spoon_status == 'finished_scooping':
            #     self.reset_position()
            #     break
            # print self.sp.leg.finished()
            # time.sleep(1)
            # self.sp.spoon.stop()
            # self.scoop()
            # # time.sleep(.5)
            # # self.spoon_servo.rotate_instant(180)
            # self.update_spoon_status()

            # time.sleep(5)
            # self.spoon_servo.stop()
            # is_alive()
            # self.ease_spoon(0)

            # self.spoon_servo.terminate()
            # time.sleep(5)
            # self.ease_spoon(180)
            # i += 1

    def scoop(self):
        if self.spoon_status in ['scooping', 'finished_scooping']: return
        print 'SCOOPING'
        self.spoon_status = 'scooping'

        self.sp.spoon.rotate(0, 2000)
        self.sp.leg.sleep(2000)

        self.sp.leg.rotate(0, 2000)
        self.sp.spoon.sleep(2000)

        self.sp.spoon.rotate(90, 2000)
        self.sp.leg.sleep(2000)

        self.sp.leg.rotate(20, 2000)

    def update_spoon_status(self):
        print str(self.sp.spoon.command_queue)
        print str(self.sp.spoon.current_command)
        print str(self.sp.leg.command_queue)
        print str(self.sp.leg.current_command)
        if self.spoon_status == 'scooping' and self.sp.spoon.is_finished() and self.sp.leg.is_finished():
            print 'FINISHED SCOOPING'
            print str(self.sp.spoon.command_queue)
            print str(self.sp.spoon.current_command)
            print str(self.sp.leg.command_queue)
            print str(self.sp.leg.current_command)
            if self.sp.leg.current_command:
                raise Exception('bla')
            self.spoon_status = 'finished_scooping'

    def update_status(self):
        if self.status == 'resetting' and self.sp.spoon.is_finished() and self.sp.leg.is_finished():
            print 'RESET'
            self.status = 'reset'

    def reset_position(self):
        # TODO: Gradually decrease angle until error, then servos are 0 position
        if self.status in ['resetting', 'reset']: return
        print 'RESETTING'
        self.status = 'resetting'
        self.sp.spoon.rotate(0, 2000)
        self.sp.leg.rotate(0, 2000)

a = Arm()
a.run()
