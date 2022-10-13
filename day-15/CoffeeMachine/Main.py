#Coffee Machine project:
#
#
#Author: Brett Dickey

user_choice = input("What would you like? (espresso/latte/cappuccino): ")
choices = ["espresso", "latte", "cappuccino", "off", "report"]

while (user_choice not in choices):
    if user_choice.lower() not in choices:
        print("Try again, I didn't quite get that.")
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")


#Resources and Recipies for the Coffee Machine
"espresso" = {
    "water": 50
    "coffee": 18
    "milk": 0
    "cost": 1.5
}

"latte" = {
    "water": 200
    "coffee": 24
    "milk": 150
    "cost": 2.5
}

"cappuccino" = {
    "water": 250
    "coffee": 24
    "milk": 100
    "cost": 3
}

resources = {
    "water": 300
    "coffee": 200
    "milk": 100
    "money": 0
}