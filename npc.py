from quest import QUESTS


def interact_with_npc(player_data):
  print("\n🧙 NPC Dialogue:")
  dialogues = [
      "Welcome traveler! Beware of monsters lurking in the shadows.",
      "The dark cave holds ancient treasures, but great peril awaits.",
      "Can you help clear out the goblins nearby?",
      "Have you visited the shop to upgrade your gear?",
      "Defeat the Dark Overlord to bring peace back to our land!",
  ]
  import random

  print(f'"{random.choice(dialogues)}"')
  input("Press ENTER to finish talking...")