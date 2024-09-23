class LocationManager:
    def __init__(self):
        self.locations = {}
    
    def add_locations(self, name, latitude, longitude):
        self.locations[name] = (latitude, longitude)
        print(f"Location '{name}' added with coordinates: ({latitude},{longitude})")

    def get_coordinates(self, name):
        
        if name in self.locations:
            return self.locations[name]
        else: 
            return None
        
# Example usage
location_manager = LocationManager()

# Adding locations
location_manager.add_locations("Eiffel Tower", 48.8584, 2.2945)
location_manager.add_locations("Statue of Liberty", 40.6892, -74.0445)

# Getting coordinates
eiffel_tower_coords = location_manager.get_coordinates("Eiffel Tower")
print(f"Coordinates of Eiffel Tower: {eiffel_tower_coords}")

statue_of_liberty_coords = location_manager.get_coordinates("Statue of Liberty")
print(f"Coordinates of Statue of Liberty: {statue_of_liberty_coords}")