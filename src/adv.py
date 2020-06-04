# from room import Room, VisibleItems
from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].north_to = room['foyer']
room['foyer'].south_to = room['outside']
room['foyer'].north_to = room['overlook']
room['foyer'].east_to = room['narrow']
room['overlook'].south_to = room['foyer']
room['narrow'].west_to = room['foyer']
room['narrow'].north_to = room['treasure']
room['treasure'].south_to = room['narrow']

# Create all of the treasure options
coin = Item("Coin", "It has an oddly dark shimmer, and seems to be calling you, you also notice a footprint on the railing")
spoon = Item("Spoon", "It looks plastic, and seems to have been used")
harpoon = Item("Harpoon", "It's hanging from the wall, you wonder if it's ever been used before")
potion = Item("Potion", "It looks dark black and viscous")
notebook = Item("Notebook", "It looks to be covered in dust, but you see no creases on the binding to suggest it has ever been used")
rug = Item("Rug", "It begins to shimmer and move around, then suddenly envelops you... Or at least that's what you saw when you entered, but as you open your eyes again you see the rug laying there idly and think to yourself that you shoud maybe walk around thet rug instead of over it")

# Treasure Assignments
room['foyer'].items = [coin, spoon, harpoon, potion, notebook, rug]
print(room['treasure'].items)


player1 = Player("Frank", room["outside"])
# print(room['outside'])
# print(player1.current_room)

# entered = input(f"Hello, {player1.name}... Time for a little game... if you want to stop just enter 'end'... hopefully that will work")



print(room['outside'])

def check_room(player, direction):
    attribute = direction + '_to'
    if hasattr(player.current_room, attribute): 
        player.current_room = getattr(player.current_room, attribute)
        print(player1.current_room)
    else: 
        print("There doesn't seem to be anywhere to go over there, choose another direction")

    
print("Your choices are 'north', 'south', 'east', 'west', and 'end'....... Choose Carefully")

information = print(player1.current_room)

while True:
    information

    entered = input(f"|\nWhere would you like to go next, {player1.name}?")

    if entered == 'north':
        check_room(player1, entered)

    elif entered == 'south':
        check_room(player1, entered)

    elif entered == 'east':
        check_room(player1, entered)

    elif entered == 'west':
        check_room(player1, entered)

    elif entered == 'end':
        break
    else:
        print("I don't understand. Be sure you entered 'north', 'south', 'east' 'west', or 'end")






#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
