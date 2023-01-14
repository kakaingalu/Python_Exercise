def uppercase(str):
    for a in str:
        if ord(a) >= ord('a') and ord(a) <= ord('z'):
             a = chr(ord(a) - 32)
        print(f"{a}", end='')
    print()