# is so hot...
class Sclad:
    def __init__(self, model, price, quantity, numb_list):
        self.model = model
        self.price = price
        self.quantity = quantity
        self.numb_list = numb_list
        self.my_store_full = []
        self.my_store = []
        self.model_unit = {'model name': self.model, 'price': self.price, 'quantity': self.quantity}

    def reception(self):
        try:
            unit = input("model name: ")
            unit_p = int(input("price: "))
            unit_q = int(input("quantity: "))
            unique = {'model name': unit, 'price': unit_p, 'quantity': unit_q}
            self.model_unit.update(unique)
            self.my_store.append(self.model_unit)
            print(f'List -\n {self.my_store}')
        except:
            return "Data entry error"


class Printer(Sclad):
    def to_print(self):
        return f'to print smth {self.numb_list} times'


class Scanner(Sclad):
    def to_scan(self):
        return f'to scan smth {self.numb_list} times'


class Xerox(Sclad):
    def to_copier(self):
        return f'to copier smth  {self.numb_list} times'


sclad_1 = Printer('hp', 2000, 5, 10)
sclad_2 = Scanner('Canon', 1200, 5, 10)
sclad_3 = Xerox('Xerox', 1500, 1, 15)

print(sclad_1.to_print())
print(sclad_2.to_scan())
print(sclad_3.to_copier())

print(sclad_1.reception())
print(sclad_2.reception())
print(sclad_3.reception())
