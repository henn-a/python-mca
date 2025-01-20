class BankAccount:
    def __init__(self, account_number, name, account_type, balance=0):
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

# Example usage:
account_number = input("Enter account number: ")
name = input("Enter account holder's name: ")
account_type = input("Enter account type (e.g., Savings/Current): ")
initial_balance = float(input("Enter initial balance: "))

# Create a BankAccount object
account = BankAccount(account_number, name, account_type, initial_balance)

# Deposit and withdraw operations
deposit_amount = float(input("Enter amount to deposit: "))
account.deposit(deposit_amount)

withdraw_amount = float(input("Enter amount to withdraw: "))
account.withdraw(withdraw_amount)
