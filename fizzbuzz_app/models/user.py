# Import necessary libraries
import json
import hashlib
import os
from config.settings import Settings  # Likely contains database settings

# Define a class called UserModel
class UserModel:

    # Initialize the user model
    def __init__(self):
        # Get the database path from Settings
        self.users_file = Settings.DB_PATH

        # Ensure the directory for the database file exists
        os.makedirs(os.path.dirname(self.users_file), exist_ok=True)

        # Initialize variables
        self.current_user = None  # Stores the currently logged-in user
        self.users = {}  # Dictionary to store usernames and hashed passwords

        # Load user data from the database file
        self.load_users()

    # Load user data from the JSON file
    def load_users(self):
        # Check if the database file exists
        if not os.path.exists(self.users_file):
            # Initialize an empty dictionary for users if file doesn't exist
            self.users = {}
            # Save the empty dictionary to the database file
            self.save_users()
        else:
            # Open the file for reading
            with open(self.users_file, 'r') as f:
                # Load the user data from the JSON file
                self.users = json.load(f)

    # Save user data to the JSON file
    def save_users(self):
        # Open the file for writing
        with open(self.users_file, 'w') as f:
            # Dump the user data dictionary to the JSON file
            json.dump(self.users, f)

    # Hash a password using SHA-256
    def hash_password(self, password):
        # Encode the password as bytes and apply SHA-256 hashing
        # Returning the hexadecimal representation of the hash digest
        return hashlib.sha256(password.encode()).hexdigest()

    # Register a new user
    def register(self, username, password):
        # Check if the username already exists
        if username in self.users:
            # Return False if username is already taken
            return False

        # Hash the password using the hash_password method
        hashed_password = self.hash_password(password)

        # Store the username and hashed password in the user dictionary
        self.users[username] = hashed_password

        # Save the updated user data to the database file
        self.save_users()

        # Return True on successful registration
        return True

    # Login a user
    def login(self, username, password):
        # Check if the username exists and the password matches (hashed)
        if username in self.users and self.users[username] == self.hash_password(password):
            # Set the current user variable
            self.current_user = username

            # Return True on successful login
            return True

        # Return False on invalid credentials
        return False