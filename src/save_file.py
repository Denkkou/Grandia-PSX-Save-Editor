from character import *

# A single save file extracted from a memory card

# Constants for the location of save file data relative to start
# ...
# MONEY, PLAY_TIME, PARTY_LINEUP etc...

# Constants for the location of character data relative to start
# ...
# JUSTIN_LOCATION = 0x???
CHARACTER_DATA_SIZE = 0x80

class SaveFile:
    characters = []
    
    def __init__(self, save_data):
        self.data = save_data
        # eg. c_Justin = Character(save_data[offset:offset+size])
        # self.characters.append(c_Justin)

    # Getters and setters for save file values
    # ...

    # This function modifies the self.data field by
    # applying whatever changes exist within this save file
    # AND within each character
    def reassemble_save_file(self):
        #...
        return self.data