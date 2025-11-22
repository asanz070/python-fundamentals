# # ECHO is on.

# # Wednesday Review

# """
#     Create a class MovieReview which has required attributes movie_title:str, reviewer_name:str, score:int, date_reviewed:datetime.date.
#         - You may need to look up how to use datetime.date (hint: you'll need from datetime import date and you can make new ones with date(2025, 12, 25))
# """
# from movie_reviews import MovieReview
# from datetime import date

# predator = MovieReview(movie_title="Predator", reviewer_name="Alan", date_reviewed=date.today(), score=4)


# """
#     Create an instance method pretty_print() which prints the review like so: "<movie_title> review by <reviewer_name> on <date_reviewed>: <score> / 5 stars".
#         - Example: land_before_time.pretty_print() >>> "Land Before Time review by Fred Flintstone on 2014-4-12: 5/5 stars"
# """
# def pretty_print(self):
#     return f"{self.movie_title} review by {self.reviewer_name} on {self.date_reviewed}: {self.score} / 5 stars"


# """
#     Create an instance method increase_score() which increases that movie's score by 1 so long as it doesn't go above 5 stars.
# """
def increase_score(self):
    if self.score < 5:
        self.score += 1
    else:
        raise ValueError("Score cannot exceed 5")
    return self.score


# """
#     Create an instance method update_review(). This accepts an argument of a new_score and optionally a new_reviewer. This updates the score and sets the date_reviewed to today. If new_reviewer was passed this will also update the reviewer_name and if not it will retain the previous reviewer_name.
#         - Example: land_before_time.update_review(4) # score changed to 4, date becomes today, reviewer is still "Fred Flinstone"
#         - Example: land_before_time.update_review(5, "Littlefoot") # score changed to 5, date becomes today, reviewer becomes "Littlefoot"
    
# """
# def update_review(self, new_score, new_reviewer=None):
#     self.score = new_score
#     self.date_reviewed = date.today()
#     if new_reviewer:
#         self.reviewer_name = new_reviewer
#     return self.score, self.reviewer_name, self.date_reviewed


# """
#     Create a class method review_bomb() which accepts a movie_title and num_reviews. This generates a review num_reviews times for the movie_title each with a score of 1, a reviewer_name of Statler & Waldorf, and a date_reviewed of today.
#         - Example: MovieReview.review_bomb("Plan 9 From Outer Space")
# """
# @classmethod
# def review_bomb(cls, movie_title, num_reviews):
#     reviews = []
#     for _ in range(num_reviews):
#         review = cls(movie_title=movie_title, reviewer_name="Statler & Waldorf", score=1, date_reviewed=date.today())
#         reviews.append(review)
#     return reviews


# ERROR HANDLING #

def divide_numbers(num_one, num_two):
    try: # do this if you can
        if type(num_one) != int or type(num_two) != int:
            raise TypeError("Inputs must be integers")
        print(num_one / num_two)
    except ZeroDivisionError as error: # do this if you got an error
        print(f"Could not divide {num_one} by {num_two}")
    except TypeError as error:
        print(f"We got a type error!")
        print(error)
    finally: # 
        print('Function Done')

def cube_number(number):
    try:
        number ** 3
    except TypeError:
        return "This data type cannot be cubed"


# try:
#     divided_by_zero = 100 / 0
# except:
#     print("I could not divide by zero... WOMP WOMP")

# print("I am below the error")


# HTTP REQUEST: #

import requests

def get_dad_joke():
    try:
        response = requests.get("https://icanhazdadjoke.com", headers={"Accept": "text/plain"})
        joke_text = response.text
        return joke_text
    except:
        print("Unable tp fetch dad joke")

# new_joke = get_dad_joke()


def fetch_number_of_jokes(num_jokes):
    jokes_list = []
    for _ in range(num_jokes):
        fetched_joked = get_dad_joke()
        jokes_list.append(fetched_joked)
    return jokes_list

# WRITING TO JSON FILE #

import json

def put_into_json_file(list_data):
    current_jokes = get_from_json_file()
    with open('jokes.json', 'w') as json_file:
        combined_jokes = current_jokes + list_data
        json.dump(combined_jokes, json_file, indent=4)

def get_from_json_file():
    with open("jokes.json", "r") as json_file:
        data = json.load(json_file)
        return data
    
# BUILDING PROGRAM #

# user.stories --> a user will be able to...

# a user will be able to boot up the program and see a menu
# a user will be able to fetch a new dad joke
# a user will be able to save or discard a fetched dad joke
# a user will be able to see their saved dad joke
# a user will be able to to exit the program

import time

class DadJokeApplication:

    running = True

    def run(self):
        while self.running:
            self.menu()
            user_choice = input("Please choose an option: ")
            print(f'You choose: {user_choice}')
            
            if user_choice == "1":
                self.get_dad_joke()
            elif user_choice == '2':
                self.print_saved_dad_jokes()
            elif user_choice == '3':
                self.exit()
            else:
                time.sleep(1)
                print("\nPlease choose a valid option!\n")



    def menu(self):
        print("-- Welcome to Dad Jokes APP-- ")
        print("1. Get new dad joke")
        print("2. See saved dad jokes")
        print("3. EXIT")

    def get_dad_joke(self):
        new_joke = fetch_number_of_jokes(1)
        print(new_joke)
        user_input = input("Save joke? [y/n]: ")

        if user_input == 'y':
            # save the joke
            print("Saving this gem of a joke!")
            put_into_json_file(new_joke)
        else:
            print("Discarding the joke...")

    def print_saved_dad_jokes(self):
        print("------------------------------")
        saved_jokes = get_from_json_file()
        for joke in saved_jokes:
            print(joke)
        print("------------------------------")

    def exit(self):
        self.running = False
        print("\nSee ya later alligator\nIn a while croocodile")

app = DadJokeApplication()
app.run()