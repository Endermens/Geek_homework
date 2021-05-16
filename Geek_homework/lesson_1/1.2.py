list = []
for i in range(1001):
    if i % 2 != 0:
        list.append(i)
print(str(list),"\n")

print(sum(filter(lambda j: sum(map(int, str(j))) % 7 == 0, [i**3 for i in range(1, 1001, 2)])), "- сумма всех чисел кратных 7.\n")
print(sum(filter(lambda j: sum(map(int, str(j + 17))) % 7 == 0, [i**3 for i in range(1, 1001, 2)])), "- сумма всех чисел после прибаления 17 к числам.")
