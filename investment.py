#!/usr/bin/python3
# Have the user enter their investment amount and expected intrest 
# Each year their investment will increase by their investment + their investment * interest rate is
# print out the earnings after 10 year period

# Ask for the money invested + the interest rate
money, interest_rate = input("Please enter your invested amount and interest rate ").split()
# Convert the value to float 
money = float(money)
# Convert value to a float and round the percentage rate by 2 digits
interest_rate = float(interest_rate) * .01
# Cycle through 10 years using a loop and range from 0 to 9 
for i in range(0, 10):
    money = money + (money * interest_rate)
# Output the results
print("Investment of ten year wil be {:.2f}".format(money))

