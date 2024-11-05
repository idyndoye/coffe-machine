from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

ressource_machine = CoffeeMaker()
Money = MoneyMachine()
menu = Menu()

#ressource_machine.report()
#Money.report()



is_on = True
while is_on:
    option = menu.get_items() 
    choice = (input(f"What would you like? ({option}):"))
    if choice == "off":
        is_on = False
    elif choice == "report":
        ressource_machine.report()
        Money.report()
    else:
        drink = menu.find_drink(choice)
        if ressource_machine.is_resource_sufficient(drink) and Money.make_payment(drink.cost):           
            ressource_machine.make_coffee(drink)





