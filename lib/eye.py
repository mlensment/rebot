import math

class Eye:
    target = None
    current_target_gaze = False
    target_gaze_cache = []

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_looking_at_target(self, target):
        error = 20.0

        if math.fabs(self.x - target[0]) <= error and math.fabs(self.y - target[1]) <= error:
            update_target_gaze_cache(True)
        else:
            update_target_gaze_cache(False)

        if sum(i for i in a) == 3:
            Eye.current_target_gaze = True

        if sum(not i for i in a) == 3:
            Eye.current_target_gaze = False

        return Eye.current_target_gaze

    def update_target_gaze_cache(self, b):
        Eye.target_gaze_cache.append(b)
        if len(Eye.target_gaze_cache) > 3:
            Eye.target_gaze_cache.pop()
        return b
