from json import dump
from itertools import zip_longest

with open('users.csv', 'r') as users:
    with open('hobby.csv', 'r') as hobby:

        if len(users.readlines()) >= len(hobby.readlines()):
            users.seek(0)
            hobby.seek(0)
            with open('dictionary_1.json', 'w', encoding='utf-8') as f:
                all_list = zip_longest((' '.join(us.split(',')) for us in users), hobby, fillvalue=None)
                my_dict = {str(el[0]).strip(): str(el[1]).strip() for el in all_list}

                dump(my_dict, f, ensure_ascii=False, indent=4)
            print(my_dict)
        else:
            exit(1)

