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

    # The @ sign is a decorator that modifies the function that follows it
    # in this case it makes the method a class method that can be called on the class itself
    @classmethod
    # cls references the class itself, almost like "self" but for the class
    def build_killer_robot(cls, name):
        print(cls)
        new_bot = Robot(name=name, battery_life="way too long",
                        processing_power="kill", mode="destroy all humans")
        new_bot.consistency = "aluminum"
        return new_bot

    # D.R.Y - Don't Repeat Yourself

# The Roomba inherits from Robot (you could say it's a type of robot)
class Roomba(Robot):

    consistency = 'Cheap Plastic'

    def __repr__(self):
        return f"Roomba ( name={self.name} battery_life={self.battery_life} processing_power={self.processing_power})"

    def vacuum(self):
        return "VRRRRRRRRRRRRRRR BUMP BUMP BUMP"
