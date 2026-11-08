class Skill:

  def __init__(self, name, cost):
    self.name = name
    self.cost = cost


class Fireball(Skill):

  def __init__(self):
    super().__init__("Fireball", 15)

  def use(self, monster):
    damage = 35
    monster.hp -= damage
    print(f"Cast Fireball dealing {damage} magic damage!")


class Heal(Skill):

  def __init__(self):
    super().__init__("Heal", 10)

  def use(self, player_data):
    heal_amt = 30
    player_data["hp"] = min(player_data["max_hp"], player_data["hp"] + heal_amt)
    print(f"Cast Heal restoring {heal_amt} HP!")