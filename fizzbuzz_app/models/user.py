# models/user.py
import json
import hashlib
import os
from config.settings import Settings

class UserModel:
    def __init__(self):
        self.users_file = Settings.DB_PATH
        os.makedirs(os.path.dirname(self.users_file), exist_ok=True)
        self.current_user = None
        self.load_users()

    def load_users(self):
        if not os.path.exists(self.users_file):
            self.users = {}
            self.save_users()
        else:
            with open(self.users_file, 'r') as f:
                self.users = json.load(f)

    def save_users(self):
        with open(self.users_file, 'w') as f:
            json.dump(self.users, f)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username, password):
        if username in self.users:
            return False
        self.users[username] = self.hash_password(password)
        self.save_users()
        return True

    def login(self, username, password):
        if username in self.users and self.users[username] == self.hash_password(password):
            self.current_user = username
            return True
        return False
