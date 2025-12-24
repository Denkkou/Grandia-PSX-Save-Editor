from memory_card import *

memcard = MemoryCard()

memcard.load_file("saves_unordered.srm")

#memcard.dump_data()

memcard.extract_saves()


# Testing

# by setting a current character, the UI can reuse the same code to populate
# its fields whenever we select someone else
current_character = Character.SUE

memcard.saves[0].set_level(current_character, 50)
print(memcard.saves[0].get_level(current_character.SUE))

memcard.saves[0].set_money(2570)
print(memcard.saves[0].get_money())
