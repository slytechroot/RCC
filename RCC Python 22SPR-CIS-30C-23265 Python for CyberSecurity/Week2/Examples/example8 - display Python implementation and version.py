#Example 8: Display Python implementation and version.

from platform import python_implementation, python_version_tuple
print(python_implementation())
for attribute in python_version_tuple():
    print(attribute)
