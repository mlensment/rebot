import math

class Eye:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def looks_at_target(self, target):
        error = 20.0

        if math.fabs(self.x - target[0]) <= error and math.fabs(self.y - target[1]) <= error:
            return True

        return False
