class Data:
    @classmethod
    def day_year(cls, interger, month, year):
        pass
    @staticmethod
    def proverka(interger, month, year):
        if interger < 1 or interger > 12 and month <= 0 or month > 30 and year < 1900 or year > 2045:
            print(f"{interger} не прошло валидацию")
        if month < 0 or month > 30:
            print(f"{month} не прошло валидацию")
        if year < 1900 or year > 2045:
            print(f"{year} не прошло валидацию")
        else:
            return interger, month, year

Data.day_year(11, 75, 2005)
print(Data.proverka(-11, 75, 2005))
