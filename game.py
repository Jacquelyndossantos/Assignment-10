import msvcrt
from colorama import Fore, Style, init
from combat import handle_combat
from database import load_user, save_game_data
from map import (
    EMOJI_TILES,
    MAPS,
    OBSTACLES,
    PORTALS,
    PLAYER,
    load_tiles,
)
from npc import interact_with_npc
from shop import open_shop

init(autoreset=True)

current_map = "forest"
game_map = []
ROWS = 0
COLS = 0
player_row = 1
player_col = 1
status_message = ""
player_data = {}


def get_key():
  """Read a keypress instantly on Windows without pressing Enter."""
  key = msvcrt.getch()
  if key in (b'\x00', b'\xe0'):
    key = msvcrt.getch()  # read the second byte of special keys
    return ""
  try:
    return key.decode("utf-8").lower()
  except UnicodeDecodeError:
    return ""


def intro():
  print(Fore.CYAN + Style.BRIGHT + "=" * 50)
  print(Fore.CYAN + Style.BRIGHT + "          THE LOST FOREST ADVENTURE")
  print(Fore.CYAN + Style.BRIGHT + "=" * 50)
  input(Fore.WHITE + "Press ENTER to continue...")
  print(Fore.YELLOW + "You wake up at the edge of an ancient forest.")
  input(Fore.WHITE + "Press ENTER to begin your journey...")


def clear_screen():
  print("\033[2J\033[H", end="")


def draw_map():
  clear_screen()
  title = MAPS[current_map]["title"]
  print(Fore.CYAN + Style.BRIGHT + f"=== {title} === Level: {player_data['level']} | HP: {player_data['hp']} | Gold: {player_data['gold']}")
  print()

  for row in range(ROWS):
    line = ""
    for col in range(COLS):
      if row == player_row and col == player_col:
        tile = PLAYER
      else:
        tile = game_map[row][col]
      if tile in EMOJI_TILES:
        line += Fore.CYAN + tile if tile == PLAYER else tile
      else:
        line += tile + " "
    print(line)

  print(Fore.WHITE + "\nControls: W/A/S/D=Move, P=Profile, I=Inventory, E=Shop (near NPC), Q=Quit")
  if status_message:
    print(Fore.YELLOW + status_message)


def switch_map(dest_map, spawn_row, spawn_col):
  global current_map, game_map, ROWS, COLS, player_row, player_col
  current_map = dest_map
  game_map = load_tiles(MAPS[current_map]["tiles"])
  ROWS = len(game_map)
  COLS = len(game_map[0])
  player_row = spawn_row
  player_col = spawn_col


def try_move(d_row, d_col):
  global player_row, player_col, status_message
  new_row = player_row + d_row
  new_col = player_col + d_col

  if not (0 <= new_row < ROWS and 0 <= new_col < COLS):
    return
  tile = game_map[new_row][new_col]

  if tile in OBSTACLES:
    status_message = "Blocked by an obstacle!"
    return

  player_row = new_row
  player_col = new_col
  status_message = ""

  if (current_map, player_row, player_col) in PORTALS:
    dest_map, sr, sc = PORTALS[(current_map, player_row, player_col)]
    switch_map(dest_map, sr, sc)
    status_message = f"Passed through portal to {MAPS[dest_map]['title']}!"
    return

  if tile == "👹":
    handle_combat(player_data)
  elif tile == "🧙":
    interact_with_npc(player_data)
  elif tile == "📦":
    status_message = "You found a treasure chest with 20 gold!"
    player_data["gold"] += 20
    game_map[player_row][player_col] = "."


def start_game(username):
  global player_data, current_map, game_map, ROWS, COLS, player_row, player_col
  player_data = load_user(username)
  current_map = player_data["current_map"]
  game_map = load_tiles(MAPS[current_map]["tiles"])
  ROWS = len(game_map)
  COLS = len(game_map[0])
  player_row = player_data["position"]["row"]
  player_col = player_data["position"]["col"]

  intro()

  try:
    while True:
      draw_map()
      move = get_key()
      if move == "w":
        try_move(-1, 0)
      elif move == "s":
        try_move(1, 0)
      elif move == "a":
        try_move(0, -1)
      elif move == "d":
        try_move(0, 1)
      elif move == "p":
        print(f"\n--- {username}'s Profile ---")
        print(f"Level: {player_data['level']}")
        print(f"XP: {player_data['xp']}")
        print(f"HP: {player_data['hp']}/{player_data['max_hp']}")
        print(f"Gold: {player_data['gold']}")
        input("Press ENTER to return...")
      elif move == "i":
        print(f"\n--- Inventory ---")
        if not player_data["inventory"]:
          print("Your inventory is empty.")
        else:
          for idx, item in enumerate(player_data["inventory"], 1):
            print(f"{idx}. {item}")
        
        choice = input("Enter item number to use (or press ENTER to go back): ").strip()
        if choice.isdigit():
          idx = int(choice) - 1
          if 0 <= idx < len(player_data["inventory"]):
            item_name = player_data["inventory"][idx]
            if item_name == "Health Potion":
              player_data["hp"] = min(player_data["max_hp"], player_data["hp"] + 30)
              player_data["inventory"].pop(idx)
              print("You drank the Health Potion and restored 30 HP!")
            else:
              print("That item cannot be used right now.")
            input("Press ENTER to continue...")
      elif move == "e":
        adjacent_coords = [
            (player_row - 1, player_col), (player_row + 1, player_col),
            (player_row, player_col - 1), (player_row, player_col + 1)
        ]
        near_npc = any(0 <= r < ROWS and 0 <= c < COLS and game_map[r][c] == "🧙" for r, c in adjacent_coords)
        if near_npc or game_map[player_row][player_col] == "🧙":
          open_shop(player_data)
        else:
          global status_message
          status_message = "You must be standing next to an NPC to open the shop!"
      elif move == "q":
        player_data["current_map"] = current_map
        player_data["position"] = {"row": player_row, "col": player_col}
        save_game_data(username, player_data)
        print("Game saved. Goodbye!")
        break
      save_game_data(username, player_data)
  except KeyboardInterrupt:
    player_data["current_map"] = current_map
    player_data["position"] = {"row": player_row, "col": player_col}
    save_game_data(username, player_data)
    print("\nGame saved safely. Goodbye!")