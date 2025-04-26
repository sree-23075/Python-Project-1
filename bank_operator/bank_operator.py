from account.user import User
from account.bank_account import BankAccount, SavingsAccount, CurrentAccount, StudentAccount
from rich.console import Console

console = Console()

users = []

def create_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    user = User(name, email)

    if not user.is_valid_email(email):
        print("Invalid email address!")
        return  # ❗ Do not create user if email invalid
    
    users.append(user)
    print(f"✅ User '{name}' created successfully.\n")

def list_users():
    if not users:
        console.print("[bold red]No users found. Please create a user first.[/bold red]")
        return False
    
    for i, user in enumerate(users):
        print(f"{i+1}. {user}")
    return True

def create_account():
    global users

    if not list_users():
        return

    try:
        idx = int(input("Select user number: ")) - 1
        if idx < 0 or idx >= len(users):
            print("Invalid user selection.\n")
            return

        print("Account Type:")
        print("1. Savings Account")
        print("2. Student Account")
        print("3. Current Account")
        
        account_choice = int(input("Enter your choice (1, 2, 3): "))
        amount = float(input("Enter initial deposit: "))

        if account_choice == 1:
            account = SavingsAccount(amount)
        elif account_choice == 2:
            account = StudentAccount(amount)
        elif account_choice == 3:
            account = CurrentAccount(amount)
        else:
            print("Invalid account type selection!\n")
            return

        users[idx].add_account(account)
        print(f"✅ {account.get_account_type()} created successfully!\n")
    
    except ValueError:
        print("Invalid input. Please enter numbers only.\n")

def deposit_money():
    global users

    if not list_users():
        return

    try:
        idx = int(input("Select user: ")) - 1
        if idx < 0 or idx >= len(users):
            print("Invalid user selection.\n")
            return

        user = users[idx]

        if not user.accounts:
            print("This user has no accounts.\n")
            return

        for i, acc in enumerate(user.accounts):
            print(f"{i+1}. Balance: Rs. {acc.get_balance()} ({acc.get_account_type()})")

        acc_idx = int(input("Select account: ")) - 1
        if acc_idx < 0 or acc_idx >= len(user.accounts):
            print("Invalid account selection.\n")
            return

        amount = float(input("Enter amount to deposit: "))
        user.accounts[acc_idx].deposit(amount)
        print("✅ Deposit successful!\n")
    
    except ValueError:
        print("Invalid input. Please enter numbers only.\n")

def withdraw_money():
    global users

    if not list_users():
        return

    try:
        idx = int(input("Select user: ")) - 1
        if idx < 0 or idx >= len(users):
            print("Invalid user selection.\n")
            return

        user = users[idx]

        if not user.accounts:
            print("This user has no accounts.\n")
            return

        for i, acc in enumerate(user.accounts):
            print(f"{i+1}. Balance: Rs. {acc.get_balance()} ({acc.get_account_type()})")

        acc_idx = int(input("Select account: ")) - 1
        if acc_idx < 0 or acc_idx >= len(user.accounts):
            print("Invalid account selection.\n")
            return

        amount = float(input("Enter amount to withdraw: "))
        try:
            user.accounts[acc_idx].withdraw(amount)
            print("✅ Withdrawal successful!\n")
        except ValueError as e:
            print(f"Error: {e}\n")

    except ValueError:
        print("Invalid input. Please enter numbers only.\n")

def view_transactions():
    global users

    if not list_users():
        return

    try:
        idx = int(input("Select user: ")) - 1
        if idx < 0 or idx >= len(users):
            print("Invalid user selection.\n")
            return

        user = users[idx]

        if not user.accounts:
            print("This user has no accounts.\n")
            return

        for i, acc in enumerate(user.accounts):
            print(f"\n{acc.get_account_type()} {i+1} - Balance: Rs. {acc.get_balance()}")
            if acc.get_transaction_history():
                for tx in acc.get_transaction_history():
                    print(f"    {tx}")
            else:
                print("    No transactions yet.")

    except ValueError:
        print("Invalid input. Please enter numbers only.\n")
