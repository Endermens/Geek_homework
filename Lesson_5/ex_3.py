tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klass = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

tut_klas = ((tutors[n], klass[n]) if len(klass) > n else (tutors[n], None) for n in range(len(tutors)))

print(*tut_klas, sep="\n")
# print(next(tut_klas)) #stop interation

print("\n", dict(zip(tutors, klass))) #подумал что в подобном случае можно обойтись без генератора.
