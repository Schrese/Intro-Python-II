# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = 'empty'
        self.s_to = 'empty'
        self.e_to = 'empty'
        self.w_to = 'empty'