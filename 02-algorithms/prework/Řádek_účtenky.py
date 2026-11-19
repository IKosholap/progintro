name = input("Položka: ")
price = float(input("Cena za kus [Kč]: "))
amount = int(input("Počet kusů: "))

total = price * amount
print(f"{name}: {amount} × {price:.2f} Kč = {total:.2f} Kč")