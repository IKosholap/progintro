#Napište třídu Vector2D se souřadnicemi x a y a metodami:

#length() — délka vektoru,
#add(other) — vrátí nový vektor, který je součtem obou,
#scale(k) — vrátí nový vektor kkrát delší,
#dot(other) — skalární součin,
#angle_to(other) — úhel mezi vektory ve stupních.
#Aby šel vektor rozumně vypsat pomocí print(), doplňte speciální metodu __str__.

class Vektor2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return (self.x**2 + self.y**2)**0.5
    def add(self, other):
        return Vektor2d(self.x + other.x, self.y + other.y)
    def scale(self, factor):
        self.x = self.x * factor
        self.y = self.y * factor
    def dot(self, other):
        return self.x * other.x + self.y * other.y
    def __str__(self):
        return(f"({self.x}, {self.y})")
    def angle_to(self, other):
        #cos(ab) = (ax * bx + ay * by)/(|a| * |b|)
        cos = (self.x*other.x+self.y*other.y)/(self.length*other.length())
        