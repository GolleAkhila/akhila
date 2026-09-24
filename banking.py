from abc import ABC, abstractmethod


# ==========================================
# Interface
# ==========================================

class BankOperations(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass


# ==========================================
# Abstract Class
# ==========================================

class BankAccount(BankOperations):

    def __init__(self, account_number, account_holder_name, balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__balance = balance

        self.transactions = []

        # Store account creation transaction
        self.transactions.append(
            f"Account created with balance: Rs.{balance}"
        )

    # Abstract method
    @abstractmethod
    def display_account_type(self):
        pass

    # Deposit
    def deposit(self, amount):

        if amount > 0:

            self.__balance = self.__balance + amount

            self.transactions.append(
                f"Deposited: Rs.{amount}"
            )

            print("Amount deposited successfully!")

        else:

            print("Invalid deposit amount!")

    # Withdraw
    def withdraw(self, amount):

        if amount > 0 and amount <= self.__balance:

            self.__balance = self.__balance - amount

            self.transactions.append(
                f"Withdrawn: Rs.{amount}"
            )

            print("Amount withdrawn successfully!")

        elif amount > self.__balance:

            print("Insufficient balance!")

        else:

            print("Invalid withdrawal amount!")

    # Check balance
    def check_balance(self):

        print(f"Current Balance: Rs.{self.__balance}")

    # Display account details
    def display_account_details(self):

        print("\n===== Account Details =====")

        print("Account Number:", self.__account_number)
        print("Account Holder:", self.__account_holder_name)
        print("Balance: Rs.", self.__balance)

    # Transaction history
    def show_transaction_history(self):

        print("\n===== Transaction History =====")

        for transaction in self.transactions:
            print(transaction)


# ==========================================
# Savings Account
# ==========================================

class SavingsAccount(BankAccount):

    def __init__(self, account_number, account_holder_name, balance):

        super().__init__(
            account_number,
            account_holder_name,
            balance
        )

    def display_account_type(self):

        print("Account Type: Savings Account")


# ==========================================
# Current Account
# ==========================================

class CurrentAccount(BankAccount):

    def __init__(self, account_number, account_holder_name, balance):

        super().__init__(
            account_number,
            account_holder_name,
            balance
        )

    def display_account_type(self):

        print("Account Type: Current Account")


# ==========================================
# Main Program
# ==========================================

print("\n================================")
print("     BANKING SYSTEM")
print("================================")


# ==========================================
# Create Account
# ==========================================

print("\n===== Create Account =====")

account_number = int(input("Enter account number: "))
account_holder_name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: Rs."))

print("\nSelect Account Type")
print("1. Savings Account")
print("2. Current Account")

account_type = int(input("Enter your choice: "))


if account_type == 1:

    account = SavingsAccount(
        account_number,
        account_holder_name,
        balance
    )

elif account_type == 2:

    account = CurrentAccount(
        account_number,
        account_holder_name,
        balance
    )

else:

    print("Invalid account type!")
    exit()


print("\nAccount created successfully!")


# ==========================================
# Menu
# ==========================================

while True:

    print("\n================================")
    print("     BANKING MANAGEMENT SYSTEM")
    print("================================")

    print("1. Display Account Details")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")

    choice = int(input("\nEnter your choice: "))


    # ======================================
    # Display Account Details
    # ======================================

    if choice == 1:

        account.display_account_type()
        account.display_account_details()


    # ======================================
    # Deposit Money
    # ======================================

    elif choice == 2:

        deposit_amount = float(
            input("Enter deposit amount: Rs.")
        )

        account.deposit(deposit_amount)


    # ======================================
    # Withdraw Money
    # ======================================

    elif choice == 3:

        withdraw_amount = float(
            input("Enter withdrawal amount: Rs.")
        )

        account.withdraw(withdraw_amount)


    # ======================================
    # Check Balance
    # ======================================

    elif choice == 4:

        account.check_balance()


    # ======================================
    # Transaction History
    # ======================================

    elif choice == 5:

        account.show_transaction_history()


    # ======================================
    # Exit
    # ======================================

    elif choice == 6:

        print(
            "Thank you for using Banking Management System!"
        )

        break


    # ======================================
    # Invalid Choice
    # ======================================

    else:

        print("Invalid choice! Please try again.")