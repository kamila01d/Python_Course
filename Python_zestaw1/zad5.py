def seq(a,b):
    a = set(a)
    b = set(b)

    print(list(a & b))
    print(list(a | b))

seq('ala ma kota','tolo ma alas')