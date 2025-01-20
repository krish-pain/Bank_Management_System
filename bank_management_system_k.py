class BankAccount:
    def __init__(self, account_number, account_name, balance=0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal successful. New balance: {self.balance}")
        else:
            print("Insufficient balance.")

    def display_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Name: {self.account_name}")
        print(f"Balance: {self.balance}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_name, balance=0):
        if account_number in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[account_number] = BankAccount(account_number, account_name, balance)
            print("Account created successfully.")

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print("Account deleted successfully.")
        else:
            print("Account does not exist.")

    def access_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print("Account does not exist.")
            return None

def main():
    bank = Bank()

    while True:
        print("\nBank Management System")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. Access Account")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter account number: ")
            account_name = input("Enter account name: ")
            balance = float(input("Enter initial balance (default=0): ") or 0)
            bank.create_account(account_number, account_name, balance)
        elif choice == "2":
            account_number = input("Enter account number: ")
            bank.delete_account(account_number)
        elif choice == "3":
            account_number = input("Enter account number: ")
            account = bank.access_account(account_number)
            if account:
                while True:
                    print("\nAccount Options")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Display Details")
                    print("4. Back")

                    choice = input("Enter your choice: ")

                    if choice == "1":
                        amount = float(input("Enter amount to deposit: "))
                        account.deposit(amount)
                    elif choice == "2":
                        amount = float(input("Enter amount to withdraw: "))
                        account.withdraw(amount)
                    elif choice == "3":
                        account.display_details()
                    elif choice == "4":
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
