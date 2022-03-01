#Example 4 - 
# retrieve the current working directory path and store the value on the pwd variable

import os

pwd = os.getcwd()
list_directory = os.listdir(pwd)

for directory in list_directory:
    print('[+] ', directory)
