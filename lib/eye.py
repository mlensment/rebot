import math
import time
from .. import config

class Eye:
    target = None
    current_target_gaze = False
    target_gaze_cache = []

    action_timer_start = int(round(time.time() * 1000))
    action_timer = 0

    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y

    def is_visible(self):
        return self.x and self.y

    def is_looking_at_target(self):
        if not self.is_visible(): return Eye.current_target_gaze
        error = 10.0

        if math.fabs(self.x - Eye.target[0]) <= error and math.fabs(self.y - Eye.target[1]) <= error:
            Eye.current_target_gaze = True
            # self.update_target_gaze_cache(True)
            self.update_timer()
        else:
            Eye.current_target_gaze = False
            # self.update_target_gaze_cache(False)
            self.reset_timer()

        # print str(math.fabs(self.x - Eye.target[0])) + ' ' + str(math.fabs(self.y - Eye.target[1]))

        # if sum(i for i in Eye.target_gaze_cache) == 3:
        #     Eye.current_target_gaze = True
        #
        # if sum(not i for i in Eye.target_gaze_cache) == 3:
        #     Eye.current_target_gaze = False

        return Eye.current_target_gaze

    def not_looking_at_target(self):
        return not self.is_looking_at_target()

    def reset_timer(self):
        Eye.action_timer_start = Eye.time_in_millis()
        Eye.action_timer = 0

    def update_timer(self):
        Eye.action_timer = Eye.time_in_millis() - Eye.action_timer_start

    def update_target_gaze_cache(self, b):
        if len(Eye.target_gaze_cache) < 40:
            Eye.target_gaze_cache.append(b)
        else:
            Eye.target_gaze_cache = []
            # Eye.target_gaze_cache.pop(0)
        return b

    def action_confirmed(self):
        if Eye.action_timer >= config.ACTION_CONFIRM_TIME:
            return True

        return False

    @staticmethod
    def time_in_millis():
        return int(round(time.time() * 1000))
