import argparse
import os
import math
import time
import servo_process as sp

class Arm:
    def __init__(self):
        self.init_servos()
        # 'scooping', ''
        self.spoon_status = 'empty'
        self.leg_status = 'retracted'

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
            if self.spoon_status in ['empty'] and self.leg_status in ['retracted']:
                self.scoop()

            if self.spoon_status in ['full'] and self.leg_status in ['retracted', 'retracting']: # and is watching target
                self.extend()

            if self.leg_status == 'extended':
                self.feed()

            if self.leg_status == 'fed' and self.spoon_status == 'empty':
                self.retract()

            # if self.leg_status in ['extended']:
            #     self.shut_down()
            #
            # if self.leg_status in ['shut_down'] and self.spoon_status in ['shut_down']:
            #     break

            # if self.spoon_status == 'finished_scooping':
            #     self.reset_position();

            self.update_spoon_status()
            self.update_leg_status()
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
        if self.not_finished(): return

        print 'SCOOPING'
        self.spoon_status = 'scooping'

        self.sp.spoon.rotate(0, 2000)
        self.sp.leg.sleep(2000)

        self.sp.leg.rotate(0, 2000)
        self.sp.spoon.sleep(2000)

        self.sp.spoon.rotate(90, 2000)
        self.sp.leg.sleep(2000)

        self.sp.leg.rotate(20, 2000)

    def extend(self):
        if self.not_finished(): return

        print 'EXTENDING'
        self.leg_status = 'extending'
        self.sp.leg.rotate(80, 5000)
        self.sp.spoon.sleep(5000)

    def feed(self):
        if self.not_finished(): return

        print 'FEEDING'
        self.leg_status = 'feeding'
        self.spoon_status = 'feeding'
        self.sp.spoon.sleep(5000)
        self.sp.leg.sleep(5000)

    def retract(self):
        if self.not_finished(): return

        print 'RETRACTING'
        self.leg_status = 'retracting'
        self.sp.leg.rotate(20, 5000)
        self.sp.spoon.sleep(5000)

    def shut_down(self):
        if self.not_finished(): return

        print 'SHUTTING DOWN'
        self.spoon_status = 'shutting_down'
        self.leg_status = 'shutting_down'

        self.sp.spoon.rotate(0, 5000)
        self.sp.leg.rotate(0, 5000)

    def update_spoon_status(self):
        if self.spoon_status == 'scooping' and self.is_finished():
            self.spoon_status = 'full'

        if self.spoon_status == 'shutting_down' and self.is_finished():
            self.spoon_status = 'shut_down'

        if self.spoon_status == 'feeding' and self.is_finished():
            self.spoon_status = 'empty'


    def update_leg_status(self):
        if self.leg_status == 'extending' and self.is_finished():
            self.leg_status = 'extended'

        if self.leg_status == 'feeding' and self.is_finished():
            self.leg_status = 'fed'

        if self.leg_status == 'retracting' and self.is_finished():
            self.leg_status = 'retracted'

        if self.leg_status == 'shutting_down' and self.is_finished():
            self.leg_status = 'shut_down'


    def is_finished(self):
        return self.sp.spoon.is_finished() and self.sp.leg.is_finished()

    def not_finished(self):
        return not self.is_finished()
a = Arm()
a.run()
