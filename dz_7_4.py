import os
import django
from collections import defaultdict

def my_directory():
    root_dir = django.__path__[0]
    django_files = defaultdict(int)
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
            django_files[size] += 1
    for size, nums in sorted(django_files.items()):
        print(f'{size}: {nums}')

my_directory()

'''не работает модуль django не пойму почему
asgiref    3.4.1
Django     4.0
pip        21.3.1
setuptools 59.1.1
sqlparse   0.4.2
wheel      0.37.0
(Lesson-7) andrew@MacBook-Pro-Andrej Lesson-7 % 

Пишет что модуль не найден:

/usr/local/bin/python3 /Users/andrew/PycharmProjects/Lesson-7/dz_7_4.py
Traceback (most recent call last):
  File "/Users/andrew/PycharmProjects/Lesson-7/dz_7_4.py", line 2, in <module>
    import django
ModuleNotFoundError: No module named 'django'

Process finished with exit code 1
'''
