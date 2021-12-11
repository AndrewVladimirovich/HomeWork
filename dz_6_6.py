"""Сам не делал. Не понял до конца как добавить значения в файл."""

from sys import argv

with open('bakery.csv', 'r', encoding='utf8') as donut_r:
    if 1 < len(argv) < 4 and [i for i in argv[1:] if i.isdigit()]:
        if len(argv) == 3:
            start,  finish = map(int, argv[1:])
            print(*(v for i, v in enumerate(donut_r) if start - 1 <= i < finish), sep="")
        else:
            print(*(v for i, v in enumerate(donut_r) if i >= int(argv[1]) - 1), sep="")
    else:
        print(donut_r.read())


"""add sale"""


from sys import argv

with open('backery.csv', 'a', encoding='utf-8') as donut_a:
    with open('bakery.csv', 'r', encoding='utf-8') as donut_r:
        if len(argv) > 1 and [i for i in argv[1:] if '.' in i and i.replace('.','').isdigit()]:
            if round(float(argv[1]), 3) <= 99999.999:
                print(f'{round(float(argv[1]), 3):>10}', file=donut_a)
            else:
                print('Number must be less than 99999.999')
        else:
            print(donut_r.read())

