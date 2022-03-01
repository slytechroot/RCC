#U2Ex2
import os

#2A display current working directory
pwd = os.getcwd()
print(pwd)

#2B display files and folders in current working directory
list_directory = os.listdir(pwd)
for directory in list_directory:
    print('+', directory)

#2C use os.walk() to list files and folders in current working directory
for root, directories, files in os.walk('.', topdown=False):
    #iterate over the files in the current 'root' folder
    for file_entry in files:
        #create the relative path to the file
        print('[+]', os.path.join(root, file_entry))
    for name in directories:
        print('[++]', name)

#2D use os.walk() and Count() in collections to count items in current directory
from collections import Counter
counts = Counter()
for currentdir, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        first_part, extension = os.path.splitext(filename)
        counts[extension] += 1
for extension, count in counts. items():
    print(f"{extension:8}{count}")

