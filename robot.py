def new_function():
    print("I DO SOMETHING")


def robot_uprising():
    print("BEEP BOOP EXTERMINATE")

# list_of_bots = ['C-3PO', 'DALEK NUMBER 12', 'T-1000']

# This won't work because this would cause a circular import
# from wednesday import list_of_angry_bots

# print("ROBOTS HAS RUN")

# Intro to Classes:

# Class is a blueprint that makes instances of that new data type / class

class Robot:
    consistency = 'metal'

    # init stands for initialize and runs whenever we initialize a new instance of the class
    def __init__(self, name, battery_life, processing_power, **kargs):
        print("BEEP BOOP MAKING A NEW ROBOT")
        # print(**kargs)
        self.name = name
        self.battery_life = battery_life
        self.processing_power = processing_power
        self.kargs = kargs

        for key in kargs:
            setattr(self, key, kargs[key])

    # Representation that will show when we print the robot
    def __repr__(self):
        return f"Robot ({self.name} battery_life={self.battery_life} processing_power={self.processing_power})"
    
    # What we see when we print() or make our instance into a string with str()
    def __str__(self):
        return f"HELLO I AM A ROBOT NAMED {self.name}"

    # A method (a function attatched to a class) must pass in "self" which references itself
    def beep(self):
        return 'BEEP'

    def bend(self):
        return "BENDING"

    def move(self):
        return "MOVING"

    def analyze_info(self, info):
        return f"BEEP BOOP ANALYZING {info}"
