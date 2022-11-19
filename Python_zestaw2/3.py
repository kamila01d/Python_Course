import re
from collections import Counter
def foo(str_):
    numbers = sum(c.isdigit() for c in str_)
    letters = sum(c.isalpha() for c in str_)
    print("Liczba liter wynosi:",letters)
    print("Liczba cyfr wynosi:", numbers)

    str_ = str_.split()
    l = 0
    s = ''
    for i in str_:

        if (bool(re.match('^[a-zA-Z0-9]*$', i)) == True):
            l += 1
            s +=i

    print('Liczba slow wynosi: ',l)
    counter = Counter(s)
    print("Statystyka czestotliwosci wystepowania", dict(counter))

foo(str_ = 'Ala , onomatopeja . -')

