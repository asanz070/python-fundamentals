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


# PART TWO: FUNCTIONS & SCOPE
# ============================

# ===== SECTION 1: INTRO TO FUNCTIONS =====
# Functions are reusable blocks of code that perform a specific task
# They help you avoid repeating code and make programs more organized

# Example 1: Basic function with no parameters or return
def say_hello():
    """
    A simple function that prints a greeting.
    This function takes NO input and returns NO output.
    """
    print('Hello, World!')

# Call the function (execute the code inside)
say_hello()  # Output: Hello, World!

# ===== UNDERSTANDING RETURN vs PRINT =====
# PRINT: Shows output to the terminal (user sees it)
# RETURN: Gives data BACK to the code that called the function (user doesn't see it unless you print it)

# Example 2: Function with NO return statement
what_we_get = say_hello()
print(what_we_get)  # Output: None (because say_hello() doesn't return anything, just prints)

# Example 3: Function WITH return statement
def add_one_plus_one():
    """
    This function performs a calculation and RETURNS the result.
    The return keyword sends data back to whoever called this function.
    """
    return 1 + 1  # Returns 2 to the caller

what_we_get = add_one_plus_one()
print(what_we_get)  # Output: 2 (because we returned 2 and then printed it)

# ===== SECTION 2: PARAMETERS & TYPE HINTS =====
# Parameters are inputs to your function
# Type hints (: data_type) tell other programmers what data type is expected
# Type hints don't enforce the type - they're just documentation

# Example 4: Function with parameters and type hints
def add(number_one: int, number_two: int):
    """
    Takes two integers and returns their sum.
    The ': int' after each parameter is a TYPE HINT
    It tells others: "This function expects two integers"
    """
    return number_one + number_two

result = add(4, 4)  # Pass in two numbers (arguments)
print(result)  # Output: 8

# ===== SECTION 3: DEFAULT PARAMETERS =====
# Default parameters give variables a value if none is provided
# These are OPTIONAL parameters - you can change them or skip them

# Example 5: Function with default parameters
def multiply(a, b, c=1):
    """
    Multiply three numbers together.
    c=1 is a DEFAULT PARAMETER - if you don't pass 'c', it uses 1
    """
    return a * b * c

result_two = multiply(5, 2)        # c is not provided, so c=1 by default
print(result_two)                  # Output: 10 (5 * 2 * 1)

result_three = multiply(5, 2, 3)   # c is provided as 3
print(result_three)                # Output: 30 (5 * 2 * 3)

# ===== SECTION 4: FUNCTIONS WITH MULTIPLE RETURN VALUES =====
# Functions can return data of any type (strings, numbers, booleans, etc.)

# Example 6: Function that returns a string
def dad_joke_creator(question: str, punchline: str):
    """
    Takes two strings and combines them into a joke format.
    Returns a formatted string with both parts.
    """
    return f'{question} {punchline} :D'

dad_joke = dad_joke_creator(
    "Why can't your nose be 12 inches long?",
    "Because then it would be a foot!"
)
print(dad_joke)
# Output: Why can't your nose be 12 inches long? Because then it would be a foot! :D


# ===== SECTION 5: SCOPE (GLOBAL vs LOCAL) =====
# SCOPE determines where a variable can be accessed
# GLOBAL SCOPE: Variable defined outside functions (can be accessed everywhere)
# LOCAL SCOPE: Variable defined inside a function (only works inside that function)

# ===== EXAMPLE 5A: GLOBAL SCOPE & THE 'global' KEYWORD =====
outside_thoughts = 'I am happy and well adjusted'

def think_about_thoughts():
    """
    This function MODIFIES a global variable using the 'global' keyword.
    Without 'global', Python creates a new LOCAL variable instead.
    """
    global outside_thoughts  # Tell Python: "I want to modify the GLOBAL variable"
    outside_thoughts = outside_thoughts + " but I would like a sportscar"

# Call the function 4 times - each time modifies the global variable
think_about_thoughts()
think_about_thoughts()
think_about_thoughts()
think_about_thoughts()
print(outside_thoughts)
# Output: I am happy and well adjusted but I would like a sportscar but I would like a sportscar but I would like a sportscar but I would like a sportscar

# ===== EXAMPLE 5B: LOCAL SCOPE (function variable doesn't affect global) =====
outside_thoughts = 'I am happy and well adjusted'

def think_inside_thoughts():
    """
    This function creates a NEW LOCAL variable named 'outside_thoughts'
    This does NOT modify the global 'outside_thoughts'
    """
    outside_thoughts = 'I am an outside thought I think'  # LOCAL variable
    print(outside_thoughts)  # Prints the LOCAL version

think_inside_thoughts()
# Output: I am an outside thought I think

def think_my_outside_thoughts():
    """
    This function accesses the GLOBAL 'outside_thoughts' (no assignment)
    Since we're not assigning to it, we don't need the 'global' keyword
    """
    print(outside_thoughts)  # Uses the GLOBAL version

think_my_outside_thoughts()
# Output: I am happy and well adjusted (still the original, unmodified by the previous function)


# ===== SECTION 6: EARLY RETURNS (Return Stops Function Execution) =====
# When Python hits a 'return' statement, it IMMEDIATELY exits the function
# Any code after the return is NEVER executed

# Example 7: Multiple returns (only first one executes)
def multiple_returns():
    """
    Demonstrates that return statements end function execution.
    Everything after the first return is UNREACHABLE CODE.
    """
    return "I am the return"      # This executes and exits the function
    return "I'll be back"          # These NEVER execute
    return "MORE RETURNS"          # (unreachable code)
    return "EVEN MORE RETURNS"     # (unreachable code)

result = multiple_returns()
print(result)  # Output: I am the return


# ===== SECTION 7: PRACTICAL EXAMPLE - LOGIN FUNCTION =====
# Real-world example: checking username and password

def login(username: str, password: str):
    """
    Validates a user's login credentials.
    Returns True if credentials are correct, False otherwise.
    
    Steps:
    1. Check if username and password are not empty (truthy check)
    2. Check if they match the correct values
    3. Return True only if ALL checks pass
    """
    if username and password:  # Both must be non-empty (truthy)
        correct_username = 'user123'
        correct_password = 'password123'
        
        if username == correct_username and password == correct_password:
            return True  # Exit early - correct credentials!
    
    return False  # If any check fails, return False

# Test Case 1: Correct credentials
logged_in = login('user123', 'password123')
print("Logged IN:", logged_in)  # Output: Logged IN: True

# Test Case 2: Wrong username
logged_in = login('henry123', 'password123')
print("Logged IN:", logged_in)  # Output: Logged IN: False

# Test Case 3: Empty username/password
logged_in = login('', '')
print("Logged IN:", logged_in)  # Output: Logged IN: False


# ===== SECTION 8: THE 'pass' KEYWORD =====
# 'pass' is a placeholder - it does nothing but allows syntax to be valid
# Use it when you need a function body but don't have code yet

def passable_function():
    """
    The 'pass' keyword is a null operation (does absolutely nothing).
    
    Common uses:
    - Placeholder for functions you'll implement later
    - Placeholder for empty class definitions
    - Placeholder for empty exception handlers
    
    Without 'pass', Python would throw a SyntaxError for empty blocks.
    """
    pass  # This function literally does nothing

# passable_function()  # You can call it, but it won't do anything


# ===== SECTION 9: PRACTICE PROBLEM - RESTAURANT BILL CALCULATOR =====
"""
    CHALLENGE: Create a function that:
    - Takes in the total price of a meal
    - Optionally adds a tip percentage
    - Divides the grand total by the number of people
    - Returns a float (the per-person cost)
    
    EDGE CASES TO HANDLE:
    1. What if someone passes a string instead of a number?
    2. What if the number of people is 0? (Can't divide by zero!)
    3. What if tip is negative?
"""

# ===== STUDENT SOLUTION (My In-Class Version) =====
# Note: This solution has some issues - see instructor solution below
def restautarant_bill_calculator(meal_price, people=1, tip=1):
    """
    Student attempt at restaurant bill calculator.
    Has some logic issues - see instructor solution for better approach.
    """
    result2 = 0
    if type(people) != int:
        print('Please Enter A Number')
    elif people:  # Checks if people is truthy (not 0)
        result1 = meal_price / people
        print(result1)
        if type(tip) != int:
            print('Please Enter A Number')
        elif tip:
            result2 = result1 + tip
            return float(result2)

print("=== Student Solution ===")
print(restautarant_bill_calculator(30, 3, 5))     # Normal case
print(restautarant_bill_calculator("43", 3, 5))   # String meal_price (shows error)
print(restautarant_bill_calculator(30, 0))        # Zero people (edge case)


# ===== INSTRUCTOR SOLUTION (Better Practice) =====
def restaurant_bill_calculator(total: float, number_of_guests: int = 1, tip_percentage: float = 0.0):
    """
    Professional restaurant bill calculator.
    
    Parameters:
    - total (float): The meal cost before tip
    - number_of_guests (int): How many people sharing. Default = 1
    - tip_percentage (float): Tip as decimal (0.20 = 20%). Default = 0.0 (no tip)
    
    Returns:
    - float: The per-person cost including tip
    - str: Error message if validation fails
    
    BEST PRACTICES SHOWN:
    1. Type checking BEFORE calculations
    2. Validates edge cases (0 guests)
    3. Clear error messages
    4. Returns consistent data type when possible
    """
    
    # Validation: Check if all parameters are the correct type
    # Note: In Python, True is technically an int, so we need strict type checking
    if type(total) == int and type(number_of_guests) == int and type(tip_percentage) == float:
        
        # Edge case: Can't split bill among zero people
        if number_of_guests > 0:
            subtotal = total * (1 + tip_percentage)  # Add tip to total
            per_guest_total = subtotal / number_of_guests  # Divide by guests
            return float(per_guest_total)
        else:
            return 'Get some friends!'  # Humorous error message
    else:
        return 'Incorrect Data Types'  # Type validation failed

print("\n=== Instructor Solution ===")

# Test 1: Simple case (no tip)
the_bill = restaurant_bill_calculator(50, 1, 0.0)
print(f"Test 1 - No tip, 1 person: ${the_bill}")
# Output: Test 1 - No tip, 1 person: $50.0

# Test 2: Split between 2 people (no tip)
the_bill = restaurant_bill_calculator(50, 2, 0.0)
print(f"Test 2 - No tip, 2 people: ${the_bill}")
# Output: Test 2 - No tip, 2 people: $25.0

# Test 3: 20% tip split between 2 people
the_bill = restaurant_bill_calculator(50, 2, 0.20)
print(f"Test 3 - 20% tip, 2 people: ${the_bill}")
# Output: Test 3 - 20% tip, 2 people: $30.0

# Test 4: Using default parameter (1 guest, 0% tip)
the_bill = restaurant_bill_calculator(50)
print(f"Test 4 - Defaults: ${the_bill}")
# Output: Test 4 - Defaults: $50.0

# Test 5: EDGE CASE - Zero guests (can't divide by zero)
the_bill = restaurant_bill_calculator(50, 0)
print(f"Test 5 - Zero guests: {the_bill}")
# Output: Test 5 - Zero guests: Get some friends!

# Test 6: EDGE CASE - String for total price
the_bill = restaurant_bill_calculator("50 Buckos", 5)
print(f"Test 6 - String price: {the_bill}")
# Output: Test 6 - String price: Incorrect Data Types

# Test 7: EDGE CASE - String for number of guests
the_bill = restaurant_bill_calculator(50, "Maybe between six or seven! We'll see!")
print(f"Test 7 - String guests: {the_bill}")
# Output: Test 7 - String guests: Incorrect Data Types

# ===== KEY TAKEAWAYS =====
# 1. Always validate user input before using it
# 2. Handle edge cases (division by zero, wrong types, etc.)
# 3. Use type hints to document expected inputs
# 4. Return meaningful error messages or None
# 5. Use descriptive variable names so others understand your code
# 6. Comment complex logic for future review