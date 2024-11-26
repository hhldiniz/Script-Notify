from enum import Enum
import os


class Environment(Enum):
    RECIPIENT = os.getenv("RECIPIENT_EMAIL")
    SENDER = os.getenv("SENDER_EMAIL")
    PASSWORD = os.getenv("SENDER_PASSWORD")
    SCRIPT_PATH = os.getenv("SCRIPT_PATH")
