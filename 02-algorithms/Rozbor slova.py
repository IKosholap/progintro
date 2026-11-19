#Slovo: Nepotopen
#Počet znaků: 9
#První znak: N
#Poslední znak: n
#Velkými písmeny: NEPOTOPEN
#Pozpátku: nepotopeN
#Palindrom: True

slovo = input("Slovo: ")
length = len(slovo)
prvni_znak = slovo[0]
posledni_znak = slovo[length-1]
slovo_upcase = slovo.upper
slovo_backwards = ""
for i in range(0, length):
    a = length - i
    slovo_backwards = slovo_backwards+slovo[a]

slovo_low = slovo.lower

is_polyndrom = True
i = len(slovo) -1
for i in slovo:
    if i != slovo_low[i]:
        is_polyndrom = False
        break
    i = i-1

print(f"Počet znaků: {length}")
print(f"První znak: {prvni_znak}")
print(f"První znak: {posledni_znak}")
print(f"Velkými písmeny: {slovo_upcase}")
print(f"Pozpátku: {slovo_backwards}")
print(f"Palindrom: {is_polyndrom}")

