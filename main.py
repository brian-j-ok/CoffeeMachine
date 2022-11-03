# TODO: 2. Check resources sufficient to make drink order.
def checkResources():
    for drink in MENU:
        can_make = True
        for ingredient in MENU[drink]["ingredients"]:
            if resources[ingredient] < MENU[drink]["ingredients"][ingredient]:
                can_make = False
        print("There are enough resources to make " + drink) if can_make else print("There are not enough resources to make" + drink)


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: 1. Print report of all the coffee machine resources.
def printResources():
    print("Water: " + str(resources["water"]))
    print("MilK: " + str(resources["milk"]))
    print("Coffee: " + str(resources["coffee"]))

checkResources()