def rectangle(len_,width_):
    s = ''
    s += '+---'*len_
    s += '+'
    d = ''
    d += '|   '*len_
    d += '|'

    out = ''
    for i in range(width_):
        out +=s
        out += '\n'
        out +=d
        out += '\n'
    out += s
    print(out)


rectangle(4,2)