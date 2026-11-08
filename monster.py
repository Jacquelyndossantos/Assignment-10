class Monster:

  def __init__(self, name, hp, attack, xp_reward, gold_reward):
    self.name = name
    self.hp = hp
    self.attack = attack
    self.xp_reward = xp_reward
    self.gold_reward = gold_reward


class Goblin(Monster):

  def __init__(self):
    super().__init__("Goblin", 30, 8, 15, 10)


class Orc(Monster):

  def __init__(self):
    super().__init__("Orc", 50, 12, 30, 20)


class Skeleton(Monster):

  def __init__(self):
    super().__init__("Skeleton", 40, 10, 25, 15)


class Dragon(Monster):

  def __init__(self):
    super().__init__("Dragon", 80, 18, 60, 50)


class Boss(Monster):

  def __init__(self):
    super().__init__("Dark Overlord (Final Boss)", 150, 25, 200, 500)