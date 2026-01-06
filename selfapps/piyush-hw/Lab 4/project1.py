FILENAME = "contacts.txt"

while True:
    action = input("What do you want to do? (add, view, search, exit) ")

    if action == "add":
        name = input("What is your name?")
        phone = input("What is your phone number?")
        try:
            with open(FILENAME, "a") as file:
                file.writelines(name.title() + "," + phone + "\n")
            print("Successfully Added!!")
        except FileNotFoundError:
            print("Sorry the database file isn't available")
        except PermissionError:
            print("Sorry you don't have permission to access the file!!")
        except IOError:
            print("An error occurred while reading the file!")

    if action == "view":
        try:
            with open(FILENAME, "r") as file:
                content = file.readlines()
            for item in content:
                name = item.split(",")[0]
                phone = item.split(",")[1]
                print(f"Name: {name}\nContact Number: {phone}")
        except FileNotFoundError:
            print("Sorry the database file isn't available")
        except PermissionError:
            print("Sorry you don't have permission to access the file!!")
        except IOError:
            print("An error occurred while reading the file!")

    if action == "search":
        search = input("Enter person's whose contact you want: ")
        try:
            with open(FILENAME, "r") as file:
                content = file.readlines()
            for item in content:
                name = item.split(",")[0]
                phone = item.split(",")[1]
                if search.lower() in name.lower():
                    print(f"{name.strip()} : {phone}")
                    response = input("Is this the correct person(y/n)? ")
                    if response == "y":
                        break
        except FileNotFoundError:
            print("Sorry the database file isn't available")
        except PermissionError:
            print("Sorry you don't have permission to access the file!!")
        except IOError:
            print("An error occurred while reading the file!")

    if action=="exit":
        print("Bye bye!")
        break
s



