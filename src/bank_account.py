"""
Module: bank_account.py
Author: David Huang

This module defines a BankAccount class for managing bank accounts.
"""

class BankAccount:
    """
    A class representing a bank account.
    """

    def __init__(self, account_number, balance):
        """
        Initialize the BankAccount object with account number and balance.
        """
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """
        Deposit the specified amount into the account.
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        """
        Withdraw the specified amount from the account.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount for withdrawal.")

    def display_balance(self):
        """
        Display the current balance and account number.
        """
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance}")


if __name__ == "__main__":
    account1 = BankAccount("123456789", 1000)
    account1.display_balance()
    account1.deposit(500)
    account1.withdraw(200)
    account1.display_balance()
