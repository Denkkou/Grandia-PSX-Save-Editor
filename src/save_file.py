from data_mappings import *

class SaveFile:
    def __init__(self, save_data):
        self.data = save_data
    
    #### Save file specific values ####

    def get_money(self):
        return int.from_bytes(self.data[MONEY:MONEY+4], byteorder = 'little')
    
    def set_money(self, value):
        bytes = value.to_bytes(4, byteorder = 'little')
        place = 0
        for b in bytes:
            self.data[MONEY + place] = b
            place += 1



    #### Character specific values ####

    def get_level(self, character): 
        return self.data[character.value + Offsets.LEVEL.value]
    
    def set_level(self, character, value):
        self.data[character.value + Offsets.LEVEL.value] = value



    # Possibly needed when rebuilding the memory card file
    def export_save_file(self):
        return self.data