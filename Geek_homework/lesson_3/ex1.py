def num_translate(word):
    en_ru = {"zero": "ноль", "one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять",
             "six": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}
    return  en_ru.get(word)

print(num_translate(input("введите число: ")))