from functions import *

print("\nWelcome to our Bank!\n")
name = input("Please, Enter your name:  ")
acc_num = input("Please, Enter your account number:  ")

create_files()
acc_num = check_credentials(name, acc_num)

while True:
    action = input("What do you want to do:\nType d for deposits\nType w for withdrawal\n"
                   "Type b to check balance\nType q to quit: ")
    if action == "d":
        amount = int(input("How much do you want to deposit: "))
        make_deposits(acc_num, amount)
    elif action == "w":
        amount = int(input("How much do you want to withdraw: "))
        make_withdrawal(acc_num, amount)
    elif action == "b":
        check_balance(acc_num)
    elif action == "q":
        print("Bye bye!")
        break






