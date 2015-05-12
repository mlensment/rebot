# R(eye)bot

The object of this project is to create an eye controllable feeding robot for the disabled. Codename of the project is R(eye)bot which is Rebot, in short.

Code is designed to run on Raspberry PI 2 B with Raspbian operating system. In order to test the code, specialized hardware is required.

## Hardware
The hardware consists of two parts - glasses and robotic arm.

* Raspberry PI 2 B
* NOIR camera for the RPI
* 2x IR LEDs (800-1000nm) (+2 resistors)
* 1x LED (+1 resistor)
* 2x servo motors (+2 1000 ohm resistors to protect GPIO pins) (note that the leg servo should be more powerful)
* AC/DC adapters for the PI and the servo motors.

## Connecting the hardware
The camera has to be mounted about 5 centimeters away from the eye. PI does not have to go necessarily on the glasses, if you have a long ribbon cable for the camera handy.
![Glasses](https://raw.githubusercontent.com/mlensment/rebot/master/img/glasses.png "Glasses")

The arm must be designed in such a way that it will mechanically maintain the horizontal position for the spoon.
![Arm](https://raw.githubusercontent.com/mlensment/rebot/master/img/arm.png "Arm")

![Schematic](https://raw.githubusercontent.com/mlensment/rebot/master/img/schematic.png "Schematic")

## Feeding procedure

1. Patient sits at a 80-90 degree angle.
2. Rebot is turned on.
3. Rebot flashes the LED shortly, this means camera calibration will start in a second
4. Rebot flashes the LED for about 2 to 3 seconds, in that time, patient must look the LED. When the LED turns off, patient must look away.
5. Rebot flashes the LED shortly, this means all systems are online and the next time patient looks at the LED, the robot will begin to feed.
6. Rebot will scoop the first portion of food automatically
7. Patient must look at the LED for 2 seconds (the LED will illuminate). After this, the arm will move to feed the patient.
8. After eating, the patient must look at the LED again to move the arm down and scoop for another portion.
9. Steps 6-8 repeat.

## System setup
