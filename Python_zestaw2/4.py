def fun(N):
    binary = bin(N)
    binary = binary[2:]
    length = len(binary)
    i = 0
    counter = 0
    lista = []

    while i < length:
        if binary[i] == "0":
            counter += 1
        elif binary[i] == "1":
            lista.append(counter)
            counter = 0
        i += 1

    print(max(lista))

fun(20)
