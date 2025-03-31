import hashlib
import json
import os
import base64
import bcrypt
from argon2 import PasswordHasher

# Load config
def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def get_secret_pepper_from_config():
    return load_config()["pepper"]

def get_hash_algorithm_from_config():
    return load_config().get("algorithm", "sha256")

# Database helpers
def load_database():
    if not os.path.exists("users.json"):
        return {}
    with open("users.json", "r") as f:
        return json.load(f)

def save_database(db):
    with open("users.json", "w") as f:
        json.dump(db, f, indent=4)

# Salt generator (Base64)
def generate_random_salt():
    return base64.b64encode(os.urandom(16)).decode()

# Hashing dispatcher
def hash_password(password, salt, pepper):
    algorithm = get_hash_algorithm_from_config()
    combined = (password + pepper + salt).encode()

    if algorithm == "sha256":
        return hashlib.sha256(combined).hexdigest()
    elif algorithm == "bcrypt":
        return bcrypt.hashpw(combined, bcrypt.gensalt()).decode()
    elif algorithm == "argon2":
        ph = PasswordHasher()
        return ph.hash((password + pepper + salt))
    else:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

# Hash verification
def verify_hash(password, salt, pepper, stored_hash):
    algorithm = get_hash_algorithm_from_config()
    combined = (password + pepper + salt).encode()

    if algorithm == "sha256":
        return hashlib.sha256(combined).hexdigest() == stored_hash
    elif algorithm == "bcrypt":
        return bcrypt.checkpw(combined, stored_hash.encode())
    elif algorithm == "argon2":
        ph = PasswordHasher()
        try:
            ph.verify(stored_hash, (password + pepper + salt))
            return True
        except Exception:
            return False
    else:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

# Register user
def register_user(username, password):
    db = load_database()
    if username in db:
        raise ValueError("User already exists.")

    salt = generate_random_salt()
    pepper = get_secret_pepper_from_config()
    hashed = hash_password(password, salt, pepper)

    db[username] = {
        "salt": salt,
        "hash": hashed
    }
    save_database(db)
    print(f"User '{username}' registered.")

# Verify login
def verify_login(username, password):
    db = load_database()
    if username not in db:
        return False

    salt = db[username]["salt"]
    stored_hash = db[username]["hash"]
    pepper = get_secret_pepper_from_config()

    return verify_hash(password, salt, pepper, stored_hash)
