from item import ITEMS


def open_shop(player_data):
  print("\n--- SHOP ---")
  for name, info in ITEMS.items():
    print(f"- {name}: {info['cost']} gold")

  choice = input(
      "Enter item name to buy (or press ENTER to exit): "
  ).strip().title()
  if choice in ITEMS:
    item = ITEMS[choice]
    if player_data["gold"] >= item["cost"]:
      player_data["gold"] -= item["cost"]
      player_data["inventory"].append(choice)
      print(f"Successfully purchased {choice}!")
    else:
      print("Not enough gold!")
  input("Press ENTER to exit shop...")