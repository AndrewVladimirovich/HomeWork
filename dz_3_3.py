
def thesaurus(*args):
    names_employee = {}
    for i in sorted(args):
        capital_letter = i[0]
        if capital_letter in names_employee:
            names_employee[capital_letter] += [i]
        else:
            names_employee[capital_letter] = [i]
    return names_employee

print(thesaurus('Петр', 'Василий', 'Михаил', 'Мария', 'Валерий', 'Владислав', 'Евгений', 'Евгения', 'Артем',
            'Антонина', 'Сергей', 'Марат', 'Игорь', 'Павел', 'Андрей', 'Серафима'))

print(type(thesaurus()))


