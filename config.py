DEBUG = True

# 0 on P1-7           GPIO-4
# 1 on P1-11          GPIO-17
# 2 on P1-12          GPIO-18
# 3 on P1-13          GPIO-21
# 4 on P1-15          GPIO-22
# 5 on P1-16          GPIO-23
# 6 on P1-18          GPIO-24
# 7 on P1-22          GPIO-25
LED_PIN = 12
SPOON_SERVO_ID = 5
LEG_SERVO_ID = 2

# these values apply for 2us pwm step
SERVO_MIN_WIDTH = 250 # 0 deg
SERVO_MAX_WIDTH = 1200 # 180 deg

WINDOW_NAME = "frame"

# how long user must look at the target to confirm the action (value in ms)
ACTION_CONFIRM_TIME = 2000
