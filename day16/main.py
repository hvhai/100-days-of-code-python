class CoffeeMachine:
    """
    A class to represent a coffee machine.
    """

    def __init__(self):
        """
        Initialize the coffee machine with resources and menu.
        """
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
            "money": 0.0
        }
        self.menu = {
            "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 1.5},
            "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5},
            "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.0}
        }

    def report(self):
        """
        Print the current resource values of the coffee machine.
        """
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.resources['money']}")

    def check_resources(self, drink):
        """
        Check if there are enough resources to make the selected drink.

        Parameters:
        drink (str): The name of the drink to check resources for.

        Returns:
        bool: True if there are enough resources, False otherwise.
        """
        for item in self.menu[drink]:
            if item != "cost" and self.resources[item] < self.menu[drink][item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        """
        Process the coins inserted by the user.

        Returns:
        float: The total monetary value of the coins inserted.
        """
        print("Please insert coins.")
        total = int(input("How many quarters?: ")) * 0.25
        total += int(input("How many dimes?: ")) * 0.10
        total += int(input("How many nickles?: ")) * 0.05
        total += int(input("How many pennies?: ")) * 0.01
        return total

    def transaction_successful(self, money_received, drink_cost):
        """
        Check if the transaction is successful.

        Parameters:
        money_received (float): The amount of money received from the user.
        drink_cost (float): The cost of the selected drink.

        Returns:
        bool: True if the transaction is successful, False otherwise.
        """
        if money_received >= drink_cost:
            change = round(money_received - drink_cost, 2)
            print(f"Here is ${change} in change.")
            self.resources["money"] += drink_cost
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False

    def make_coffee(self, drink):
        """
        Make the selected drink and deduct the resources.

        Parameters:
        drink (str): The name of the drink to make.
        """
        for item in self.menu[drink]:
            if item != "cost":
                self.resources[item] -= self.menu[drink][item]
        print(f"Here is your {drink}. Enjoy!")

    def start(self):
        """
        Start the coffee machine and prompt the user for input.
        """
        is_on = True
        while is_on:
            choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
            if choice == "off":
                is_on = False
            elif choice == "report":
                self.report()
            elif choice in self.menu:
                if self.check_resources(choice):
                    payment = self.process_coins()
                    if self.transaction_successful(payment, self.menu[choice]["cost"]):
                        self.make_coffee(choice)
            else:
                print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    machine = CoffeeMachine()
    machine.start()
