x = 10


def double_print(x):
    print(x * 2)


def double_return(x):
    return x * 2


a = double_print(5)
b = double_return(5)
print("a =", a)
print("b =", b)
print("x =", x)

#x se nezmneni protoze ve funkce pouzivame lokalni hodnotu x
# funkce vrati 