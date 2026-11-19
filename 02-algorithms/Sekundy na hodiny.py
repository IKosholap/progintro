secundy = int(input("Počet sekund: "))
secundy_zbytek = secundy % 60
minuty = secundy // 60
minuty_zbytek = minuty % 60
hodiny = minuty // 60

dny = hodiny // 24
if dny >= 1:
    hodiny_zbytek = hodiny % 24
    print(f"{dny}d {hodiny_zbytek:02d}:{minuty_zbytek:02d}:{secundy_zbytek:02d}")
else:
    print(f"{hodiny:02d}:{minuty_zbytek:02d}:{secundy_zbytek:02d}")
