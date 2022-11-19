def triangle(num_of_stairs):
    if (len(num_of_stairs)//2 == 0):
        print("Otrzymano parzysta liczbe!")
        return
    for i in range(0,len(num_of_stairs),2):
        if i == 0:
            print('*'*len(num_of_stairs))
        elif i == len(num_of_stairs)-1:
            print(" "*(i//2 -1),'*')
        else:
            print(" "*(i//2) + '*' + " "*((len(num_of_stairs)-2-(i//2)*2)) +'*')

param = input('jakis tekst')
triangle(param)
