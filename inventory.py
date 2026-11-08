def view_inventory(player_data):
  print("\n--- Inventory ---")
  for idx, item in enumerate(player_data["inventory"], 1):
    print(f"{idx}. {item}")