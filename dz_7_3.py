from os import path, walk, listdir
import shutil

mydir_name = 'my_new_project'

try:
    for root, dirs, files in walk(mydir_name):
        if 'templates' in dirs and root != mydir_name:
            for entry in listdir(path.join(root, 'templates')):
                shutil.copytree(path.join(root, 'templates', entry),
                                path.join(mydir_name, 'templates', entry))
except FileExistsError:
    print('Already worked with these templates!')


