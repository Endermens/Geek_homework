print("что бы выйти напишите - exit\n")
translate = input("Введите нужное вам число от 0 до 10: ")

en_ru = {"zero": "ноль", "one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять",
         "six": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}

def num_translate(word):
    if word.istitle():
        return str(en_ru.get(word.lower())).title()
    return en_ru.get(word)


print(num_translate(translate))



