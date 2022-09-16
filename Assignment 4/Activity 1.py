# References:
# 1. Programming Fundamentals
# 2. https://www.w3schools.com/
# 3. https://www.python.org/about/gettingstarted/

# Getting input from the user
hours = float(input("Enter hours worked per week:"))
rate = float(input("Enter rate:"))

# Calculating weekly, yearly, monthly gross pay
gross_pay_week = hours * rate
gross_pay_year = gross_pay_week * 52
gross_pay_month = gross_pay_year / 12

# Printing results
print("Weekly pay " + str(gross_pay_week))
print("Monthly pay " + str(gross_pay_month))
print("Annual pay " + str(gross_pay_year))
