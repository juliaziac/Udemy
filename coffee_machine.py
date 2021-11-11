def coffee_machine():

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
        "money": 0, #added this
    }

    request = input("What would you like? (espresso/latte/cappuccino) ")

    if request == "off":
        quit()

    if request == "report":
        print(f"Water: {resources['water']}mL\n"
                f"Milk: {resources['milk']}mL\n"
                f"Coffee: {resources['coffee']}g\n"
                f"Money: ${resources['money']}")

    '''
    if request == "espresso":
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"]:
            if resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
                #insert coins
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough water.")

    #if request == "latte":

    #if request == "cappuccino":'''
