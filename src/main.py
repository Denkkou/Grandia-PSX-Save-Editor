from memory_card import *

memcard = MemoryCard()

memcard.load_file("saves_unordered.srm")

#memcard.dump_data()

memcard.extract_saves()
memcard.saves[0].set_level(Character.SUE, 50)
print(memcard.saves[0].get_level(Character.SUE))
