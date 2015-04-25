import argparse
import os
import math
import time
import servo_process as sp

class Arm:
    def __init__(self):
        # self.init_servos()
        # 'scooping', ''
        self.spoon_status = 'empty'
        self.leg_status = 'retracted'

    def init(self):
        self.sp = sp.ServoProcess()
        self.sp.start()

    def is_initialized(self):
        return self.sp.initialized

    def update(self, eye):
        if self.spoon_status in ['empty'] and self.leg_status in ['retracted']:
            self.scoop()

        if self.leg_status == 'extended':
            self.feed()

        if self.leg_status == 'fed' and self.spoon_status == 'empty':
            self.retract()

        if eye.is_looking_at_target():
            if self.spoon_status in ['full'] and self.leg_status in ['retracted', 'retracting']:
                self.extend()

        if eye.is_not_looking_at_target():
            if self.spoon_status in ['full'] and self.leg_status in ['extending']:
                self.stop()
                self.spoon_status = 'empty'
                print 'STARTIN RETRACTING'
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
        self.sp.leg.rotate(70, 5000)
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

    def stop(self):
        self.sp.leg.stop()
        self.sp.spoon.stop()
        time.sleep(.1) # wait until servo buffers clear

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
# a = Arm()
# a.run()
