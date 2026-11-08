PLAYER = "👤"
TREE = "🌲"
ROCK = "🗿"
MONSTER = "👹"
NPC = "🧙"
CHEST = "📦"

TILE_FROM_LETTER = {"T": TREE, "R": ROCK, "M": MONSTER, "N": NPC, "C": CHEST}
EMOJI_TILES = {PLAYER, TREE, ROCK, MONSTER, NPC, CHEST}
OBSTACLES = {"#", TREE, ROCK}

MAPS = {
    "forest": {
        "title": "LOST FOREST",
        "tiles": [
            "####################",
            "#........T.........#",
            "#..M..........C....#",
            "#.......##.........#",
            "#..N....##....R....#",
            "#...................",
            "#....T.............#",
            "#.........N........#",
            "#..C..........T....#",
            "#..................#",
            "####################",
        ],
    },
    "cave": {
        "title": "DARK CAVE",
        "tiles": [
            "####################",
            "#....R........M....#",
            "#..C...............#",
            "#......####........#",
            "#......####...N....#",
            "...................#",
            "#........T.........#",
            "#..M..........C....#",
            "#.............R....#",
            "#.........N........#",
            "####################",
        ],
    },
}

PORTALS = {
    ("forest", 5, 19): ("cave", 5, 1),
    ("cave", 5, 0): ("forest", 5, 18),
}


def load_tiles(raw_tiles):
  return [[TILE_FROM_LETTER.get(ch, ch) for ch in row] for row in raw_tiles]