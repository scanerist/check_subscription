import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()

@dataclass
class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")