import os

dir = "/Users/mdkhan/Code"
file_dict = {}
dir_dict = {}
for index, name in enumerate(os.listdir(dir)):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        dir_dict[name] = dir
        print(f"{fullname} is a directory")
    else:
        print(f"{fullname} is a file")
print(index, dir_dict)