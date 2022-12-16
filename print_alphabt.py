#!/usr/bin/python3
for alpha in range(ord('a'), ord('{')):
    if alpha == ord('q') or alpha == ord('e'):
        continue
    print(chr(alpha), end='')
    #print(chr(123))