# References:
# 1. Programming Fundamentals
# 2. https://www.w3schools.com/
# 3. https://www.python.org/about/gettingstarted/

# Getting input from the user
hours = int(input("Enter hours worked per week:"))
rate = int(input("Enter rate:"))

# Calculating weekly, yearly, monthly gross pay
gross_pay_week = hours * rate
gross_pay_year = grossPayWeek * 52
gross_pay_month = grossPayYear / 12

# Printing results
print(gross_pay_week)
print(gross_pay_month)
print(gross_pay_year)
