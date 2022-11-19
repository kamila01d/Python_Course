import math
from collections import Counter

import sys

argv = sys.argv[1:]


def rozklad(n):
    a = math.sqrt(n)
    k = 2
    d = []

    while n > 1 and k <= a:
        while (n % k == 0):
            d.append(k)
            n /= k
        k += 1

    if n > 1:
        d.append(n)

    d = Counter(d)

    for key in d:
        if d[key] > 1:
            print(int(key), '^', int(d[key]), sep='', end='')
        else:
            print(int(key), sep='', end='')
        if list(d)[-1] != key:
            print('*', sep='', end='')


for i in range(1, len(argv)+1):
    print(int(sys.argv[i]), '= ', end='')
    rozklad(int(sys.argv[i]))
    print(end='\n')
