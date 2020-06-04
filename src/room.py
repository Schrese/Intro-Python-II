# Implement a class to hold room information. This should have name and
# description attributes.
# from item import Item

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def __str__(self):
        return f"|\nYou find yourself in {self.name}, as you look around, you see {self.description}"


# class VisibleItems(Room):
#     def __init__(self, name, description):
#         super().__init__(name, description)
#         self.items = []
    
#     # def create_items(item_name, item_description):
#     #     item = Item(item_name, item_description)
#     #     self.items.append(item)

#     # def __str__(self):
#     #     print(f"You find {self.items} in here")
    
#     def print_items(self):
#         print(self.items)

# newroom = Room("news", "we got it")

# office = Room("office", "office description")
# print(office)

# offitems = VisibleItems(office).create_items('sword', 'something cool')

# # itemlist = [("sword, something"), ("another", "something else")]


# print(offitems)