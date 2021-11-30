translator = {'one': 'один', 'two': 'два', 'three': 'три', 'four': ' четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь',
         'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

def numeric_word_translate(i):
    return translator.get(i)






print(numeric_word_translate(input('Ведите любое число от одного до десяти: ')))