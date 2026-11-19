for cislo in range(1, 101):
    pocet = 0
    max_count = cislo **0.5
    for i in range(1, cislo):
        if i > max_count:
            break
        if cislo % i == 0:
            pocet = pocet +1
    if pocet == 1:
        print(cislo)
print(f"pocet: {pocet}")