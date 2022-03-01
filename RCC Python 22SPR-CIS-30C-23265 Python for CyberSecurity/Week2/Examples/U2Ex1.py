#U2Ex1 using sys module
import sys

#2A script name
print('Name of the script is: ', sys.argv[0])

#2B number of arguments in script
print("\nThe number of arguments is: \n", len(sys.argv))

#2C OS platform
print("OS platform: ", sys.platform)

#2D python version
print("Python package version: ", sys.version)

#2E encoding and default encoding system
print('System encoding: ', sys.getfilesystemencoding)
print('Default encoding: ', sys.getdefaultencoding)

#2F environment variable path
print('Path environment variable: ', sys.path)

