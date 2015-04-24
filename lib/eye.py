import math

class Eye:
    def __init__(self, pupil_x, pupil_y):
        self.pupil_x = pupil_x
        self.pupil_y = pupil_y

    def looks_at_target(self, target):
        error = 20.0

        if math.fabs(self.pupil_x - target[0]) <= error and math.fabs(self.pupil_y - target[1]) <= error:
            return True

        return False
