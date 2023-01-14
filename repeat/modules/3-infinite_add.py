if __name__ == "__main__":
    from sys import argv
    sum = 0
    for a in range(len(argv) - 1):
        sum = sum + int(argv[a + 1])
    print(sum)