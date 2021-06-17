class Clothes:
    """ clothes """
    def __init__(self, v = 0, h = 0):
        self.v = v
        self.h = h

    def coat(self):
        return (self.v / 6.5 + 0.5)

    @property
    def suit(self):
        return f"{2 * self.h + 0.3}"

    # @property
    def __add__(self, other):
        """ experemental """
        # return  Clothes((self.v / 6.5 + 0.5) + (other.v / 6.5 + 0.5) + (2 * self.h + 0.3) + (other.h * self.h + 0.3))
        return  Clothes(self.v + other.v, self.h + other.h)

    def __str__(self):
        return f"Объект с параметрами ({self.v}, {self.h})"

class Cell:
    """ какая-то клетка """
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

    def __add__(self, other):
        """ add """
        return Cell(self.data1 + other.data1, self.data2 + other.data2)

    def __sub__(self, other):
        return Cell(self.data1 - other.data1, self.data2 - other.data2)

    def __mul__(self, other):
        return Cell(self.data1 * other.data1, self.data2 * other.data2)

    def __floordiv__(self, other):
        return Cell(self.data1 // other.data1, self.data2 // other.data2)

    def __truediv__(self, other):
        return Cell(self.data1 / other.data1, self.data2 / other.data2)

    def make_order(self, pikachu):
        x = ""
        quantity_of_row = int(self.quantityr_of_snowflakes)//pikachu
        for i in range(quantity_of_row):
            x += ("*" * pikachu)
            x += "\n"
        rest_of_snowflakes = (int(self.data1) - quantity_of_row * pikachu)
        x += "*" * rest_of_snowflakes
        return x


    def __str__(self):
        return f"Что-то там возвращаю({self.data1}, {self.data2})"




a = Clothes(100, 5)
a2 = Clothes(20, 66)
print(a.coat())
print(a.suit)
print(f"{a + a2}\n")

#usloive 2.0
c1 = Cell(2, 6)
c2 = Cell(8, 4)
print(f"складываю: {c1 + c2}\n")
print(f"вычитаю: {c1 - c2}\n")
print(f"умножаю: {c1 * c2}\n")
print(f"целочисленное деление: {c1 // c2}\n")
print(f"деление: {c1 / c2}\n")
