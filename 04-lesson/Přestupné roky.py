pocet = 0
for rok in range(1890, 2031):
    if rok % 4 == 0 and not(rok%100 == 0) or rok %400 == 0:
        if pocet%10 == 0:
            print(f"{rok}", end="")
        else:
            print(f" {rok}", end="")
        pocet = pocet +1
        if pocet%10 == 0:
            print()
print()
        
print(pocet)