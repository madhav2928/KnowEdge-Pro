import os
from dotenv import dotenv_values, set_key

def update_config(updates: dict[str, str], env_path=".env"):
    """
    Updates multiple keys in the .env file and refreshes the environment.

    Args:
        updates: dict of environment variable keys and their new values.
        env_path: path to the .env file.
    """
    # Load current .env content
    current_env = dotenv_values(env_path)

    # Apply updates to file and memory
    for key, value in updates.items():
        set_key(env_path, key, value)
        os.environ[key] = value

    # Optional: update your Config class at runtime
    from config import Config
    for key, value in updates.items():
        if hasattr(Config, key):
            setattr(Config, key, value)