from itertools import islice, zip_longest


tutors = ["Иван", "Анастасия", "Петр", "Сергей", "Дмитрий", "Борис", "Елена"]
klasses = ['9A', '7B', '9Б', '9B', '8Б', '10A', '10Б', '9A']


name_klasses = ((tutors[n], klasses[n]) if len(klasses) > n else (tutors[n], None) for n in range(len(tutors)))

print(type(name_klasses), *name_klasses, sep='; \n ')
print(next(name_klasses))


