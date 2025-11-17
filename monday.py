# ==========================================
# INTRO TO PYTHON: DATA TYPES & CONDITIONALS
# ==========================================

# SECTION 1: COMMENTS
# ==================
# Comments are notes for humans - Python ignores them
# They help explain what your code does
# Use # for single line comments


# SECTION 2: STRINGS (Text Data)
# ===============================
# A string is any text enclosed in quotes (' or ")

# Example 1: Simple string variable
variable_name = '---> Hello, World! <---'
print(variable_name)  # Output: ---> Hello, World! <---

# Example 2: Longer string (like a dad joke!)
my_favorite_dad_joke = 'Why did the scarecrow win an award? Because he was outstanding in his field'
print(my_favorite_dad_joke)

# Example 3: String concatenation (combining strings)
# Method 1: Using f-strings (formatted strings) - RECOMMENDED
question = 'What do you call fake spaghetti?'
answer = 'An Imposta'

# f-strings let you insert variables using {variable_name}
formattted_jokes = f'{question} {answer} {my_favorite_dad_joke}' + ". " + my_favorite_dad_joke
print(formattted_jokes)


# SECTION 3: NUMBERS
# ===================
# There are TWO number data types in Python:

# Integer: Whole numbers (no decimal point)
# Examples: 5, -10, 0, 100
number_of_snakes = 12
print(number_of_snakes)  # Output: 12

# Float: Numbers with decimals
# Examples: 3.14, 9.8, -2.5
average_number_of_snakes = 9.8
print(average_number_of_snakes)  # Output: 9.8

# Tip: You can check the type of data using type()
# print(type(number_of_snakes))  # Would output: <class 'int'>
# print(type(average_number_of_snakes))  # Would output: <class 'float'>


# SECTION 4: BOOLEANS & TRUTHINESS
# ==================================
# Boolean: A data type with only TWO possible values: True or False

# True Example:
i_am_true = True
print(i_am_true)  # Output: True

# False Example:
i_am_false = False
print(i_am_false)  # Output: False

# Truthy vs Falsy Concept:
# Some values are considered "truthy" (act like True) or "falsy" (act like False)
# Truthy: Non-empty strings, numbers that aren't 0, True
# Falsy: Empty strings "", 0, False, None, empty lists []

i_am_truthy = "YES I AM TRUTHY"  # Non-empty strings are truthy
print(i_am_truthy)  # Output: YES I AM TRUTHY

# The "not" operator - REVERSES the boolean value
# not True becomes False
# not False becomes True
# not (truthy value) becomes False
# Output: False (because the string is truthy, not reverses it)
print(not i_am_truthy)
print(not False)  # Output: True
print(not 0)  # Output: True (because 0 is falsy)


# SECTION 5: CONDITIONALS (if/elif/else)
# ========================================
# Conditionals allow your code to make decisions
# if: execute code IF a condition is True
# elif: else if - execute if previous condition was False AND this is True
# else: execute if all previous conditions were False

# Example setup:
first_name = 'Alan'
last_name = 12  # Intentionally an integer (wrong type!)

# Check if variables are NOT strings using type() and !=
# type(variable) returns the data type
# != means "not equal to"
# False (first_name IS a string)
first_name_is_not_string = type(first_name) != str
# True (last_name is NOT a string)
last_name_is_not_string = type(last_name) != str

# LOGICAL OPERATORS:
# "and" operator: BOTH conditions must be True
# "or" operator: AT LEAST ONE condition must be True

# Condition 1: Check if name matches AND last name matches
if first_name == 'Alan' and last_name == 'Sanchez':
    print("Welcome User!")

    # Nested if: Check another condition INSIDE the first if
    if number_of_snakes >= 10:
        print('You have a lot of snakes today Alan')

# Condition 2: Check if EITHER name or last name is not a string
# Using "or" - this runs if first_name_is_not_string OR last_name_is_not_string (or both)
elif first_name_is_not_string or last_name_is_not_string:
    # This will print because last_name IS not a string
    print("Entry must be text")

# Condition 3: Just check if first_name is truthy
elif first_name:
    print('Hello Stranger!')

# Condition 4: Fallback - if NONE of the above were true
else:
    print("IT'S SOOOOOO FALSE")

# This always prints (outside all conditionals)
print('All Done!!')


# ######################################################################################################## #


# PART TWO:

# Intro to Functions:

# Define a function:
def say_hello():
    # Put here what the funcitons would be doing here:
    print('Hello, World!')


#  Call the function
say_hello()

# Example of what will not work:
# No data is being passed or return
what_we_get = say_hello()
print(what_we_get)  # will return NONE

# This works because the key word returns data from the function


def add_one_plus_one():
    return 1 + 1


what_we_get = add_one_plus_one()
print(what_we_get)

# You can add data types to the parameters to imply to other what is expected:

# Example where we pass data:
# For example, add the expected data type:


def add(number_one: int, number_two: int):
    return number_one + number_two


result = add(4, 4)
print(result)

# Different example using multiplication:
# You can use default parameters to hold a value and then modify iy if needed. Optional to use


def multiply(a, b, c=1):
    return a * b * c


result_two = multiply(5, 2)
print(result_two)

# Not all functions are mathematicall:


def dad_joke_creator(question: str, punchline: str):
    return f'{question} {punchline} :D'


dad_joke = dad_joke_creator(
    "Why can't your nose be 12 inches long?", "Because then it would be a foot!")
print(dad_joke)


# Scope:

# Can be accessed from inside the functions because this is a global scope
outside_thoughts = 'I am happy and well adjusted'


def think_about_thoughts():
    # Access or call the global scope
    # print(outside_thoughts)
    # Using the keyword global will help access it and modify it inside the function and then call it outside of the function
    global outside_thoughts
    outside_thoughts = outside_thoughts + "but I would like a sportscar"


# This will repeat the function or what is happening inside rather
think_about_thoughts()
think_about_thoughts()
think_about_thoughts()
think_about_thoughts()
print(outside_thoughts)

# Different Example:
outside_thoughts = 'I am happy and well adjusted'


def think_inside_thoughts():
    # We have declared a new variable called outside_thoughts in the local scope
    outside_thoughts = 'I am an outside thought I think'
    print(outside_thoughts)


think_inside_thoughts()


def think_my_outside_thoughts():
    print(outside_thoughts)


think_my_outside_thoughts()


# Login Example:

# You can only return
def multiple_returns():
    # This first return ends the functions execution
    return "I am the return"
    # These other returns have NO EFFECT
    return "I'll be back"
    return "MORE RETURNS"
    return "EVEN MORE RETURNS"


result = multiple_returns()
print(result)


def login(username: str, password: str):
    if username and password:
        correct_username = 'user123'
        correct_password = 'password123'
        if username == correct_username and password == correct_password:
            return True

    return False


logged_in = login('user123', 'password123')  # True
print("Logged IN:", logged_in)

logged_in = login('henry123', 'password123')  # False
print("Logged IN:", logged_in)

logged_in = login('', '')  # False
print("Logged IN:", logged_in)


def passable_function():
    # Pass keyword:
    # The pass keyword in Python is a null operation. When executed, it does nothing.
    # Its primary use is as a placeholder in situations where a statement is syntactically required but no code execution is desired or necessary at that moment.
    # pass
    pass


# =================================================================
# Practice:

"""
    Create a function that takes in the total price of the meal: 
    - You can optionally add a tip, 
    - If there are multiple people divide the grand total by the number of people
    - Your output should be a float 

    Edge Cases:
    - What happens if someone puts in something that ISN'T a number
    - What happends if the number of people is 0
"""

# My In-Class Solution:

# def restautarant_bill_calculator(meal_price, people=1, tip = 1):
#     result2 = 0
#     if type(people) != int:
#         print('Please Enter A Number')
#     elif people:
#         result1 = meal_price / people
#         print(result1)
#         if type(tip) != int:
#             print('Please Enter A Number')
#         elif tip:
#             result2 = result1 + tip
#             return float(result2)
     
# print(restautarant_bill_calculator(30, 3, 5))
# print(restautarant_bill_calculator("43", 3, 5))
# print(restautarant_bill_calculator(30, 0))

# Instructor Solution:

def restaurant_bill_calculator(total:float, number_of_guests:int=1, tip_percentage:float=0.0):

    if type(total) == int and type(number_of_guests) == int and type(tip_percentage) == float:
        if number_of_guests > 0:
            subtotal = total * (1 + tip_percentage)
            per_guest_total = subtotal / number_of_guests
            return float(per_guest_total)
        else:
            return 'Get some friends!'
    else:
        return 'Incorrect Data Types'

the_bill = restaurant_bill_calculator(50, 1, 0.0)
print(f"The Total Bill: {the_bill}")

the_bill = restaurant_bill_calculator(50, 2, 0.0)
print(f"The Total Bill: {the_bill}")

the_bill = restaurant_bill_calculator(50, 2, 0.20)
print(f"The Total Bill: {the_bill}")

the_bill = restaurant_bill_calculator(50)
print(f"The Total Bill: {the_bill}")

the_bill = restaurant_bill_calculator(50, 0)
print(f"The Total Bill: {the_bill}") # Will not work because you can't divide by zero, unless you had an if statement to handle this error

the_bill = restaurant_bill_calculator("50 Buckos", 5)
print(f"The Total Bill: {the_bill}")

the_bill = restaurant_bill_calculator(50, "Maybe between six or seven! We'll see!")
print(f"The Total Bill: {the_bill}")