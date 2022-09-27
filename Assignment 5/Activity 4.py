def calculateAge(age):
    humanAge = age * 7
    print("Dog's age in human age is " + str(humanAge))

def getAge():
    print("Enter dog's age: ")
    age = int(input())
    
    return age

# Main
# variable to store age
# calling function to get input from the user
age = getAge()

# calling function to calculate dog's age in human's age
calculateAge(age)
