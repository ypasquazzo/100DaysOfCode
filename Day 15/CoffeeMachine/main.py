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

water = 500
milk = 300
coffee = 100
money = 0


def print_report():
    print(f"Water: {water}")
    print(f"Milk: {milk}")
    print(f"Coffee: {coffee}")
    print(f"Money: {money}")


def check_resources(drink):
    check = True
    if MENU[drink]["ingredients"]["water"] > water:
        print("Sorry there is not enough water.")
        check = False
    if "milk" in MENU[drink]["ingredients"] and MENU[drink]["ingredients"]["milk"] > milk:
        print("Sorry there is not enough milk.")
        check = False
    if MENU[drink]["ingredients"]["coffee"] > coffee:
        print("Sorry there is not enough coffee.")
        check = False
    return check


def insert_coins():
    q = int(input("How many quarters? "))
    d = int(input("How many dimes? "))
    n = int(input("How many nickles? "))
    p = int(input("How many pennies? "))

    return q * 0.25 + d * 0.1 + n * 0.05 + p * 0.01


def transaction(c, a):
    if MENU[a]["cost"] <= c:
        global water
        water -= MENU[a]["ingredients"]["water"]
        global milk
        if "milk" in MENU[a]["ingredients"]:
            milk -= MENU[a]["ingredients"]["milk"]
        global coffee
        coffee -= MENU[a]["ingredients"]["coffee"]
        global money
        money += round(MENU[a]["cost"], 2)
        return round(c - MENU[a]["cost"], 2)
    else:
        return -1


action = input("What would you like? (espresso/latte/cappuccino): ")

while True:

    if action == "report":
        print_report()

    elif action == "espresso" and check_resources("espresso"):
        change = insert_coins()
        rest = transaction(change, "espresso")
        if rest > 0:
            print(f"Here is ${rest} in change.")
            print("Enjoy your Espresso!")
        elif rest == 0:
            print("Enjoy your Espresso!")
        else:
            print("Sorry that's not enough money. Money refunded.")

    elif action == "latte" and check_resources("latte"):
        change = insert_coins()
        rest = transaction(change, "latte")
        if rest > 0:
            print(f"Here is ${rest} in change.")
            print("Enjoy your Latte!")
        elif rest == 0:
            print("Enjoy your Latte!")
        else:
            print("Sorry that's not enough money. Money refunded.")

    elif action == "cappuccino" and check_resources("cappuccino"):
        change = insert_coins()
        rest = transaction(change, "cappuccino")
        if rest > 0:
            print(f"Here is ${rest} in change.")
            print("Enjoy your Cappuccino!")
        elif rest == 0:
            print("Enjoy your Cappuccino!")
        else:
            print("Sorry that's not enough money. Money refunded.")

    elif action == "off":
        break

    else:
        print("This is not a valid action!")

    action = input("What would you like? (espresso/latte/cappuccino): ")
