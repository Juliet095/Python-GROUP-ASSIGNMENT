 #1.  Basic: Create a class called Car with attributes brand and color. Instantiate an object
# #  of the Car class and print its attributes.
class car: 
    def __init__(my_car,brand,color):
        my_car.brand = brand
        my_car.color = color
car2 = car("Vanguard","White")
print(car2.brand)
print(car2.color)
# # 2.  Intermediate: Add a method called start_engine to the Car class that prints a 
# # message saying the engine of the car has started. Create an instance of Car and call the method.

class car: 
    def __init__(my_car,brand,color):
        my_car.brand = brand
        my_car.color = color
    def start_engine(unbeilievable):
        print(f"The engine of the car has started")
car2 = car("Vanguard","White")
car2.start_engine()

# 3.    Advanced: Create a class called BankAccount with attributes account_number and balance. Add methods to:
#  Deposit an amount.
#  Withdraw an amount (only if sufficient balance exists).
# ○ Print the account balance.
class bank_account:
    def __init__(account1,account_number,balannce):
        account1.account_number = account_number
        account1.balance = balannce
    def deposit(account1,amount):
        if amount>0:
            account1.balance += amount
            print(f"{amount}. new balance: {account1.balance}")
        else:
            print(f"deposite amount must be positive not negative") 
    def withdraw (account1,amount):
        if amount >0:
            if amount <= account1.balance:
                account1.balance -= amount
                print(f"withdraw {amount}. new balance: {account1.balance}")
            else:
                print("insufficient balance and withdraw amount must be positive")
    def print_balance(account1):
        print(f"Account number: {account1.account_number}")
        print(f"Current balance: {account1.balance}")

# 4.    Challenge: Implement a class called Library that manages a collection of books.
#  Each book has a title, author, and available status. The Library class should have methods to:
#  Add a book to the library.
#  Remove a book from the library.
#  Check if a book is available by title.
#  Borrow a book (mark it as unavailable if it’s available).
#  Return a book (mark it as available again if it was borrowed)