import os

names = os.listdir()
files_dict = {}

for file in names:
    name, extension = os.path.splitext(file)

    if extension not in files_dict:
        files_dict[extension] = []
    files_dict[extension].append(name)

for extension, names in sorted(files_dict.items()):
    print(extension)

    for name in sorted(names):
        print(f'- - - {name}{extension}')