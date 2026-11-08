from auth import login_menu
from game import start_game


def main():
  print("\033[2J\033[H", end="")
  print("=== WELCOME TO TERMINAL RPG ===")
  username = login_menu()
  if username:
    start_game(username)


if __name__ == "__main__":
  main()