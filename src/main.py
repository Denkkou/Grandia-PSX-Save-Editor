from memory_card import *

memcard = MemoryCard()

memcard.load_file("saves_unordered.srm")

memcard.extract_saves()


# Testing

# by setting a current character, the UI can reuse the same code to populate
# its fields whenever we select someone else
curr_char = Character.JUSTIN

print(memcard.saves[0].get_character_value(curr_char.value, Offsets.LEVEL.value, 1))
# Expect 10

print(memcard.saves[0].get_character_value(curr_char.value, Offsets.TOTAL_XP.value, 4, 'little'))
# Expect 4387

memcard.saves[0].set_character_value(
    curr_char.value, 
    Offsets.TOTAL_XP.value, 
    5555, 
    4, 
    'little'
)
print(memcard.saves[0].get_character_value(
    curr_char.value, 
    Offsets.TOTAL_XP.value, 
    4, 'little'
    )
)
# Expect 5555

memcard.saves[0].set_savefile_value(MONEY, 99999, 4, 'little')
print(memcard.saves[0].get_savefile_value(MONEY, 4, 'little'))
# Expect 99999

#memcard.dump_data(0)