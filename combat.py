import random
from monster import Boss, Dragon, Goblin, Orc, Skeleton


def handle_combat(player_data):
  monsters = [Goblin(), Orc(), Skeleton(), Dragon(), Boss()]
  monster = random.choice(monsters)
  print(f"\nA wild {monster.name} appears!")

  while monster.hp > 0 and player_data["hp"] > 0:
    print(f"\n{monster.name} HP: {monster.hp} | Your HP: {player_data['hp']}")
    action = input("Actions: [1] Attack [2] Run: ").strip()

    if action == "1":
      damage = random.randint(10, 20)
      monster.hp -= damage
      print(f"You hit {monster.name} for {damage} damage.")
    elif action == "2":
      print("You fled safely!")
      return
    else:
      print("Invalid action.")

    if monster.hp > 0:
      player_data["hp"] -= monster.attack
      print(f"{monster.name} hits you for {monster.attack} damage.")

  if player_data["hp"] <= 0:
    print("You have been defeated...")
    player_data["hp"] = 50  # Respawn penalty
  else:
    print(f"Victory! You defeated {monster.name}.")
    player_data["gold"] += monster.gold_reward
    player_data["xp"] += monster.xp_reward
    print(
        f"Gained {monster.gold_reward} gold and {monster.xp_reward} experience!"
    )
    input("Press ENTER to continue...")