vyska = -1
while True:
    vyska = input("Výška: ")
    if vyska.isdigit():
        if int(vyska) %2 == 1:
            vyska = int(vyska)
            break
        else:
            print("Napiste lyche cislo")
    else:
         print("Napiste cislo")

mid_x = vyska//2+1
mid_y = vyska//2+1

for y in range(1, mid_y):
    print(" "*(mid_y-y),end="")
    print("*"*(y*2-1))

print("*"*vyska)

for y in range(mid_y, vyska):
    print(" "*(mid_y+y-vyska),end="")
    print("*"*((vyska-y)*2-1))

