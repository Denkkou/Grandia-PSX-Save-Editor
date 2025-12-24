from memory_card import *

memcard = MemoryCard()
memcard.load_file("saves_unordered.srm")
memcard.extract_saves()


#### Testing ####

def test_getters():
    money = memcard.saves[0].get_savefile_value(MONEY, 4)

    if money == 13030:
        print("Money value correct!")

    level = memcard.saves[0].get_character_value(c, Offset.LEVEL, 1, 'big')
    xp_next = memcard.saves[0].get_character_value(c, Offset.NEXT_XP, 2)
    total_xp = memcard.saves[0].get_character_value(c, Offset.TOTAL_XP, 4)

    if level == 10 and xp_next == 1385 and total_xp == 4387:
        print("Level and XP values correct!")

    str = memcard.saves[0].get_character_value(c, Offset.STR, 1, 'big')
    vit = memcard.saves[0].get_character_value(c, Offset.VIT, 1, 'big')
    wit = memcard.saves[0].get_character_value(c, Offset.WIT, 1, 'big')
    agi = memcard.saves[0].get_character_value(c, Offset.AGI, 1, 'big')

    if str == 50 and vit == 20 and wit == 48 and agi == 26:
        print("Stat values correct!")

# by setting a current character, the UI can reuse the same code to populate
# its fields whenever we select someone else
c = Character.JUSTIN
test_getters()
