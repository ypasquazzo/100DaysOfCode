from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

action = input("What would you like? (espresso/latte/cappuccino): ")

while True:

    if action == "report":
        coffee_maker.report()

    elif action == "espresso" or action == "latte" or action == "cappuccino":
        menu_item = menu.find_drink(action)
        if coffee_maker.is_resource_sufficient(menu_item):
            if money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)
    elif action == "off":
        break
    else:
        print("This is not a valid command")

    action = input("What would you like? (espresso/latte/cappuccino): ")
