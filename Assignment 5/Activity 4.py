def calculateAge(age):
    humanAge = age * 7
    
    return humanAge

def displayAge(humanAge):
    print("Dogs age in human age is " + str(humanAge))

def getAge():
    print("Enter dog's age: ")
    age = int(input())
    
    return age

# Main
# variable to store age
# calling function to get input from the user
age = getAge()
humanAge = calculateAge(age)
displayAge(humanAge)

# calling function to calculate dog's age in human's age
