for a in range(0, 10):
    for b in range(1 + a, 10):
        if a == 8 and b == 9:
            print(89)
        else:
            print(f"{a}{b}", end=', ')