class Arm:
    def __init__(self):
        pass

    def move_to(self, deg):
        try:
            f = open("/dev/servoblaster", 'w')
    		f.write('2=' + deg)
            f.write('5=' + deg)
    		f.close()
        except:
		    print("Error writing to servoblaster. Is the driver loaded?")

a = Rebot()
a.move_to(120)
