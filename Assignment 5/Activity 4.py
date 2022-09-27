def calculateAge():
    age = getAge()
    humanAge = age * 7
    displayAge(humanAge, 1, "")
    
    return humanAge

def calculateStage():
    month = getMonth()
    if month < 24:
        stage = "Puppy"
    else:
        stage = "Adult"
    displayAge(0, 2, stage)

def displayAge(humanAge, choice, stage):
    if choice == 1:
        print("Dogs age in human age is " + str(humanAge))
    else:
        print("Dog is " + stage)

def getAge():
    print("Enter dog's age: ")
    age = int(input())
    
    return age

def getChoice():
    print("Enter Y to convert dogs age to humans age or N to get dogs life stage")
    choice = input()
    
    return choice

def getMonth():
    print("Enter dog's month: ")
    month = int(input())
    
    return month

# Main
choice = getChoice()
if choice == "Y" or choice == "y":
    calculateAge()
else:
    calculateStage()
