from tkinter import Tk, Label, Button, StringVar, OptionMenu, Entry, messagebox
# import tkinter as tk


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


class Storage:
    """
    A class to represent a storage.
    """

    def __init__(self):
        """
        Initialize the storage with resources.
        """
        self.resources = [
            Resource("water", 300),
            Resource("milk", 200),
            Resource("coffee", 100),
            Resource("money", 0.0)
        ]

    def has_enough_resource(self, resource_name, amount):
        """
        Check if there is enough resource.

        Parameters:
        resource_name (str): The name of the resource.
        amount (int): The amount of the resource to check.

        Returns:
        bool: True if there is enough resource, False otherwise.
        """
        for resource in self.resources:
            if resource.name == resource_name:
                return resource.amount >= amount
        return False

    def deduct_resource(self, resource_name, amount):
        """
        Deduct the resource amount.

        Parameters:
        resource_name (str): The name of the resource.
        amount (int): The amount of the resource to deduct.
        """
        for resource in self.resources:
            if resource.name == resource_name:
                resource.amount -= amount
                break


class Recipe:
    """
    A class to represent a recipe.
    """

    def __init__(self, name, ingredients, cost):
        """
        Initialize the recipe with a name, ingredients, and cost.

        Parameters:
        name (str): The name of the recipe.
        ingredients (list): A list of Resource objects required for the recipe.
        cost (float): The cost of the recipe.
        """
        self.name = name
        self.ingredients = [Resource(name, amount) for name, amount in ingredients.items()]
        self.cost = cost

    def __str__(self):
        """
        Return a string representation of the recipe.

        Returns:
        str: The string representation of the recipe.
        """
        ingredients_str = ", ".join([str(ingredient) for ingredient in self.ingredients])
        return f"{self.name}: {ingredients_str}, Cost: {self.cost}"


class CoffeeMachine:
    """
    A class to represent a coffee machine.
    """

    def __init__(self):
        """
        Initialize the coffee machine with storage and menu.
        """
        self.storage = Storage()  # Use Storage class for resources
        self.menu = [
            Recipe("espresso", {"water": 50, "milk": 0, "coffee": 18}, 1.5),
            Recipe("latte", {"water": 200, "milk": 150, "coffee": 24}, 2.5),
            Recipe("cappuccino", {"water": 250, "milk": 100, "coffee": 24}, 3.0)
        ]

    def report(self):
        """
        Print the current resource values of the coffee machine.
        """
        for resource in self.storage.resources:  # Access resources from storage
            if resource.name == "money":
                print(f"Money: ${resource.amount}")
            else:
                print(f"{resource.name.capitalize()}: {resource.amount}ml")

    def get_report(self):
        """
        Generate the current resource values of the coffee machine as a string.

        Returns:
        str: The current resource values.
        """
        report = ""
        for resource in self.storage.resources:  # Access resources from storage
            if resource.name == "money":
                report += f"Money: ${resource.amount}\n"
            else:
                report += f"{resource.name.capitalize()}: {resource.amount}ml\n"
        return report

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
                for ingredient in item.ingredients:
                    if not self.storage.has_enough_resource(ingredient.name, ingredient.amount):
                        print(f"Sorry there is not enough {ingredient.name}.")
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
            self.storage.deduct_resource("money", -drink_cost)  # Add money to storage
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
                for ingredient in item.ingredients:
                    self.storage.deduct_resource(ingredient.name, ingredient.amount)
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


class CoffeeMachineUI:
    """
    A class to represent the Coffee Machine UI.
    """

    def __init__(self, coffee_machine):
        """
        Initialize the Coffee Machine UI.

        Parameters:
        coffee_machine (CoffeeMachine): The CoffeeMachine instance to interact with.
        """
        self.coffee_machine = coffee_machine
        self.window = Tk()
        self.window.title("Coffee Machine")

        # Dropdown menu for drink selection
        self.selected_drink = StringVar(self.window)
        self.selected_drink.set("Select a drink")
        self.drink_menu = OptionMenu(self.window, self.selected_drink, *[item.name for item in coffee_machine.menu])
        self.drink_menu.grid(row=0, column=0, columnspan=2, pady=10)

        # Coin inputs
        Label(self.window, text="Quarters:").grid(row=1, column=0)
        self.quarters_input = Entry(self.window)
        self.quarters_input.grid(row=1, column=1)

        Label(self.window, text="Dimes:").grid(row=2, column=0)
        self.dimes_input = Entry(self.window)
        self.dimes_input.grid(row=2, column=1)

        Label(self.window, text="Nickles:").grid(row=3, column=0)
        self.nickles_input = Entry(self.window)
        self.nickles_input.grid(row=3, column=1)

        Label(self.window, text="Pennies:").grid(row=4, column=0)
        self.pennies_input = Entry(self.window)
        self.pennies_input.grid(row=4, column=1)

        # Pay button
        self.pay_button = Button(self.window, text="Pay", command=self.process_payment)
        self.pay_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Report button
        self.report_button = Button(self.window, text="Report", command=self.show_report)
        self.report_button.grid(row=6, column=0, columnspan=2, pady=10)

    def process_payment(self):
        """
        Process the payment and make the selected drink.
        """
        drink = self.selected_drink.get()
        if drink == "Select a drink":
            messagebox.showerror("Error", "Please select a drink.")
            return

        try:
            quarters = int(self.quarters_input.get() or 0)
            dimes = int(self.dimes_input.get() or 0)
            nickles = int(self.nickles_input.get() or 0)
            pennies = int(self.pennies_input.get() or 0)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid coin amounts.")
            return

        total_money = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

        if self.coffee_machine.check_resources(drink):
            drink_cost = next(item.cost for item in self.coffee_machine.menu if item.name == drink)
            if self.coffee_machine.transaction_successful(total_money, drink_cost):
                self.coffee_machine.make_coffee(drink)
                messagebox.showinfo("Success", f"Here is your {drink}. Enjoy!")
            else:
                messagebox.showerror("Error", "Not enough money. Money refunded.")
        else:
            messagebox.showerror("Error", f"Not enough resources to make {drink}.")

    def show_report(self):
        """
        Display the current resource report in a popup.
        """
        report = self.coffee_machine.get_report()
        messagebox.showinfo("Report", report)

    def run(self):
        """
        Run the Coffee Machine UI.
        """
        self.window.mainloop()


if __name__ == "__main__":
    machine = CoffeeMachine()
    ui = CoffeeMachineUI(machine)
    ui.run()

