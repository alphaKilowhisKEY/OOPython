# Coffee Machine

## Description
This Python script simulates a coffee machine that can make various types of coffee drinks. It utilizes classes to represent different components such as the CoffeeMaker, Menu, MenuItem, and MoneyMachine. The script allows users to interactively order coffee, check resources and profit, and turn off the coffee machine.

## Features
- CoffeeMaker: Models the machine that makes the coffee. It keeps track of resources such as water, milk, and coffee beans, reports resource levels, checks if there are enough resources to make a drink, and makes coffee by deducting required ingredients from resources.
- Menu: Models the menu with drinks. It provides a list of available menu items and allows searching for a particular drink by name.
- MenuItem: Models each menu item. It stores information about the name, ingredients, and cost of a drink.
- MoneyMachine: Models the money handling component of the machine. It keeps track of profit, reports the current profit, processes coins inserted by the user, and handles payments for drinks.

## Usage
1. Run the script to start the coffee machine: $python3 main.py
2. Follow the prompts to order coffee, check resources and profit, or turn off the machine.
3. To order a drink, type the name of the drink as listed in the menu.
4. To check resources and profit, type 'report'.
5. To turn off the coffee machine, type 'off'.

## Requirements
- Python 3.x