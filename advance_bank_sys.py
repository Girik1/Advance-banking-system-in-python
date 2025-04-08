class BankAccount:
    def __init__(self, account_holder, account_number, initial_balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited {amount}")
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew {amount}")
            return True
        return False

    def transfer(self, amount, recipient_account):
        if self.withdraw(amount):
            recipient_account.deposit(amount)
            self.transactions.append(f"Transferred {amount} to account {recipient_account.account_number}")
            return True
        return False

    def get_balance(self):
        return self.balance

    def print_statement(self):
        print(f"Account Statement for {self.account_holder} ({self.account_number})")
        for transaction in self.transactions:
            print(transaction)
        print(f"Current Balance: {self.balance}\n")

class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_holder, initial_balance=0):
        account_number = len(self.accounts) + 1
        account = BankAccount(account_holder, account_number, initial_balance)
        self.accounts[account_number] = account
        print(f"Account for {account_holder} created with account number {account_number}")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def show_account_details(self, account_number):
        account = self.get_account(account_number)
        if account:
            account.print_statement()
        else:
            print("Account not found.")

    def process_transaction(self, from_account_number, to_account_number, amount):
        sender = self.get_account(from_account_number)
        recipient = self.get_account(to_account_number)

        if sender and recipient:
            if sender.transfer(amount, recipient):
                print(f"Transfer of {amount} from account {from_account_number} to {to_account_number} successful.")
            else:
                print("Transfer failed. Insufficient funds.")
        else:
            print("Invalid account details.")

# Example usage
if __name__ == "__main__":
    bank_system = BankSystem()

    bank_system.create_account("Alice", 500)
    bank_system.create_account("Bob", 1000)

    alice_account = bank_system.get_account(1)
    bob_account = bank_system.get_account(2)

    bank_system.show_account_details(1)
    bank_system.show_account_details(2)

    # Alice makes a deposit
    alice_account.deposit(200)
    bank_system.show_account_details(1)

    # Bob withdraws money
    bob_account.withdraw(150)
    bank_system.show_account_details(2)

    # Alice transfers money to Bob
    bank_system.process_transaction(1, 2, 100)
    bank_system.show_account_details(1)
    bank_system.show_account_details(2)
