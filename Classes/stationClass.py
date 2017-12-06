class Station(object):
    """Station with it's name and coordinates"""
    def __init__(self, aName, aLongitude, aLatitude, critically):
        self.name = aName
        self.longitude = aLongitude
        self.latitude = aLatitude
        self.destinations = []
        if critically == "Kritiek":
            self.isCritical = True
        else:
            self.isCritical = False

    def addDestination(self, destination):
        self.destinations.append(destination)
