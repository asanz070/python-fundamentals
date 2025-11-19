# ECHO is on.

"""
    Tuesday Review

    - Exercise 1:

    Define a new function fungus_among_us() which accepts a list plants as an argument
    - return True if the function contains the string "fungus" and False if not
    - don't overthink this one, there's a very simple method to doing it...
    
    Example: fungus_among_us( ["tree", "flower", "fungus", "moss"] ) >>> True
    
    - Exercise 2:

    Define a new function total_bill() which accepts a list of numbers item_costs
    - return the sum total of all items in the list
    
    Example: total_bill( [6, 9.99, 20] ) >>> 35.99
    
    - Exercise 3:

    Define a new function halfway_there() which accepts a list of arbitrary data items longer than 1 item
    - insert the string "HALFWAY" at the middle of the list and return the altered list
    - when inserting, you will need to make sure your index is an integer...
    
    Example: halfway_there( [1,2,3,4,5,6] ) >>> [1,2,3,"HALFWAY",4,5,6]
"""

# Exercise 1:

plants = ['tree', 'flower', 'fungus', 'moss']

def fungus_amongus(plants):
    for plant in plants:
        if plant == 'fungus':
            return True
    return False

print(fungus_amongus(plants))

# Exercise 2:

# Def version
def total_bill(item_costs):
    return sum(item_costs)

print(total_bill([6, 9.99, 20]))

# Lambda version
total_bill_two = lambda item_costs: sum(item_costs)
print(total_bill_two([6, 9.99, 20]))

# Exercise 3:

def halfway_there(items):
    # floor operator
    halfway = len(items) // 2
    # items[halfway] = "HALFWAY"
    items.insert(halfway, "HALFWAY")
    return items

print(halfway_there([1,2,3,4,5,6]))


# IMPORTING MODULES #

# This will create a "__pycache__" file
# from robot import new_function, robot_uprising, list_of_bots
# from robot import robot_uprising

# new_function()
# robot_uprising()
# print(list_of_bots)

# list_of_angry_bots = [("Angry " + bot) for bot in list_of_bots]
# print("WEDNESDAY HAS RUN")

from robot import Robot

wall_e = Robot('Wall_e', "2000 years", "not that smart, he likes garbage")