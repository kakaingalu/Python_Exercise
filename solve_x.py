#!/usr/bin/python3

# solve for x
# x + 4 = 9

# x will always be the 1st value recieved by and only
# will deal with addition

# Recieve the string and split the string into variables

# Convert the strings into less

# Convert the result into a string and join it to the string "x = "

# print()

def solve_x(equation):
    x,add,num1,equal,num2 = equation.split()
    num1,num2 = int(num1),int(num2)
    return "x = " + str(num2 - num1)

print(solve_x("x + 5 = 9"))
