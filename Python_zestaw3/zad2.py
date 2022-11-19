def convert(num):

    if not isinstance(num, int):
        return "Incorrect value"
    if 3999 < num < 1:
        return "Value must be in the scope 1-3999!"

    num_ = str(num)
    lenOfNum = len(str(num))
    out = ''
    indx = 0

    if lenOfNum == 4:
        out += 'M'*int(num_[indx])
        print(out)
        indx += 1
    if lenOfNum >= 3:
        if int(num_[indx]) == 0:
            indx += 1
        elif 3 >= int(num_[indx]) > 0:
            out += 'C' * int(num_[indx])
            indx += 1
        elif int(num_[indx]) == 4:
            out += 'CD'
            indx += 1
        elif int(num_[indx]) == 5:
            out += 'D'
            indx += 1
        elif 8 >= int(num_[indx]) > 5:
            out += 'D' + 'C' * (int(num_[indx])-5)
            indx += 1
        elif int(num_[indx]) == 9:
            out += 'CM'
            indx += 1
    if lenOfNum >= 2:
        if int(num_[indx]) == 0:
            indx += 1
        elif 3 >= int(num_[indx]) > 0:
            out += 'X' * int(num_[indx])
            indx += 1
        elif int(num_[indx]) == 4:
            out += 'XL'
            indx += 1
        elif int(num_[indx]) == 5:
            out += 'L'
            indx += 1
        elif 8 >= int(num_[indx]) > 5:
            out += 'L' + 'X' * (int(num_[indx])-5)
            indx += 1
        elif int(num_[indx]) == 9:
            out += 'XC'
            indx += 1
    if lenOfNum >= 1:
        if int(num_[indx]) == 0:
            indx += 1
        elif 3 >= int(num_[indx]) > 0:
            out += 'I' * int(num_[indx])
            indx += 1
        elif int(num_[indx]) == 4:
            out += 'IV'
            indx += 1
        elif int(num_[indx]) == 5:
            out += 'V'
            indx += 1
        elif 8 >= int(num_[indx]) > 5:
            out += 'V' + 'I' * (int(num_[indx])-5)
            indx += 1
        elif int(num_[indx]) == 9:
            out += 'IX'
            indx += 1

    print(out)


def RomanToNum(num):
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    for i in num:
        if not i in roman:
            return "Incorrect value"
    prev = 0
    outnum = 0
    for i in num:
        current = roman[i]
        if prev < current and prev != 0:
            outnum += (current - 2*prev)
        else:
            outnum += current
        prev = current
    print(outnum)



RomanToNum('MMMCMXCIX')

convert(3221)


