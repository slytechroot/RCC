'''
5.	Refer to  Python Documentation for Built-in List Methods and write a Python script to 
accomplish the following tasks.
A.	Sort the list created in Exercise 4 including step 4C. *Note: sort() cannot sort tuple. Display list.
B.	Count the number of times ‘NETGEAR05’ appears in the list in Exercise 4. Display count value.
C.	Return the index of ‘NETGEAR04’. Display index.
D.	Display the last item in the list using list index.
E.	Insert ‘Linksys12’ at the third index or 4th item in the list.
F.	Display the reversed list.
G.	Clear the list.

'''
#declare a list of network devices
network_devices = ['FortiNet10','ASA5500','Linksys07','Linksys08','NETGEAR04','NETGEAR05']

#sort the list
network_devices.sort()
print(network_devices)

#count 'NETGEAR' in list
print(network_devices.count('NETGEAR05'))

#return and print index of 'NETGEAR04'
network_item = network_devices.index('NETGEAR04')
print(network_item)

#display the last item on the list
print(network_devices[-1])
#or
print(network_devices[5])

#print range of devices: second to last item
print(network_devices[1:6])

network_devices.insert(3, 'Linksys12')
print(network_devices)

#display reversed list
network_devices.reverse()
print(network_devices)

#clear all items from the list
network_devices.clear()
print(network_devices)




