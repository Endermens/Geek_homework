class NoInt(Exception):
    def __init__(self, txt):
        self.txt = txt

list = [1, 2, 6]
stop = False
while stop==False:
    try:
        a = input()
        list.append(a)
        for i in list:
            if type(list) != int or type(list) != float:
                raise NoInt("в этом списке некотрые элементы не являються числами!")
    except NoInt as err:
        print(err)
        stop = True
    else:
        print(list)
