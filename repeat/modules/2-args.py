#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1
    a = 0
    if argc == 2:
        print(f"{1} argument:")
    if argc == 1:
        print(f"{0}: arguments.")
    else:
        print(f"{argc} arguments:")
    for a in range(argc):
        print(f"{a + 1}: {argv[a + 1]}")