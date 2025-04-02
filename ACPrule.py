import re
import random
from colorama import Fore, init

init(autoreset=True)

a = {"destinations": ["Paris-Pleasant", "Goa-Thunderstroms", "Hawaii-Sunny", "Iceland-Cloudy"],
     "continents": ["Asia", "Europe", "America"]}
jokes = ["What do call a bear without bees? Ear",
         "Why did the bicycle fall over? Because it was two tired",
         "Why did the scarecrow win an award? Because he was outstanding in his field!",
         "What did the ocean say to the beach? Nothing, it just waved!",
         "I told my suitcase that there will be no vacations this year…Now I am dealing with emotional baggage."]


def process(b):
    return b.strip().lower()


def greet():
    print("Welcome")
    return input("What is your name : ")


def pref():
    rec = process(input("Enter your preference(destinations/continents)- "))
    if rec in a:
        print("How about", random.choice(a[rec]))

    else:
        print("invalid choice")


def tips():
    days = int(input("How many days will you be staying? "))
    if days <= 4:
        print("So its going to be a short trip")
    elif days >= 5:
        print("Its going to be hard visiting everything so make a list of your must-visits for a peaceful trip.")
    elif days >7:
        print("Try visiting all landmarks")


def joke():
    print(random.choice(jokes))


def recomend():
    name = greet()
    print("What would you like, jokes, tips or destinations to visit?")
    while True:
        input1 = process(input("Enter your choice: "))
        if "tips" in input1:
            tips()
        elif "jokes" in input1:
            joke()
        elif "destinations" in input1:
            pref()
        elif "exit" in input1:
            break
        else:
            print("invalid input")


recomend()
