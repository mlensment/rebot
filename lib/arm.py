import argparse
import os
import math
import time
import servo_process as sp
from rebot import config

class Arm:
    def __init__(self):
        self.spoon_status = 'empty'
        self.leg_status = 'retracted'

    def init(self):
        self.sp = sp.ServoProcess()
        self.sp.start()

    def is_initialized(self):
        return self.sp.initialized.value

    def update(self, eye):
        if self.spoon_status in ['empty'] and self.leg_status in ['retracted']:
            self.scoop()

        if eye.action_confirmed():
            if self.spoon_status in ['full'] and self.leg_status in ['retracted']:
                self.extend()

            if self.spoon_status in ['empty'] and self.leg_status in ['extended']:
                self.retract()

        self.update_spoon_status()
        self.update_leg_status()

    def scoop(self):
        if self.not_finished(): return

        print '--> Scooping'
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

        print '--> Extending'
        self.leg_status = 'extending'
        self.sp.leg.rotate(70, 5000)
        self.sp.spoon.sleep(5000)

    def retract(self):
        if self.not_finished(): return

        print '--> Retracting'
        self.leg_status = 'retracting'
        self.sp.leg.rotate(20, 5000)
        self.sp.spoon.sleep(5000)

    def stop(self):
        self.sp.leg.stop()
        self.sp.spoon.stop()
        time.sleep(.1) # wait until servo buffers clear

    def shut_down(self):
        self.stop()

        self.spoon_status = 'shutting_down'
        self.leg_status = 'shutting_down'

        self.sp.spoon.rotate(0, 5000)
        self.sp.leg.rotate(0, 5000)

    def update_spoon_status(self):
        if self.spoon_status == 'scooping' and self.is_finished():
            print '--> Finished scooping'
            self.spoon_status = 'full'

        if self.spoon_status == 'shutting_down' and self.is_finished():
            self.spoon_status = 'shut_down'

        if self.leg_status == 'extended' and self.is_finished():
            self.spoon_status = 'empty'

    def update_leg_status(self):
        if self.leg_status == 'extending' and self.is_finished():
            print '--> Finished extending'
            self.leg_status = 'extended'

        if self.leg_status == 'retracting' and self.is_finished():
            print '--> Finished retracting'
            self.leg_status = 'retracted'

        if self.leg_status == 'shutting_down' and self.is_finished():
            self.leg_status = 'shut_down'


    def is_finished(self):
        return self.sp.spoon.is_finished() and self.sp.leg.is_finished()

    def not_finished(self):
        return not self.is_finished()
# a = Arm()
# a.run()
