'''
4.	Write a Python to declare a list of network devices and use common methods to accomplish 
the below tasks.
A.	Add a device to the list.
B.	Remove the first device from the list.
C.	Add tuple seg1_switch = ('NETGEAR04', 'NETGEAR05') to the list using extend()
D.	Add tuple seg1_switch = ('NETGEAR04', 'NETGEAR05') to the list using append()
'''
#declare a list of network devices
network_devices = ['Cisco01','FortiNet10','Linksys07']
print(network_devices)

#append a device to list
network_devices.append('Linksys08')
print(network_devices)

#remove the first device from the list
network_devices.remove('Cisco01')
print(network_devices)

#declare a tuple
seg1_switch = ('NETGEAR04','NETGEAR05')
print(seg1_switch)

#append tuple to list
print('\nMove a list into a tuple by extending.')
network_devices.extend(seg1_switch)
print(network_devices)

#use append instead
print('\nMove a list into a tuple by appending.')
network_devices.append(seg1_switch)
print(network_devices)



