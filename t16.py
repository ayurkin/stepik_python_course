from os import listdir
from os.path import isfile, join


# files = [f for f in listdir('C:/') if isfile(join('C:/', f))]
# print(files)

files2 = []
for i in listdir('C:/'):
    # print(i)
    if isfile(join('C:/', i)):
        files2.append(i)

print(files2)