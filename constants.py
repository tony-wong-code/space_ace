SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

N_SHIPS_PER_TIER = (18, 15, 15, 12, 9, 6)
N_SHIPS_IN_MARKET_PER_TIER = (3, 6, 9, 12, 15, 18)

HANGAR = 0
HANGAR_BLOCK_SIZE = (80, 80)
HANGAR_BLOCK_PADDING = 20
HANGAR_BOTTOM_PADDING = 10
HANGAR_OUTLINE_THICKNESS = 3
HANGAR_SIZE = (10, 1)
HANGAR_RECT_SIZE = (
    HANGAR_SIZE[0]*HANGAR_BLOCK_SIZE[0] + (HANGAR_SIZE[0] + 1)*HANGAR_BLOCK_PADDING,
    HANGAR_SIZE[1]*HANGAR_BLOCK_SIZE[1] + (HANGAR_SIZE[1] + 1)*HANGAR_BLOCK_PADDING
)
HANGAR_RECT_OUTLINE_SIZE = (
    HANGAR_RECT_SIZE[0] + 2*HANGAR_OUTLINE_THICKNESS,
    HANGAR_RECT_SIZE[1] + 2*HANGAR_OUTLINE_THICKNESS
)
HANGAR_RECT_POS = (
    (SCREEN_WIDTH - HANGAR_RECT_SIZE[0]) // 2,
    SCREEN_HEIGHT - HANGAR_RECT_SIZE[1] - HANGAR_BOTTOM_PADDING
)
HANGAR_RECT_OUTLINE_POS = (
    HANGAR_RECT_POS[0] - HANGAR_OUTLINE_THICKNESS,
    HANGAR_RECT_POS[1] - HANGAR_OUTLINE_THICKNESS
)
HANGAR_RECT_OBJ_POS = (
    HANGAR_RECT_POS[0] + HANGAR_BLOCK_PADDING,
    HANGAR_RECT_POS[1] + HANGAR_BLOCK_PADDING
)

COLOR_HANGAR_OUTLINE = (88, 94, 98)
COLOR_HANGAR = (58, 65, 71)

BATTLE = 1
BATTLE_BLOCK_SIZE = (125, 125)
BATTLE_BLOCK_PADDING = 20
BATTLE_BOTTOM_PADDING = HANGAR_RECT_SIZE[1] + 100
BATTLE_OUTLINE_THICKNESS = 3
BATTLE_SIZE = (7, 1)
BATTLE_RECT_SIZE = (
    BATTLE_SIZE[0]*BATTLE_BLOCK_SIZE[0] + (BATTLE_SIZE[0] + 1)*BATTLE_BLOCK_PADDING,
    BATTLE_SIZE[1]*BATTLE_BLOCK_SIZE[1] + (BATTLE_SIZE[1] + 1)*BATTLE_BLOCK_PADDING
)
BATTLE_RECT_OUTLINE_SIZE = (
    BATTLE_RECT_SIZE[0] + 2*BATTLE_OUTLINE_THICKNESS,
    BATTLE_RECT_SIZE[1] + 2*BATTLE_OUTLINE_THICKNESS
)
BATTLE_RECT_POS = (
    (SCREEN_WIDTH - BATTLE_RECT_SIZE[0]) // 2,
    SCREEN_HEIGHT - BATTLE_RECT_SIZE[1] - BATTLE_BOTTOM_PADDING
)
BATTLE_RECT_OUTLINE_POS = (
    BATTLE_RECT_POS[0] - BATTLE_OUTLINE_THICKNESS,
    BATTLE_RECT_POS[1] - BATTLE_OUTLINE_THICKNESS
)
BATTLE_RECT_OBJ_POS = (
    BATTLE_RECT_POS[0] + BATTLE_BLOCK_PADDING,
    BATTLE_RECT_POS[1] + BATTLE_BLOCK_PADDING
)

COLOR_BATTLE_OUTLINE = (88, 94, 98)
COLOR_BATTLE = (58, 65, 71)

MARKET = 2
MARKET_BLOCK_SIZE = (80, 80)
MARKET_BLOCK_PADDING = 20
MARKET_TOP_PADDING = 50
MARKET_LEFT_PADDING = 125
MARKET_OUTLINE_THICKNESS = 3
MARKET_SIZE = (6, 3)
MARKET_RECT_SIZE = (
    MARKET_SIZE[0]*MARKET_BLOCK_SIZE[0] + (MARKET_SIZE[0] + 1)*MARKET_BLOCK_PADDING,
    MARKET_SIZE[1]*MARKET_BLOCK_SIZE[1] + (MARKET_SIZE[1] + 1)*MARKET_BLOCK_PADDING
)
MARKET_RECT_OUTLINE_SIZE = (
    MARKET_RECT_SIZE[0] + 2*MARKET_OUTLINE_THICKNESS,
    MARKET_RECT_SIZE[1] + 2*MARKET_OUTLINE_THICKNESS
)
MARKET_RECT_POS = (
    MARKET_LEFT_PADDING,
    MARKET_TOP_PADDING
)
MARKET_RECT_OUTLINE_POS = (
    MARKET_RECT_POS[0] - MARKET_OUTLINE_THICKNESS,
    MARKET_RECT_POS[1] - MARKET_OUTLINE_THICKNESS
)
MARKET_RECT_OBJ_POS = (
    MARKET_RECT_POS[0] + MARKET_BLOCK_PADDING,
    MARKET_RECT_POS[1] + MARKET_BLOCK_PADDING
)

COLOR_MARKET_OUTLINE = (88, 94, 98)
COLOR_MARKET = (58, 65, 71)
COLOR_MARKET_TILE = (105, 169, 157)
MARKET_TILE_X_OFFSET = 8
MARKET_TILE_Y_OFFSET = 8

SHIP_BLOCK_SIZE = (90, 90)