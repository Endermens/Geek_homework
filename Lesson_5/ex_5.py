src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []
for i in src:
    if src.count(i) == 1:
        result.append(i)
print(result)

print("\nOPTIMIZE:\n")
print([x for x in src if (src).count(x) == 1], "\n")

print("\nCringe optimize: \n")
print(list(set(src))) #ну...
