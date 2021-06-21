class Sclad:
    """ Склад Оргтехники """
    def __init__(self, printout):
        self.printout = printout

class Printer(Sclad):
    def __init__(self, printout):
        self.text = printout

    def finalinput(self):
        return f"Printer - распечатка: {self.text}"

class Scanner(Sclad):
    def __init__(self, printout):
        self.text_data= printout

    def vivod(self):
        return f"Scaner - отправил на комп: {self.text_data}"

class Xerox(Sclad):
    def __init__(self, printout):
        self.text_data = printout

    def pechat(self):
        return f"Xerox - распечатка: {self.text_data}"

printer = Printer("text")
print(printer.finalinput())

scan = Scaner("text")
print(scan.vivod())

xerox = Xerox("text")
print(xerox.pechat())
