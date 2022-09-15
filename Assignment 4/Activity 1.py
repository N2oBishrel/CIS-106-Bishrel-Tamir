# Getting input from the user
hours = int(input("Enter hours worked per week:"))
rate = int(input("Enter rate:"))

# Calculating weekly, yearly, monthly gross pay
grossPayWeek = hours * rate
grossPayYear = grossPayWeek * 52
grossPayMonth = grossPayYear / 12

# Printing results
print(grossPayYear)
print(grossPayWeek)
print(grossPayMonth)
