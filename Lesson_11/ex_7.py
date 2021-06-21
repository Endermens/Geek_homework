
class Complex_number():
    """ Операции с комплексными числами """
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def __add__(self, other):
        """ add """
        return f"{self.number1 + other.number1} + i*{self.number2 + other.number2}"

    def __mul__(self, other):
        """ (a - bi) * (c + di) = (ac - bd) + (bc + ad)i """
        return f"({(self.number1 * other.number1) - (self.number2 * other.number2)}) + ({(other.number1 * other.number1) + (self.number1 * other.number2)})i"

a1 = Complex_number(1, 6)# a b
a2 = Complex_number(4, 3)# c d
print(a1 + a2)
print(a1 * a2)
