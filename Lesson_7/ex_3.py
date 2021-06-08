from os import path, walk, listdir
import shutil

folder_name = 'my_project2'

try:
    for root, dirs, files in walk(folder_name):
        if 'templates' in dirs and root != folder_name:
            for entry in listdir(path.join(root, 'templates')):
                # shutil.copytree(path.join(root, root, entry))
                shutil.copytree(path.join(root, 'templates', entry),
                    path.join(folder_name, 'templates', path.basename(root)))
except FileExistsError:
    print("runtime error, such file does not exist or the specified location is invalid")
