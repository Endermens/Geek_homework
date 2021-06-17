
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



#usloive 2.0
c1 = Cell(2, 6)
c2 = Cell(8, 4)
print(f"складываю: {c1 + c2}\n")
print(f"вычитаю: {c1 - c2}\n")
print(f"умножаю: {c1 * c2}\n")
print(f"целочисленное деление: {c1 // c2}\n")
print(f"деление: {c1 / c2}\n")
