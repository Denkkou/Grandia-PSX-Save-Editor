from data_mappings import *

class SaveFile:
    def __init__(self, save_data):
        self.data = save_data
    
    #### Save file specific values ####

    def get_savefile_value(self, target, size, order='little'):
        return int.from_bytes(self.data[target:target + size], order)

    def set_savefile_value(self, target, value, size, order='little'):
        bytes_to_set = value.to_bytes(size, order)
        place = 0
        for b in bytes_to_set:
            self.data[target + place] = b
            place += 1   


    #### Character specific values ####

    def get_character_value(self, character, offset, size, order='little'):
        target = character.value + offset.value
        return int.from_bytes(self.data[target:target + size], order)

    def set_character_value(self, character, offset, value, size, order='little'):
        bytes_to_set = value.to_bytes(size, order)
        target = character.value + offset.value
        place = 0
        for b in bytes_to_set:
            self.data[target + place] = b
            place += 1



    # Possibly needed when rebuilding the memory card file
    def export_save_file(self):
        return self.data