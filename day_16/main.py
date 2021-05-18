from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

is_machine_on = True
while is_machine_on:
    command = input(f"What do you want to order? ({my_menu.get_items()})")
    if command == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    elif command == "off":
        is_machine_on = False
    else:
        order = my_menu.find_drink(command)
        if order is None:
            continue

        if not my_coffee_maker.is_resource_sufficient(order):
            continue

        if not my_money_machine.make_payment(order.cost):
            continue

        my_coffee_maker.make_coffee(order)

    input("Enter to continue")