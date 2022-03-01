#U2Ex3

import platform

#U2Ex3
#3A display OS
operating_system = platform.system()
print('Your operating system is: ', operating_system)

#3B display command based on OS
if(operating_system == 'Windows'):
    net_command = "ipconfig"
elif(operating_system == 'Linux'):
    net_command = "ip addr"
else:
    net_command = 'ipconfig getifaddr en1'

print(net_command)

#3C display Python implementation and version
from platform import python_implementation, python_version, python_version_tuple
print(python_implementation())
for attribute in python_version_tuple():
    print(attribute)


