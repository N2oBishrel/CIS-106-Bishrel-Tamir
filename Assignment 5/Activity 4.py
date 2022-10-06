def calculatedogage(age):
    dogage = age * 7
    
    return dogage

def displayresult(dogage, name):
    print("The dogs name is " + name + " and they are " + str(dogage) + " years old")

def getdogage():
    print("Input dog`s age in human years")
    age = int(input())
    
    return age

def getdogname():
    print("Input dog`s name")
    name = input()
    
    return name

# Main
# This program prompts the user for the name of their dog and its age in human years.
name = getdogname()
age = getdogage()
dogAge = calculatedogage(age)
displayresult(dogAge, name)
