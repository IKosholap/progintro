#Číslo: 202
#Dvojkově: 11001010
#Kontrola: 0b11001010
#Počet bitů: 8
#Počet jedniček: 4

cislo = int(input("Číslo: "))
temp = cislo
output = ""
while temp>0:
    if temp%2 == 1:
        output = output+"1"
    else:
        output = output+"0"
    temp = temp // 2

output = output[::-1]

print(f"Dvojkově: {output}")
print(f"Kontrola: {bin(cislo)}")
print(f"Počet bitů: {len(output)}")

jednicky = 0
for i in output:
    if i == "1":
        jednicky += 1
print(f"Počet jedniček: {jednicky}")