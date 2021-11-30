from random import choice, randrange

nouns = ['город', 'деревня', 'чайник', 'дорога', 'море', 'картина', 'перец']
adverbs = ['жарко', 'скучно', 'весело', 'суетливо', 'не красиво', 'отлично', 'феерично', 'симпатично']
adjectives = ['жизненный', 'зеленый', 'сладкий', 'прелестный', 'искуственный', 'полезный']

def any_jokes(n, repeat=False):
    """

    :param n: указывает на количество шуток
    :param repeat: указывает будут ли шутки повторяться или нет False - соответсвтенно нет, True - да будут
    :return:

    """
    non, adverb, adject = nouns.copy(), adverbs.copy(), adjectives.copy()
    number_of_jokes = []
    number_of_jokes_min = min(non, adverb, adject)
    while n and len(number_of_jokes_min):
        num = randrange(len(number_of_jokes_min)) 
        if repeat:
            number_of_jokes.append(f"{non.pop(num)} {adverb.pop(num)} {adject.pop(num)}")
        else:
            number_of_jokes.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
        n -= 1
    return number_of_jokes

print(any_jokes(6, True))