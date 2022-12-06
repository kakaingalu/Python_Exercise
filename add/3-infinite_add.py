#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    for arg in range(1, len(argv)):
        sum = sum + int(argv[arg])
    print("{}".format(sum))
