class Dev:
    def __init__(self, name, IPaddress):
        self.name = name
        self.IPaddress = IPaddress
        print("Device name: ", name)
        print("IP address: ", IPaddress)

class Loc(Dev):

    def __init__(self, name, IPaddress, location):
        super().__init__(name, IPaddress)
        print("Location of device: ", location)

c = Loc('Cisco Switch', '10.0.0.17', 'HQ')

