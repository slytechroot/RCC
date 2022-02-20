#write a script to define a Python function and use arguments to displaya list of network server 
#types
#U1Ex9.py - using lists are arguments

#define method or function
def show_Server(systems):
    for s in systems:
        print(s)

servers_List = ['FTP','DHCP','RAS','AD','IIS','Apache','DNS']

#call the function show_Server which will also print the servers_List
#pass the parameter of servers_List

show_Server(servers_List)

print(servers_List)

