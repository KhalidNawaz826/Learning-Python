class Atm:
    def __init__(self) :
        self.pin = ""
        self.balance = 0

        self.menue()
    
    def menue(self):
        temp = input('''
               Hello, How you want to proceed?
               1. Enter one to create pin
               2. Enter two to deposit balance
               3. Enter three to withdraw balance
               4. Enter four to check balance
               5. Enter five to exit

''')
        if temp == "1":
            self.creat_pin()
        elif temp == "2":
            self.deposit()
        elif temp == "3":
            self.withdraw()
        elif temp == "4":
            self.check_balance()
        else:
            print("Bye")
    def creat_pin(self):
        self.pin = input("Enter your pin")
        print("Pin set successfully")
        self.menue()

    def deposit(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter your balance"))
            self.balance += amount
            print(f"{amount} Deposit Successfully\n{self.balance} is your current balance")
            self.menue()
        else:
            print("Invalid pin")
            self.menue()
    
    def withdraw(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter your balance"))
            if amount < 0:
                print("Invalid Amount")
                self.menue()
            elif amount <= self.balance:
                self.balance -= amount
                print(f"{amount} withdraw successfully\n{self.balance} Current balance")
                self.menue()
            else:
                print("Insufficient Balance")
                self.menue()
    
    def check_balance(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            print(f"Current Balance: {self.balance}")
            self.menue()
    
  

            



khalid = Atm()
furqan = Atm()
balance01 = khalid.balance
balance02 = furqan.balance
print(f"Furqan Account balance: {balance02}\nKhalid Account Balance: {balance01}")