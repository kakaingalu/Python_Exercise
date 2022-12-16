#!/usr/bin/python3
import random
Random = random.randint(-10, 10)
if Random < 0:
    print("{} is negative".format(Random))
elif Random == 0:
    print("{} is zero".format(Random))
elif Random > 0:
    print("{} is positive".format(Random))
