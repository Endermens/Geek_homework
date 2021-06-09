import os
from collections import defaultdict
import django

# dir = 'C:\Python\Home\Geek_homework\Lesson_7\mysite'
# list = os.listdir(dir) # dir is your directory path
# number_files = len(list)
# print ("fiels:", number_files)

root_dir = django.__path__[0] #mysite - django_project
django_files = defaultdict(int)
for root, dirs, files in os.walk(root_dir):
    for file in files:
        ext = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
        # ext1 = 10 ** len(str(etx))
        django_files[ext] += 1
for size, nums in sorted(django_files.items()):
    print(f'{ext}: {nums}')
