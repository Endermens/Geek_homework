
class Worker(object):
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus":bonus}

class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return f"{sum(self._income.values())}"

office_worker = Position("Maksim", "Kopalkov", "Senior", 1000000, 500000)
print(office_worker.get_full_name(), "/n", office_worker.get_total_income())
