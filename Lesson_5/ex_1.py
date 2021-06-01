def generate(min_f):
    for num in range (1, min_f):
        if num % 2 != 0:
            yield num

for i in generate(111):
        print (i)
