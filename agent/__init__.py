# load env variables before importing any other module
from dotenv import load_dotenv

load_dotenv()

from .robot import Robot
from .observer import KEN_GREEN, KEN_RED
from .llm import get_client
