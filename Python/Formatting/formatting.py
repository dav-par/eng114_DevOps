class Location:

    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

    def __repr__(self):
        return f"Location(latitude={self.lat}, longitude ={self.long})"



bham_academy = Location(52.488647, -1.887249)

print(bham_academy)