from save_file import *

# Memory card data blank after 0xAE80
DATA_READ_AMOUNT = 0xAE80

SAVE_DATA_SIZE = 0xE80

# The ledger order is the order of creation
# The number at these values (0 to 4) determines which
# save file slot is at that location (slots 1 to 5)
LEDGER_ADDRESSES = [0x9C, 0x11C, 0x19C, 0x21C, 0x29C]

class MemoryCard:
    def __init__(self):
        self.data_size = DATA_READ_AMOUNT
        self.save_order = []
        self.saves = []


    def load_file(self, filepath):
        file = open(filepath, "rb")
        self.data = file.read(self.data_size)
        file.close()


    def order_saves(self):
        index = 0
        for l in LEDGER_ADDRESSES:
            value = self.data[l]
            if value != 0x00:
                # Create a tuple containing the ledger, and the address locating its save
                save_number = int(chr(value))
                save_location = (0x2000 + (0x2000 * index))
                self.save_order.append((save_number, save_location))
            else:
                self.save_order.append(None)
            index += 1

        # Sort numerically
        self.save_order.sort(key = lambda x: x[0])


    def extract_saves(self):
        # Locate and order save data
        self.order_saves()
        print(*self.save_order)

        # Create correctly ordered list of save files
        for s in self.save_order:
            if s is not None:
                # Use address found in tuple to slice data
                save_data = self.data[s[1]:s[1]+SAVE_DATA_SIZE]
                save_file = SaveFile(save_data)
                self.saves.append(save_file)
            else:
                self.saves.append(None)
    
    # This function will modify its self.data field
    # by patching in the reassembled outputs of each
    # save file in self.saves, by calling their reassemble_ functions
    def reassemble_memory_card(self):
        # ...
        return self.data

    def dump_data(self):
        counter = 0
        for byte in self.data:
            counter += 1
            if counter < 16:
                if counter == 9: print(" ", end = "")
                print("{:02X}".format(byte), end = " ")
            else:
                print("{:02X}".format(byte))
                counter = 0