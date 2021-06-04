from json import dump
from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:
            person_list = zip_longest((" ".join(us.split(",")) for us in users), hobby)
            my_dict = {str(el[0]).strip(): (el[1].strip()) for el in person_list}

            with  open('dict.json', 'w', encoding = 'utf-8') as f:
                dump(my_dict, f, ensure_ascii=False, indent = 4)
                print("\n".join(f'{k}: {v}' for k,v in my_dict.items()))
