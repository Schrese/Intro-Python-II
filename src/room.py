# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"You find yourself in {self.name}, as you look around, you see {self.description}"

# room1 = Room("name", "some sort of description")

# print(room1)