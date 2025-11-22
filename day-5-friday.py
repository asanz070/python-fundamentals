# ECHO is on.

# Data Structure & Algorithms

# Example Challenge:
# Write a function get_average() which accepts list_of_munbers:list
#   Return all of those numbers average togehter

# Which are the inputs for my algorithm?

def get_average(list_of_numbers):
    # pseudocode
    # sum all of the numbers
        # iterate through and add all those numbers to a total
    total = 0
    for number in list_of_numbers:
        total = total + number
    print(f"Total: {total}")
    # divide by the length of the list
    #     get the length of the list
    length = len(list_of_numbers)
    print(f"Length: {length}")
    result = total / length
    # return all numbers averaged
    return result

# Refactored Code:
get_average_redo = lambda list_of_numbers: sum(list_of_numbers) / len(list_of_numbers)

# Challenge One:
# Write a function bill_calculator() which accepts item_price_list:list, tax_rate:float and tip:float.

#     The item_price_list is a list of prices as floats such as [9.99, 5.80, 12.99]
#     tax_rate and tip are floats  that indicate the percentage that goes to each such as 0.087 and 0.20
#     The function returns the sum of the list plus the additional taxes and tips applied
#     BONUS: The function also accepts an optional parameter party_size which defaults to 1 and automatically divides the total by the number of people dining

def bill_calculator(item_price_list, tax_rate, tip, party_size=1):
    # add items together
    subtotal = sum(item_price_list)
    # get the tax
    tax = subtotal * tax_rate
    # get the tip
    tipped_amount = subtotal * tip
    # add everything together
    total = subtotal + tax + tipped_amount
    # divide the number of people
    per_person_total = total / party_size
    #return the final bill
    return total

# Challenge Two:
# Write a function reverse_list()  which accepts a data_list:list of arbitrary data

#     The function returns the list in reverse order
#     Do not use .reverse() or .sort() for this challenge
#     BONUS: Allow the function to accept and reverse a string as well


my_list = [1,2,3,4,5,6]

def reverse_list(data_list):
    reversed_list = []
    for item in data_list:
        reversed_list.insert(0,item)
    if isinstance(data_list, str):
        return "".join(reversed_list)
    return reversed_list

# My Solution:
def reverse_list(data):
    return data[::-1]

print(reverse_list(my_list))

# Challenge Three:
# Write a function character_counter() which accepts string:str as an argument

#     The function returns a dictionary with each key being a character and each value being the number of times it appeared
#     Example: character_counter("data") >>> { "d": 2, "a": 1, "t": 1 }
#     Example: character_counter("character") >>> { "c":2, "h":1, "a":2, "r":2, "t":1 }
#     Hint: There is a way to iterate through string characters
#     Hint: You should start with an empty dictionary
#     Hint: When assessing a character you may do something differently depending on whether it's in the dictionary already or not...

def character_counter(string):
    char_frequency = {}
    for char in string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    return f"Character frequencies: {char_frequency}"

print(character_counter("banana"))

# Bonus Challenge One:
# Write a function fibonacci_of() which takes in an integer n:int  which gives the nth integer in the fibonacci sequence

#     You can find more information about the the fibonacci sequence here: link
#     There is something known as a recursive function where a function can call itself... use that information wisely!

def fibo_series(n:int):
    print(f"Fibonacci for n={n}")
    if n == 1:
        return 0
    if n == 2:
        return 1
    # Recursive function
    return fibo_series(n - 1) + fibo_series(n - 2)

print(fibo_series(10))


# Bonus Challenge Two:
# Write a function rot_13() which accepts a string:str as an argument

#     The function returns an altered string with each of the letter characters "rotated" 13 places in the alphabet
#     Example: rot_13("hello there") >>> "uryyb gurer"
#     Hint: There is a function chr() which allows you to see the character for an ascii code and ord() which allows you to see the ascii code for a character...
#     There are multiple ways of doing this!

def rot_13(string: str):
    result = ""
    for character in string:
        if 97 <= ord(character) <= 109:
            result += chr(ord(character) + 13)
        elif 110 <= ord(character) <= 122:
            result += chr(ord(character) - 13)
        else:
            result += character
    return result

print(rot_13("abc"))

# API_KEY - authorization for YOUR ACCOUNT to access an api

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("API_KEY")
print(f"API_KEY ---> {API_KEY}")

# Make the request
import requests

def fetch_animal_facts(animal:str):
    base_url = "https://api.api-ninjas.com/v1/animals?name="
    response = requests.get(base_url + animal, headers={'X-Api-Key': API_KEY})
    return response