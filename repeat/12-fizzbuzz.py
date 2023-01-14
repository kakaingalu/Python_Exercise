def fizzbuzz():
    for a in range(1, 101):
        if (a % 3) == 0:
            print("Fizz", end=' ')
        elif (a % 5) == 0:
            print("Buzz", end=' ')
        elif (a % 15) == 0:
            print("FizzBuzz", end=' ')
        else:
            print(a, end=' ')

fizzbuzz()