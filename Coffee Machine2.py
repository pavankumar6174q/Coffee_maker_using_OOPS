from menu import Menu, MenuItem
from CoffeeMaker import CoffeeMaker
from money_machine import MoneyMachine



money_machine = MoneyMachine()

coffee_maker = CoffeeMaker()
menu = Menu()



should_stop = True
while should_stop:
    user_choice = input(f"what do you want , {menu.get_items()}:  ").lower()
    if user_choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif user_choice == "off":
        should_stop = False
    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

