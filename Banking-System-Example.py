accounts = []

def createAccount():
   # Start with a balance of 0
   # Return the new account ID
    pass

def deposit(account_id, amount):
    # Complete this function to add the amount to the balance
    pass

def withdraw(account_id, amount):
    # Partner 2: Complete this function to subtract the amount from the balance
    pass

def display_balance(account_id):
    print(f"Current balance: ${accounts[account_id]}")


while True:
        print("1. Create account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
    
        choice = int(input("Enter choice: "))

        if choice == 1:
            # Create new account
            
        elif choice == 2:
            # Deposit to account
            
        elif choice == 3:
            # Withdraw from account
            
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")
