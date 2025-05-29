registeredMembers = "Event Registration System/registeredMembers.txt"
waitlistMembers = "Event Registration System/waitlistMembers.txt"
size = 5

def listLoad(filename):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []
    
def listSave(filename, data_list):
    with open(filename, "w") as file:
        for name in data_list:
            file.write(name + " \n")

def fileSave(filename, name):
    with open(filename, "a") as file:
        file.write(name + " \n")

def registeredGuests(registered, waitlist):
    name = input("Enter the guest's full name to register them: ").strip()

    if name in registered:
        print("This guest has already been registered.")
        return
    elif name in waitlist:
        print("This guest is currently in the waitlist.")
        return

    if len(registered) < size:
        registered.append(name)
        fileSave(registeredMembers, name)
        print(f"{name} is registered.")
    else:
        waitlist.append(name)
        fileSave(waitlistMembers, name)
        print(f"{name} has been placed in the waitlist.")

def listDisplay(registered, waitlist):
    print("\n Registered Guests: ")
    for i, name in enumerate(registered, 1):
        print(f"{i}, {name}")

    print("\n Waitlisted Guests: ")
    for i, name in enumerate(waitlist, 1):
        print(f"{i}, {name}")

def sizeChange():
    global size
    try:
        newSize = int(input(f"The Max Capacity is currently: {size}. What would you like the new Max Capacity to be: "))
        if newSize > 0:
            size = newSize
            print(f"The new Maximum Capacity is {size}.")
        else:
            print("The current Maximum Capacity is too low. Please choose a number above 0.")
    except ValueError:
        print("Not a Valid Value.")

def deleteGuest(registered, waitlist):
    name =input("Which guest would you like to remove: ").strip()

    if name in registered:
        registered.remove(name)
        listSave(registeredMembers, registered)
        print(f"{name} was removed from the Registered List.")
    elif name in waitlist:
        waitlist.remove(name)
        listSave(waitlistMembers, waitlist)
        print(f"{name} was removed from the Waitlist.")
    else:
        print("The following name is in neither the Registered or Waitlist.")

def bumpUp(registered, waitlist):
    if len(registered) >= size:
        print("The registed list is current at maximum capacity. Remove someone in order to perform this action.")
    elif not waitlist:
        print("There is no one currently in the waitlist.")
    else:
        bumped = waitlist.pop(0)
        registered.append(bumped)
        listSave(registeredMembers, registered)
        listSave(waitlistMembers, waitlist)
        print(f"{bumped} was bumped up from the waitlist to the registered list.")

def menu():
    global size
    registered = listLoad(registeredMembers)
    waitlist = listLoad(waitlistMembers)

    while True:
        print("\nEvent Registration\n")
        print("1. Register Guest")
        print("2. Display Lists [Register & Waitlist]")
        print("3. Change Maximum Capacity")
        print("4. Remove Guest")
        print("5. Change Guest status from Waitlist to Register")
        print("6. Exit")
        option = input("Choose one of the options below (1 - 6): ")

        if option == "1":
            registeredGuests(registered, waitlist)
        elif option == "2":
            listDisplay(registered, waitlist)
        elif option == "3":
            sizeChange()
        elif option == "4":
            deleteGuest(registered, waitlist)
        elif option == "5":
            bumpUp(registered, waitlist)
        elif option == "6":
            print("Exited. ")
            break
        else:
            print("Invalid Option, Please type a number between [1 - 6]")

if __name__ == "__main__":
    menu()

