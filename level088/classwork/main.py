balance = 1000
transactions = []
def check_balance():
    print(f"you have ${balance}")
def deposit(user_balance):
    while True:
        try:
            amount = input("enter how much would you like to deposit: ")
            if not amount.digit():
                print("deposit amount must be number")
                raise ValueError("deposit amount must be number")
            amont = float(amount)

            if amount <= 0:
                print("deposit amount has to be positive number")
                raise ValueError("deposit amount has to be positive number")
            
            new_balance = user_balance + amount
            check_balance(new_balance)
            return new_balance
        except:
            pass

def withdraw(user_balance):
    while True:
            try:
                amount = input("enter withdraw amount:")
                if not amount.isdigit():
                    print("deposit amount must be number")
                    raise ValueError("deposit amount must be number")
                amount = float(amount)

                if amount <= 0:
                    print("deposit amount has to be positive number")
                    raise ValueError("deposit amount has to be positive number")
                
                new_balance = user_balance + amount
                check_balance(new_balance)
                return new_balance
            except:
                pass
def main():
    while True:
        try:
            print("welcome ATM!")

            print("1. check balance")
            print("2. deposit")
            print("3. withdraw")
            print("4. last 5 transactions")
            print("5. exit the ATM")

            option = input("pick operation (1-5): ")

            if not option.isdigit():
                print("must enter a valid operation number")
                raise ValueError("must enter a valid operation number")
            option = int(option)

            if option == 1:
                check_balance(balance)
            elif option == 2:
                new_balance = deposit(balance)
                balance = new_balance
                check_balance(balance)
            elif option == 3:
                new_balance = withdraw(balance)
                balance = new_balance
                check_balance(balance)
            elif option == 4:
                pass
            elif option == 5:
                print("thank you for using our service")
                print("system shuting down")
                return
            else:
                print("invalid operation")
                raise ValueError("ivalid operation")    
        except:
            pass