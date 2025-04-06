class Resource:
    """
    A class to represent a resource.
    """

    def __init__(self, name, amount):
        """
        Initialize the resource with a name and amount.

        Parameters:
        name (str): The name of the resource.
        amount (int): The amount of the resource.
        """
        self.name = name
        self.amount = amount

    def __str__(self):
        """
        Return a string representation of the resource.

        Returns:
        str: The string representation of the resource.
        """
        return f"{self.name}: {self.amount}"
    
class Recipe:
    """
    A class to represent a recipe.
    """

    def __init__(self, name, ingredients, cost):
        """
        Initialize the recipe with a name, ingredients, and cost.

        Parameters:
        name (str): The name of the recipe.
        ingredients (dict): The ingredients required for the recipe.
        cost (float): The cost of the recipe.
        """
        self.name = name
        self.ingredients = ingredients
        self.cost = cost

    def __str__(self):
        """
        Return a string representation of the recipe.

        Returns:
        str: The string representation of the recipe.
        """
        return f"{self.name}: {self.ingredients}, Cost: {self.cost}"
    
class CoffeeMachine:
    """
    A class to represent a coffee machine.
    """

    def __init__(self):
        """
        Initialize the coffee machine with resources and menu.
        """
        self.resources = [
            Resource("water", 300),
            Resource("milk", 200),
            Resource("coffee", 100),
            Resource("money", 0.0)
        ]
        self.menu = [
            Recipe("espresso", {"water": 50, "milk": 0, "coffee": 18}, 1.5),
            Recipe("latte", {"water": 200, "milk": 150, "coffee": 24}, 2.5),
            Recipe("cappuccino", {"water": 250, "milk": 100, "coffee": 24}, 3.0)
        ]

    def report(self):
        """
        Print the current resource values of the coffee machine.
        """
        for resource in self.resources:
            if resource.name == "money":
                print(f"Money: ${resource.amount}")
            else:
                print(f"{resource.name.capitalize()}: {resource.amount}ml")

    def check_resources(self, drink):
        """
        Check if there are enough resources to make the selected drink.

        Parameters:
        drink (str): The name of the drink to check resources for.

        Returns:
        bool: True if there are enough resources, False otherwise.
        """
        for item in self.menu:
            if item.name == drink:
                for ingredient, amount in item.ingredients.items():
                    for resource in self.resources:
                        if resource.name == ingredient and resource.amount < amount:
                            print(f"Sorry there is not enough {ingredient}.")
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
            for resource in self.resources:
                if resource.name == "money":
                    resource.amount += drink_cost
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
        for item in self.menu:
            if item.name == drink:
                for ingredient, amount in item.ingredients.items():
                    for resource in self.resources:
                        if resource.name == ingredient:
                            resource.amount -= amount
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
            elif choice in [item.name for item in self.menu]:
                if self.check_resources(choice):
                    payment = self.process_coins()
                    if self.transaction_successful(payment, next(item.cost for item in self.menu if item.name == choice)):
                        self.make_coffee(choice)
            else:
                print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    machine = CoffeeMachine()
    machine.start()
