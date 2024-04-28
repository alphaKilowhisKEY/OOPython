from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_running = True

make_coffee_class = CoffeeMaker()
money_machine = MoneyMachine()

menu_class = Menu()


while is_running:
	print(f"We can offer: {menu_class.get_items()}")
	user_choice = input("What would you like to order? ")
	if user_choice == 'report':
		make_coffee_class.report()
		money_machine.report()
	elif user_choice == 'off':
		is_running = False
	else:
		beverage = menu_class.find_drink(user_choice)
		if make_coffee_class.is_resource_sufficient(beverage) and money_machine.make_payment(beverage.cost):
			make_coffee_class.make_coffee(beverage)

