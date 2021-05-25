# (C) @DamienSoukara 

import os
import time
import datetime
import pytz
import pyrogram
import heroku3
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Api Strings From my.telegram.org
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Your Username Without '@'
BOT_OWNER = os.environ.get("BOT_OWNER")
OWNER_ID = int(853393439)

HEROKU_API_KEY = "f14e4b11-d32f-4631-b150-6fb5afa2c859"
HEROKU_APP_NAME = "dzrobot"

# Time & Limits
TIME = int(os.environ.get("TIME"))

Alty = Client(
        "Alty-Logs",
        bot_token=BOT_TOKEN,
        api_id=API_ID,
        api_hash=API_HASH
    )

def main():
    with Alty:
        while True:
            print("💬 [INFO] Starting To Stream Logs..")
            TEXT = "💬 [INFO] Starting To Stream Logs.."
            Alty.send_message(OWNER_ID, TEXT)
            server = heroku3.from_key(HEROKU_API_KEY)
            app = server.app(HEROKU_APP_NAME)
            for line in app.stream_log(lines=1):
                Alty.send_message(OWNER_ID, line)

#            time.sleep(TIME * 60)


main()
