#Search Range example
from re import search


NumList = [2, 1, 14, 1, 409, 55, 82]
search_key = 67
found = False

for i in range(len(NumList)):
    found = NumList[i] == search_key
    if found:
        break
if found:
    print('Element found at index...', i)
else:
    print('Element not found.')

