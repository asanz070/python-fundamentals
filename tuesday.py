# ECHO is on.

"""
    Monday Review Practice

    Define a new function create_full_name() which takes in two arguments: first_name and last_name as strings
    - the function returns the first_name and last_name as a single string
    - Example:    create_full_name("Bob", "Marley") >>> "Bob Marley"

    Define a new function c_to_f() which takes in one argument: temp_celsius as a number
    - the function returns the temperature as farenheit, you may return either an int or a float
    - the formula for conversion is F = (C * 9/5) + 32
    - Example:    c_to_f(30) >>> 86.0

    Define a new function open_thieves_cave() which takes in one argument: passphrase as a string
    - the function returns True if the passphrase is "open sesame" and False if the passphrase is anything else
    - Example:    open_thieves_cave("open sesame") >>> True
    - Example:    open_thieves_cave("speak friend and enter") >>> False

    For these functions do not worry about edge cases; assume the functions will receive the proper data type
    For example you don't need to worry about giving c_to_f a string
"""

# Exercise One:

def create_full_name(first_name:str, last_name:str):
    return first_name + " " +  last_name

print(create_full_name('Alan', 'Sanchez'))
print(create_full_name('Sophia', 'Fuentes'))

# Exercise Two:

def c_to_f(temp_celcius:int):
    convert = (temp_celcius * 9/5) + 32
    return float(convert)

print(c_to_f(12))
print(c_to_f(32))
print(c_to_f(-3))

# Exercise Three:

def open_thieves_cave(passpharase:bool):
    if passpharase == "Open Sesame":
        return True
    else:
        print("Speak Friend and Enter")
        return False

phrase = open_thieves_cave('Open Sesame')
print(phrase)

phrase = open_thieves_cave('password')
print(phrase)

phrase = open_thieves_cave(12)
print(phrase)


# Tuesdays Lesson:

# Intro into LISTS:

# Lists are a collection of data
sodas = ["Coke", "Pepsi", "Dr. Pepper", "Sprite"]

# Index - where it is in the list
# "sodas[0]" - "Coke"
# "sodas[1]" - "Pepsi"
# We can access an item by its index
# If we have a negative indexes (expect 0) they will count from the end instead of the beginning

sodas[0] # "Coke"
sodas[3] or sodas[-1] # Sprite

sodas[1] = "Root Beer" # you can add a specific item in the list like so, but you could also use append()

# You may use different types of data in a list
different_stuff = [True, 'Whatever', 12, 12.0, [], "THE END"]

# You can also put in line breaks if you feel like it
listception = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# This will access the first list's second element
listception[0][1] # will return the 2nd item in the first list ---> 2

# How do we add to a list?
# We use the method .append()
# This method will add an item at the end of the list always
sodas.append('Fanta')
sodas.append('Cream Soda')

# "len()" Method:
# Gives you how many items there are in the list
len(sodas) # will return 6 items in the list

# "insert()" Method:
# Inserts an item at a specific index
sodas.insert(0, "Diet Coke Zero")

# ".sort()" Method:
# This will sort the list and modify the original
sodas.sort()

# ".pop()" Method:
#  Removes and returns the item at a specific index (or the last item if no index is given).
sodas.pop()

# Remove an item by its index
sodas.pop(3)

# Lambda function:
# It's like a short function
# A lambda automatically "implicitly" returns
plus_one = lambda x : x + 1

create_fullname = lambda first_name, last_name: first_name + " " + last_name

# Lambda function would be like this if it was a long function
# def plus_one(x):
#     return x + 1

# Higher order functions - takes in a function and does something with it
def do_three_times(fn):
    fn()
    fn()
    fn()

def say_hi():
    print("Hi")

pass_in_3 = lambda fn: fn(3)

# filtered


# Exercise Overview:

"""
    Create a new list with three pieces of furniture >>> ["chair", "table", "bed"]

    Step One:
    - Access the second furniture item in the list
    - Access the last furniture item in the list
    
    Step Two:
    - Use python to check the length of the list
    - Add three new furniture items to the list
    
    Step Three:
    - Add a new furniture item to the beginning of the list
    - Add a new furniture item as the 3rd item in the list

    Step Four:
    - Sort the list

    Step Five:
    - Remove the second to last item in the list
    - Remove a "chair" from the list if it exists

    Step Six:
    - Use python to check the length of the list

    Additional Exercises:

    - Look up a way to count the number of times "bed" appears in the list. 
    We only want "bed" exactly, don't worry about things like "waterbed"
    
    - Look up a way to reverse the order of the list

    - Look up a way to clear the entire list
"""

# List:
furniture = ["chair", "table", "bed"]

# Step 1:
furniture[1] # "table"
furniture[2] # "bed"
furniture[-1] # "bed" --> alternative way

# Step 2:
len(furniture)

furniture.append('couch')
furniture.append('recliner')
furniture.append('coffee table')

# Step 3:
furniture.insert(0, "recliner")
furniture.insert(2, "lamp")

# Step 4:
furniture.sort()

# Step 5:
furniture.pop(-2)
furniture.remove("chair")

# Step 6:
len(furniture)

# Additional Exercises:

# Look up a way to count the number of times "bed" appears in the list
furniture.count("bed")

# Two different variations of reversing a list
furniture.sort(reverse=True)
furniture.reverse()

# Look up a way to clear the entire list
furniture.clear()


# Intro to TUPLES, SETS, DICTIONARIES:

# Important to Know:
# When we create the tuple it will be like this forever
my_tuple = ('pizza', 'hamburger', 'hotdog', 'salad')


# Sets
my_set = {1,2,3,4,5,6,7,7,7,7,7,7,7,7} # {1,2,3,4,5,6,7}

# Dictionaries:
my_dict = { "key" : "value"}

person = {
    "first_name": "Chett",
    "last_name": "Tiller",
    "height": "1000 feet tall",
    "age": 21,
    "favorite_sodas": ["Coke", "Pepsi"]      
}

person["first_name"]
person['height'] # accesses the height in the dict

# person['fav_movie'] - will result in a key error

person.get('fav_movie') # will not result in a key error

person['first_name'] = 'Boba Chett'

person['favorite_movie'] = 'The Land Before Time'

def legally_able_to_drive(person:dict):
    return person['age'] >= 16


# LOOPS and ITERATIONS

for item in sodas:
    print(item)

for thing in person:
    print(thing)

for item in my_set:
    print(item)

for key in person:
    print(f"{key} - {person[key]}")

# While Loops:

index = 0
while index < len(sodas):
    print(sodas[index])
    index += 1

# List Comprehesion

empty_sodas = [("Empty " + item) for item in sodas]
print(empty_sodas)

shaken_sodas = [(s + " explosion") for s in sodas]
print(shaken_sodas)

my_numbers = [1,2,3,4,5]
squared = [num * num for num in my_numbers]
print(squared)

person_keys = [key for key in person]
print(person_keys)

person_value = [person[value] for value in person]
print(person_value)

# Afternoon Guided Exercise:

"""
    New Function called fizz_buzz_list
"""

test_case_one = [1,2,3,4,5,6,7,8]
test_case_two = [50, 55, 98, 133]
test_case_three = [6081, 1200, 134, 547, 896, -200, -35, -6081, 0]

# def fizz_buzz_list(list_of_nums):
#     for number in list_of_nums:
#         if number % 3 == 0 and number % 5 == 0:
#             index = list_of_nums.index(number)
#             list_of_nums[index] = 'Fizz Buzz'
#         # if the number is divisible by three
#         elif number % 3 == 0:
#             print('fizz')
#             # replace the number with Fizz by first getting its index
#             index = list_of_nums.index(number)
#             list_of_nums[index] = 'Fizz'
#         elif number % 5 ==0:
#             index = list_of_nums.index(number)
#             list_of_nums[index] = 'Buzz'
#         else:
#             print(number)
    
#     return list_of_nums


# print(fizz_buzz_list(test_case_one))
# print(fizz_buzz_list(test_case_two))
# print(fizz_buzz_list(test_case_three))


# While Loop Version:

def fizz_buzz_list_while(list_of_nums):
    index = 0
    while index < len(list_of_nums):
        if list_of_nums[index] % 3 == 0 and list_of_nums[index] % 5 == 0:
            print("Fizz Buzz")
            list_of_nums[index] = 'Fizz Buzz'
        elif list_of_nums[index] % 3 == 0:
            print("Fizz")
            list_of_nums[index] = 'Fizz'
        elif list_of_nums[index] % 5 == 0:
            print("Buzz")
            list_of_nums[index] = 'Buzz'
        index += 1
    
    return list_of_nums

print("While Loop Version",fizz_buzz_list_while(test_case_one))
print("While Loop Version",fizz_buzz_list_while(test_case_two))
print("While Loop Version",fizz_buzz_list_while(test_case_three))