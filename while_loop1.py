#!/usr/bin/python3
i = 1

while i <= 20:
    if (i % 2) == 0:
        i += 1
        continue

    if i == 15:
        break

    print(i)

    i += 1
