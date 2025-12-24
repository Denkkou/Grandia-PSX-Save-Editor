from enum import Enum

# Characters and their location within the save file
# Get location through Character.JUSTIN.value
class Character(Enum):
    JUSTIN  = 0x310 #01
    FEENA   = 0x390 #02
    SUE     = 0x410 #03
    GADWIN  = 0x490 #04
    RAPP    = 0x510 #05
    #6      = 0x590 #06
    #7      = 0x610 #07
    LIETE   = 0x690 #08

# Character overworld groups are hard-coded combinations
class Lineup(Enum):
    JS      = 0x1
    JSF     = 0x2
    JF      = 0x3
    JSFR    = 0x4
    JSFG    = 0x5
    JL      = 0x6
    JFG     = 0x8
    JFR     = 0x9
    JFRM    = 0xA
    JFRG    = 0xC
    JRG     = 0xE
    JFRL    = 0xF
    JRL     = 0x10

# Relative offsets from start of character's data block
class Offset(Enum):
    LEVEL       = 0x03  # 1 Byte
    TOTAL_XP    = 0x34  # 4 Bytes Little-endian
    NEXT_XP     = 0x08  # 2 Bytes Little-endian

    MAX_HP      = 0x0A  # 2 bytes Little-endian
    HP          = 0x0C  # 2 bytes Little-endian

    STR         = 0x0E  # 2 bytes
    VIT         = 0x10  # 2 bytes
    WIT         = 0x12  # 2 bytes
    AGI         = 0x14  # 2 bytes

    MAX_SP      = 0x16  # 2 Bytes Little-endian
    SP          = 0x18  # 2 Bytes Little-endian

    WPN_1_XP    = 0x24  # 2 Bytes Little-endian
    WPN_2_XP    = 0x26  # 2 Bytes Little-endian
    WPN_3_XP    = 0x28  # 2 Bytes Little-endian

    WPN_1_LVL   = 0x30  # 1 Byte
    WPN_2_LVL   = 0x31  # 1 Byte
    WPN_3_LVL   = 0x32  # 1 Byte

    FIRE_XP     = 0x1C  # 2 Bytes Little-endian
    WATER_XP    = 0x1E  # 2 Bytes Little-endian
    WIND_XP     = 0x20  # 2 Bytes Little-endian
    EARTH_XP    = 0x22  # 2 Bytes Little-endian

    FIRE_LVL    = 0x2C  # 1 Byte
    WATER_LVL   = 0x2D  # 1 Byte
    WIND_LVL    = 0x2E  # 1 Byte
    EARTH_LVL   = 0x2F  # 1 Byte

    # WEAPON # 2 Bytes Little-endian
    # SHIELD # 2 Bytes Little-endian
    # ARMOUR # 2 Bytes Little-endian
    # HELMET # 2 Bytes Little-endian
    # SHOES # 2 Bytes Little-endian
    # JEWELRY # 2 Bytes Little-endian

    # ITEM_1 # 2 Bytes Little-endian
    # ITEM_2 # 2 Bytes Little-endian
    # ...
    # ITEM_16 # 2 Bytes Little-endian

# Misc save file data locations
MONEY   = 0x1B0 # 4 Bytes, Little-endian
LINEUP  = 0x1A8 # Where the lineup value is stored
DISK    = 0x1A9 # 1 or 2

# Characters in the party
# Changing these values DOES NOT change portraits
# TODO Find where the portraits are saved!!!
PARTY_CHAR_1 = 0x1AC
PARTY_CHAR_2 = 0x1AD
PARTY_CHAR_3 = 0x1AE
PARTY_CHAR_4 = 0x1AF