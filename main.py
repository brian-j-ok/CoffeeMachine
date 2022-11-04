# TODO: 2. Check resources sufficient to make drink order.
def checkResources(drink):
    if drink in MENU:
        for ingredient in MENU[drink]["ingredients"]:
            if resources[ingredient] < MENU[drink]["ingredients"][ingredient]:
                print("Sorry there is not enough " + ingredient + ".")
                return
        checkMoney(drink)
    else:
        print("Can't find that drink")

def checkMoney(drink):
    total = 0
    change = input("Please enter $" + str('${:,.2f}'.format(MENU[drink]["cost"])) + " in change.\n[quarters, dimes, nickles, pennies]\n")
    for coin in change.split(","):
        print(coin)
        # TODO 1. Need to fix indent at beggning of string
    #     coin_type = change.rstrip('0123456789')
    #     coin_quantity = change[len(coin_type):]
    #     total += (coins[coin_type] * int(coin_quantity))
    # print(total)

coins = {
    "q": 25,
    "d": 10,
    "n": 5,
    "p": 1
}

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
    print()
    print("Water: " + str(resources["water"]) + "ml")
    print("MilK: " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["coffee"]) + "g")
    print("Money")

def start():
    response = input("What would you like? (espresso/latte/cappuccino):\n")
    match response:
        case "off":
            return
        case "report":
            printResources()
        case _:
            checkResources(response)

start()