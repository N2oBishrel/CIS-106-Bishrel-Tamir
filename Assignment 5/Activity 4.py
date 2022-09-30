def calculateCelsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    
    return celsius

def displayResult(fahrenheit, celsius):
    print(str(fahrenheit) + "°Fahrenheit is" + str(celsius) + "°Celsius")

def getFahrenheit():
    print("Enter Fahrenheit temperature:")
    fahrenheit = float(input())
    
    return fahrenheit

# Main
fahrenheit = getFahrenheit()
celsius = calculateCelsius(fahrenheit)
displayResult(fahrenheit, celsius)
