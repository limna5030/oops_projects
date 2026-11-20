from abc import ABC, abstractmethod
class balanceexception(Exception):
    pass

class BankAccount(ABC):
    def __init__(self, account_name, amount):
        if amount < 0:
            raise ValueError("The opening balance cannot be negative.")
        self.__name = account_name
        self.__balance = amount
        self.__transactions = []

    @property
    @abstractmethod
    def account_type(self):
        pass

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("The deposit amount must be positive.")
        self.__balance += amount
        self.__transactions.append(("deposit", amount, self.__balance))
    def viable(self,amount):
        if self.__balance>=amount:
            return
        else:
            raise balanceexception("\ninsufficient balance\n")

    def withdraw(self, amount):
        try:
            self.viable(amount)
            
        
            self.__balance -= amount
            self.__transactions.append(("withdrawal", amount, self.__balance))
        except balanceexception as e:
            print(f"withdrawal interrupted: {e}")

    def get_transactions(self):
        return tuple(self.__transactions)


class SavingsAccount(BankAccount):
    @property
    def account_type(self):
        return "Savings"


class CheckingAccount(BankAccount):
    @property
    def account_type(self):
        return "Checking"


