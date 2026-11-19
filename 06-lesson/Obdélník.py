#Napište třídu Rectangle s atributy width a height a metodami:

#area() a perimeter() — obsah a obvod,
#is_square() — vrátí True, pokud je obdélník čtverec,
#scale(factor) — zvětší oba rozměry factorkrát,
#describe() — vrátí řetězec, například Obdélník 3 × 4, obsah 12.
#Vytvořte seznam alespoň tří obdélníků, vypište jejich popis a najděte ten s největším obsahem.


class Rectangle:
    def __init__(self,width, height):
        self.height = height
        self.width = width

    def area(self):
        return self.width*self.height

    def is_square(self):
        return self.width == self.height
    def scale(self, factor):
        self.width = self.width * factor
        self.height = self.height * factor
    def describe(self):
        return f"Obdélník {self.width} x {self.height}, obsah {self.area()}."

def max_of_three_rect_area(a,b,c):
    max = a
    if b.area() > max.area():
        max = b
    if c.area() > max.area():
        max = c
    return max

a = Rectangle(10,5)
b = Rectangle(1,15)
c = Rectangle(6,9)

print(f"a = {a.describe()} \nb = {b.describe()} \nc = {c.describe()}")
print(f"nejvetsi obdelnik: {max_of_three_rect_area(a,b,c).describe()}")


