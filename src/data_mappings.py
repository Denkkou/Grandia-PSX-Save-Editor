from enum import Enum

# Characters and their location within the save file
# Get location through Character.JUSTIN.value
class Character(Enum):
    JUSTIN = 0x310  #01
    FEENA = 0x390   #02
    SUE = 0x410     #03
    GADWIN = 0x490  #04
    RAPP = 0x510    #05
    #6 = 0x590      #06
    #7 = 0x610      #07
    LIETE = 0x690   #08

# Character overworld groups are hard-coded combinations
class Lineup(Enum):
    JS = 0x1
    JSF = 0x2
    JF = 0x3
    JSFR = 0x4
    JSFG = 0x5
    JL = 0x6
    JFG = 0x8
    JFR = 0x9
    JFRM = 0xA
    JFRG = 0xC
    JRG = 0xE
    JFRL = 0xF
    JRL = 0x10

# RELATIVE offsets from character location start
# Usage: CHARACTER + OFFSET = character's value
# Size: 1 byte unless otherwise stated
# Order: Big-endian unless otherwise stated
class Offsets(Enum):
    LEVEL = 0x03
    TOTAL_XP = 0x34 # 4 Bytes Little-endian
    NEXT_XP = 0x8   # 2 Bytes Little-endian

    # MAX_HP        # 2 bytes Little-endian
    # HP            # 2 bytes Little-endian

    # STR           # 2 bytes
    # VIT           # 2 bytes
    # WIT           # 2 bytes
    # AGI           # 2 bytes

    # MAX_SP        # 2 Bytes Little-endian
    # SP            # 2 Bytes Little-endian

    # WPN_1_XP      # 2 Bytes Little-endian
    # WPN_2_XP      # 2 Bytes Little-endian
    # WPN_3_XP      # 2 Bytes Little-endian

    # WPN_1_LVL
    # WPN_2_LVL
    # WPN_3_LVL

    # FIRE_MAGIC_XP     # 2 Bytes Little-endian
    # WATER_MAGIC_XP    # 2 Bytes Little-endian
    # WIND_MAGIC_XP     # 2 Bytes Little-endian
    # EARTH_MAGIC_XP    # 2 Bytes Little-endian

    # FIRE_MAGIC_LVL
    # WATER_MAGIC_LVL
    # WIND_MAGIC_LVL
    # EARTH_MAGIC_LVL

    # EQUIP_WEAPON
    # EQUIP_SHIELD
    # EQUIP_ARMOUR
    # EQUIP_HELMET
    # EQUIP_SHOES
    # EQUIP_JEWELRY

    # ITEM_1
    # ITEM_2
    # ...
    # ITEM_16

# Misc save file data locations
MONEY = 0x1B0 # 4 Bytes, Little-endian
LINEUP = 0x1A8 # Where the lineup value is stored
DISK = 0x1A9 # 1 or 2

# Characters in the party
# Changing these values DOES NOT change portraits
PARTY_CHAR_1 = 0x1AC
PARTY_CHAR_2 = 0x1AD
PARTY_CHAR_3 = 0x1AE
PARTY_CHAR_4 = 0x1AF