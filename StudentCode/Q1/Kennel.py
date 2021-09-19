from Dog import Dog
from SmallDog import SmallDog
from BigDog import BigDog

dogs = []
unit = 0

def AddDog():
    name = input("Please enter the dog's name:\n")
    weight = input("Please enter the dog's weight:\n")
    days = input("Please enter the number of days the Dog will stay:\n")

    if float(weight) < 10:
        x = SmallDog(name, weight, days)
    else:
        age = input("Please Input the Dog's age:\n")
        x = BigDog(name, weight, days, age)

    global unit
    if unit + x.unit <= 15:
        dogs.append(x)
        unit += x.unit
        print(x.name + " is added successfully!\nYou owe $" + str(x.getCost()) + '\n')
    else:
        print("Sorry, not enough space for " + x.name + '\n')

def RemoveDog():
    name = input("Enter the name of the dog you wish to remove:\n")
    print("Removing " + name + " from the kennel")
    global unit
    for i in dogs:
        if i.name == name:
            unit -= i.unit
            dogs.remove(i)
            print("Successful removal\n")
            return
    print("Removal failed, could not find dog.\n")
            
    

def printList():
    print("Dogs currently here are:")
    for i in dogs:
        print("Name: " + i.name + "  Weight: " + i.weight + "  Days: " + i.days + "  Senior: " + str(i.isSenior()))
    print()


#main()
option = ''
while option != 'Q':
    option = input("select an option: A for adding, R for removing, P for printing, X for quitting:\n")
    if option == 'A':
        AddDog()
    elif option == 'R':
        RemoveDog()
    elif option == 'P':
        printList()
    elif option == 'X':
        print("Thank you for using the program!")
        break
    else:
        print("Invalid option")






