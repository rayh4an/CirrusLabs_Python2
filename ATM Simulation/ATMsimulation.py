import os

accounts = {
    "7232": {"name": "Rayhaan Mohamed", "balance": 1620.24},
    "4163": {"name": "John Smith", "balance": 3607.28},
    "9481": {"name": "Sara Mills", "balance": 4981.06},
    "9644": {"name": "Arib Hungerman", "balance": 6347.42},
    "3783": {"name": "Drew Talon", "balance": 6441.25},
    "6601": {"name": "Patches Last", "balance": 6527.92},
    "3370": {"name": "Heather Star", "balance": 7098.57},
    "5705": {"name": "Marika Freed", "balance": 7718.02},
}

class UserAccouts:
    def __init__(self, pin):
        self.pin = pin
        self.name = accounts[pin]["name"]
        self.balance = accounts[pin]["balance"]

    def currentBalance(self):
        print(f"Your Current Balance is ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print(f"You Deposit ${amount:.2f}. Your New Balance is ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("You unfortunatly have insufficent funds.")
        else:
            self.balance -= amount
            print(f"You Witdrew ${amount:.2f}. Your New Balance is ${self.balance:.2f}")
            
    def exit(self):
        accounts[self.pin]["balance"] = self.balance

def atm():
    pin = input("\nATM\nPlease enter in your 4 Digit PIN.   ")
    
    if pin not in accounts:
        print("Invalid PIN")
        return
    
    user = UserAccouts(pin)
    print(f"Welcome {user.name}!")

    while True:
        print("\nSelect on of the options Below:")
        print("1) Check Balance")
        print("2) Deposit Amount")
        print("3) Withdraw Amount")
        print("4) Exit & Log Out")

        option = input("Enter Option: ")

        if option == "1":
            user.currentBalance()
        elif option == "2":
            amount = float(input("How much money would you like to Deposit?"))
            user.deposit(amount)
        elif option == "3":
            amount = float(input("How much money would you like to Withdraw?"))
            user.withdraw(amount)
        elif option == "4":
            user.exit()
            print("Logged Out")
            break
        else:
            print("Invalid Option Selected, Try Again.")

if __name__ == "__main__":
    atm()