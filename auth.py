import hashlib
from database import load_user, register_user


def hash_password(password):
  return hashlib.sha256(password.encode()).hexdigest()


def login_menu():
  while True:
    print("\n1. Login")
    print("2. Register")
    print("3. Quit")
    choice = input("Select an option (1-3): ").strip()

    if choice == "1":
      username = input("Username: ").strip()
      password = input("Password: ").strip()
      user = load_user(username)
      if user and user["password"] == hash_password(password):
        print(f"Welcome back, {username}!")
        return username
      print("Invalid username or password.")

    elif choice == "2":
      username = input("Choose a Username: ").strip()
      if load_user(username):
        print("Username already exists.")
        continue
      password = input("Choose a Password: ").strip()
      register_user(username, hash_password(password))
      print("Registration successful! You can now log in.")

    elif choice == "3":
      return None
    else:
      print("Invalid choice. Please enter 1, 2, or 3.")
