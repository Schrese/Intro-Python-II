from room import Room
from player import Player

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

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

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



# MY OWN STUFF
# Making sure that everything works
# player1 = Player('Hugo', "outside")
# player1.current_room = "outside"

# player1.current_room = room["foyer"].name

# print(player1.current_room)
# print(room["outside"].name)

# for i in room:
#     # print(dir(i[0]))
#     print(i)
 



# create input variable

# create a new player
player1 = Player('Hugo', "outside")

# set value for gamestate
stop_play = False

# player starts the game
    # print instructions
print("Welcom to this game... %s" % (player1.name))
print("You'll be trying to find your way out of this house... if there is a way...")
print("I'll just need a bit of input from you...")
print("Are you ready? ")
print("GOOD!")
print("remember, you can always quit the game by entering 'q'")

empty = 'empty' # only uses one memory slot instead of holding each string in the stack


# While the game is going: 
# while not stop_play:

# Print current room name and description
    # Print next options
print("Right now you are in the %s and %s" % (room[player1.current_room].name, room[player1.current_room].description))

def prtcurrent(curroom): 
    print("Right now you are in the %s and %s" % (room[player1.current_room].name, room[player1.current_room].description))

# player inputs direction they want to move in 
    # print if direction is available to the player
        # set current room to this new room
new_direc = input("Where would you like to go next? North, South, East, or West? Choose Wisely...")
print(new_direc)
# if new_direc == 'north':
#     # if direction is not available, have them pick another direction
#     if room[player1.current_room].n_to == empty:
#         print('there is no room there') 

#     # otherwise set the current room to the "n_to" room
#     else:
#         new_room = room[player1.current_room].n_to
#         print(new_room)
#         print(player1.current_room)
# Overlook || Treasure
# Foyer    || Narrow
# Outside

# if player current room is outside, then north goes to foyer
if player1.current_room == 'outside':
    if new_direc == 'north':
        player1.current_room = 'foyer'
        prtcurrent(player1.current_room)
        new_direc = input("Where would you like to go next? North, South, East, or West? Choose Wisely...")
    else:
        new_direc = input("Where would you like to go next? North, South, East, or West? Choose Wisely...")
# if player current room is foyer, then north goes to overlook, east goes to narrow, south goes to outside
if player1.current_room == 'foyer':
    if new_direc == 'north':
        player1.current_room = 'overlook'
        prtcurrent(player1.current_room)
    elif new_direc == 'east':
        player1.current_room = 'narrow'
        prtcurrent(player1.current_room)
    elif new_direc == 'south':
        player1.current_room = 'outside'
    else:
        print("You stare at an empty wall... You wonder how long it's been there...")
        new_direc = input("Where would you like to go next? North, South, East, or West? Choose Wisely...") 
# player current room is overlook, then east goes to treasure, south goes to foyer

# player current room is treasure, then west goes to overlook, south goes to narrow

# player current room is narow, then west goes to foyer, north goes to outside



# Player ends the game
