import math

class Eye:
    target = None
    current_target_gaze = False
    target_gaze_cache = []

    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y

    def is_visible(self):
        self.x and self.y

    def is_looking_at_target(self):
        if not self.is_visible(): return Eye.current_target_gaze
        error = 10.0

        if math.fabs(self.x - Eye.target[0]) <= error and math.fabs(self.y - Eye.target[1]) <= error:
            self.update_target_gaze_cache(True)
        else:
            self.update_target_gaze_cache(False)

        if sum(i for i in Eye.target_gaze_cache) == 3:
            Eye.current_target_gaze = True

        if sum(not i for i in Eye.target_gaze_cache) == 3:
            Eye.current_target_gaze = False

        return Eye.current_target_gaze

    def update_target_gaze_cache(self, b):
        Eye.target_gaze_cache.append(b)
        if len(Eye.target_gaze_cache) > 3:
            Eye.target_gaze_cache.pop(0)
        return b
