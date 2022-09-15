hours = int(input("Enter hours worked per week:"))
rate = int(input("Enter rate:"))
grossPayWeek = hours*rate
print(grossPayWeek)
grossPayYear = grossPayWeek*52
print(grossPayYear)
grossPayMonth = grossPayYear/12
print(grossPayMonth)