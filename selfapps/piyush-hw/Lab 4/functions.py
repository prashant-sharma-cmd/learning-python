import time, sys, random

CUSTOMERS_RECORD_FILE = "customers.txt"
TRANSACTION_RECORD_FILE = "transactions.txt"

def create_files():
    file = open(CUSTOMERS_RECORD_FILE, "a")
    file.close()
    file = open(TRANSACTION_RECORD_FILE, "a")
    file.close()

def check_credentials(name, acc_num):
    try:
        with open(CUSTOMERS_RECORD_FILE, "r") as file:
            customers = file.readlines()
            dict = {}
        for item in customers:
            customer = item.split(",")
            dict[customer[1]] = customer[0]
        if acc_num in dict.keys():
            print(f"{name}, Successfully logged in!")
            return acc_num
        else:
            print(f"Sorry, the account number you entered is invalid.")
            response = input("Do you want to create new account? (y/n): ")
            if response == "y":
                while True:
                    acc_num = str(random.randint(10000000, 999999999999))
                    if acc_num not in dict.keys():
                        break
                create_new_account(name, acc_num)
                print(f"Your account details are:\nName: {name}\n"
                      f"Account Number: {acc_num}\n"
                      f"Account Balance: 0")
                return acc_num
            else:
                sys.exit("You can't run other commands without account")
    except FileNotFoundError:
        print("Sorry the database is down for now")
        return None
    except PermissionError:
        print("Sorry you don't have permission to access the file!!")
        return None
    except IOError:
        print("An error occurred while reading the file!")
        return  None


def create_new_account(account_name, account_number):
    try:
        with open(CUSTOMERS_RECORD_FILE, "a") as file:
            file.write(account_name + "," + str(account_number) + ",0" + "\n")
            print("New account created successfully!")
    except FileNotFoundError:
        print("Sorry the database is down for now")
    except PermissionError:
        print("Sorry you don't have permission to access the file!!")
    except IOError:
        print("An error occurred while reading the file!")

def make_deposits(account_number, amount):
    try:
        with open(CUSTOMERS_RECORD_FILE, "r") as file:
            content = file.readlines()
        for index, item in enumerate(content):
            record = item.split(",")
            if record[1] == account_number:
                content.pop(index)
                new_balance = int(record[2]) + amount
                new_record = f"{record[0]},{record[1]},{new_balance}\n"
                content.append(new_record)
                with open(TRANSACTION_RECORD_FILE, "a") as file:
                    current_time = time.strftime("%d/%m/%Y %H:%M:%S")
                    log = f"{record[1]}: Made deposit of {amount}, {current_time}\n"
                    file.write(log)
                    print("Transaction Completed Successfully!")
        with open(CUSTOMERS_RECORD_FILE, "w") as file:
            file.writelines(content)
    except FileNotFoundError:
        print("Sorry the database is down for now")
    except PermissionError:
        print("Sorry you don't have permission to access the file!!")
    except IOError:
        print("An error occurred while reading the file!")


def make_withdrawal(account_number, amount):
    try:
        with open(CUSTOMERS_RECORD_FILE, "r") as file:
            content = file.readlines()
        for index, item in enumerate(content):
            record = item.split(",")
            if record[1] == account_number:
                content.pop(index)
                if int(record[2])>amount:
                    new_balance = int(record[2]) - amount
                else:
                    print("Not enough money!")
                new_record = f"{record[0]},{record[1]},{new_balance}\n"
                content.append(new_record)
                with open(TRANSACTION_RECORD_FILE, "a") as file:
                    current_time = time.strftime("%d/%m/%Y %H:%M:%S")
                    log = f"{record[1]}: Made withdrawal of {amount}, {current_time}\n"
                    file.write(log)
                    print("Transaction Completed Successfully!")
        with open(CUSTOMERS_RECORD_FILE, "w") as file:
            file.writelines(content)
    except FileNotFoundError:
        print("Sorry the database is down for now")
    except PermissionError:
        print("Sorry you don't have permission to access the file!!")
    except IOError:
        print("An error occurred while reading the file!")


def check_balance(account_number):
    try:
        with open(CUSTOMERS_RECORD_FILE, "r") as file:
            content = file.readlines()
        for index, item in enumerate(content):
            record = item.split(",")
            if record[1] == account_number:
                print(f"Your current balance is {record[2]}")
    except FileNotFoundError:
        print("Sorry the database is down for now")
    except PermissionError:
        print("Sorry you don't have permission to access the file!!")
    except IOError:
        print("An error occurred while reading the file!")


