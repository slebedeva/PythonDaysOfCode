# Create a class representing a simple bank account with deposit and withdraw methods

# TODO: add customer id

class BankAccount:
    """ A simple bank account. Has deposit and withdraw methods."""
    def __init__(self, total=0) -> None:
        self.total = total
    def deposit(self, amount):
        self.total += amount
    def withdraw(self, amount):
        total -= amount
