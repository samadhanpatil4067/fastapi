def add(num1: int, num2: int):
    return num1 + num2

def subtract(num1: int, num2: int):
    return num1 - num2

class BankAccount:
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance
    
    def collect_interest(self):
        self.balance *= 1.1  # 1% interest rate