import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

Owner = list(map(int, getenv("Owner", "5738579437").split()))
