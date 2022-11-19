class Bug:
    """some Bug class"""

    licznik = 0

    def __init__(self):
        """Initailize new object"""
        self.id = Bug.licznik
        Bug.licznik += 1
    def __del__(self):
        print('Koniec', Bug.licznik, self.licznik)
        Bug.licznik -= 1

    def __str__(self):
        """Returns licznik and id"""
        return str(Bug.licznik) + " " + str(self.id)


bugs = []
for i in range(100):
    bugs.append(Bug())
    print(bugs[-1])

print(help(Bug))