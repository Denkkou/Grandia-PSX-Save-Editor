# The character is a more granular slice of a save file.
# It contains the offsets for each in-game value, like stats and items
# to allow direct access

# Constants for the location of each stat relative to start
# ...

class Character:
    def __init__(self, character_data):
        self.data = character_data

    # Getters and Setters for each stat
    # ...
