import csv

class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def transfer(self, amount, target_account):
        if self.withdraw(amount):
            target_account.deposit(amount)
            return True
        return False

    def __repr__(self):
        return f"Account(name={self.name}, balance={self.balance})"


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, balance=0):
        if name in self.accounts:
            return False
        self.accounts[name] = Account(name, balance)
        return True

    def get_account(self, name):
        return self.accounts.get(name)

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['name', 'balance'])
            for account in self.accounts.values():
                writer.writerow([account.name, account.balance])

    def load_from_csv(self, filename):
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            self.accounts = {}
            for row in reader:
                self.create_account(row['name'], float(row['balance']))

# Example usage
if __name__ == "__main__":
    bank = BankSystem()
    bank.create_account("Alice", 100)
    bank.create_account("Bob", 50)

    alice_account = bank.get_account("Alice")
    bob_account = bank.get_account("Bob")

    alice_account.deposit(50)
    alice_account.withdraw(30)
    alice_account.transfer(50, bob_account)

    bank.save_to_csv("bank_data.csv")

    # Load the bank system state from CSV
    new_bank = BankSystem()
    new_bank.load_from_csv("bank_data.csv")
    print(new_bank.accounts)
