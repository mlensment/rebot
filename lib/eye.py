import math
import time
import config

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
        error = 15.0

        if math.fabs(self.x - Eye.target[0]) <= error and math.fabs(self.y - Eye.target[1]) <= error:
            Eye.current_target_gaze = True
            self.update_timer()
        else:
            Eye.current_target_gaze = False
            self.reset_timer()

        return Eye.current_target_gaze

    def reset_timer(self):
        Eye.action_timer_start = Eye.time_in_millis()
        Eye.action_timer = 0

    def update_timer(self):
        Eye.action_timer = Eye.time_in_millis() - Eye.action_timer_start

    def action_confirmed(self):
        if Eye.action_timer >= config.ACTION_CONFIRM_TIME:
            return True

        return False

    @staticmethod
    def time_in_millis():
        return int(round(time.time() * 1000))
