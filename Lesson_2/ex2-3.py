spisok = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort
i = 0
print(id(spisok))
while i < len(spisok):
    if spisok[i].isdigit() or (spisok[i].startswith(("+", "-")) and spisok[i][1:].isdigit()):
        if spisok[i].isdigit():
            spisok[i] = spisok[i].zfill(2)
        else:
            spisok[i] = spisok[i][0] + spisok[i][1:].zfill(2)
            spisok[:i] += '"'
            spisok[i:i + 2] += '"'

            i += 2
    i += 1

print(spisok)

print(id(spisok))
