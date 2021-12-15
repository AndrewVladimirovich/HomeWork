import os

starter_list = {'my_project': [{'settings': []}, {'mainapp': []}, {'adminapp': ['my_password.txt']}, {'authapp': []}]}

for key, val in starter_list.items():
    if not os.path.exists(key):
        for item in val:
            for s in item.keys():
                os.makedirs(os.path.join(key, s))

