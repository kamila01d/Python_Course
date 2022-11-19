def miarka(len_):
    s = ''
    s += '|....'*len_
    s += '|'
    s += '\n'

    for i in range(len_+1):
        s += str(i)
        s += ' '*(6 - len(str(i+1))-1)

    print(s)



miarka(100)
