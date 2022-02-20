#Protocol search

Protocol_list = ['FTP', 'SNMP','TCP','HTTP','NTP','SSH','IP']
search_key = 'SSH'

found = False
for i in range(len(Protocol_list)):
    found = Protocol_list[i] == search_key
    if found:
        break
if found:
    print('Element found at index ', i)
else:
    print('Element not found.')

    