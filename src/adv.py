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


# While the game is going: 
# while not stop_play:

# Print current room name and description
    # Print next options
print("Right now you are in the %s and %s" % (room[player1.current_room].name, room[player1.current_room].description))


# player inputs direction they want to move in 
    # print if direction is available to the player
        # set current room to this new room
new_direc = input("Where would you like to go next? North, South, East, or West? Choose Wisely...")
print(new_direc)
if room[player1.current_room].new_direc == "empty":
    print('there is no room there') 
    # if direction is not available, have them pick another direction
else:
    player1.current_room == room[player1.current_room].new_direc






# Player ends the game
