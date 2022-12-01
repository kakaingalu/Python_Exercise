#!/usr/bin/python3

def multi_divide(num1, num2):
    return (num1 / num2), (num1 * num2)

multi, divide = multi_divide(5,4)

print("5 x 4 =", multi)
print("5 / 4 =", divide)
