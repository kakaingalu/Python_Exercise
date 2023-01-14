for a in range(ord('z'), ord('a') - 1, -1):
    if a % 2 == 0:
        n = a - 0
    else:
        n = a - 32
    print("{}".format(chr(n)), end='')