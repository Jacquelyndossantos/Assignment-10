from tinydb import Query, TinyDB

db = TinyDB("rpg_database.json")
users_table = db.table("users")


def register_user(username, password_hash):
  users_table.insert({
      "username": username,
      "password": password_hash,
      "level": 1,
      "xp": 0,
      "hp": 100,
      "max_hp": 100,
      "gold": 50,
      "inventory": ["Health Potion"],
      "skills": ["Fireball", "Heal"],
      "current_map": "forest",
      "quest_progress": {"main": 0, "side1": 0, "side2": 0},
      "position": {"row": 1, "col": 1},
  })


def load_user(username):
  User = Query()
  result = users_table.get(User.username == username)
  return result


def save_game_data(username, data):
  User = Query()
  users_table.update(data, User.username == username)