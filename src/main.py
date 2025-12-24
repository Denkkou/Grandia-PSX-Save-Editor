from memory_card import *

memcard = MemoryCard()

memcard.load_file("saves_unordered.srm")

#memcard.dump_data()

memcard.extract_saves()

# Example access down to a character's stat
# memcard.saves[0].characters[JUSTIN].get_hp()
#
# Or to the save file's money value
# memcard.saves[3].set_money(9999)
