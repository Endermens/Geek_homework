from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
list_1 = []


def get_jokes(n, flag=False):
    """
    1. the program sets as many generation options as the user requests.
    2. the function randomly selects an item from each list.
    3. there is a check for duplication, if there is one, it deletes and replaces the duplicate.
    """
    for i in range(n):
        x = choice(nouns)
        x1 = choice(adverbs)
        x2 = choice(adjectives)
        joke = (f'{x} {x1} {x2}')
        list_2 = []
        print(joke)
        if flag == True:
            list_2 = joke.split()

            for adverb in adverbs:
                for fun in list_2:
                    if adverb == fun:
                        adverbs.remove(adverb)

            for adjective in adjectives:
                for fun in list_2:
                    if adjective == fun:
                        adjectives.remove(adjective)


print(get_jokes(3))