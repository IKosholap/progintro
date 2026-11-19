for cislo in range(100,1001):
    sto = cislo // 100
    deset = (cislo//10 %10)
    jedn = (cislo % 10)%10

    if cislo == sto**3+deset**3+jedn**3:
        print(str(cislo)+" "+str(sto)+" "+str(deset)+" "+str(jedn))


