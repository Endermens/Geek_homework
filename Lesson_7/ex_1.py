import os

root_path = 'C:\Python\Home\Geek_homework\Lesson_7\my_project'
project_folder = 'my_project'
if not os.path.exists(project_folder):
    os.mkdir(project_folder)

new_folders =  ['settings', 'mainapp', 'adminapp', 'authapp']

for folder in new_folders:
    os.mkdir(os.path.join(root_path, folder))
