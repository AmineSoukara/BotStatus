# (C) @DamienSoukara 

import os
import time
import logging
import datetime
import pytz
import urllib3
import pyrogram
import heroku3
from pyrogram import Client, filters, StopPropagation
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# get a token from @BotFather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# The Telegram API things
API_ID = int(os.environ.get("APP_ID", 12345))
API_HASH = os.environ.get("API_HASH")
# Get these values from my.telegram.org

# Your ID, Or Channel/Group ID :
ID = int(os.environ.get("ID", 12345))

HEROKU_API_KEY = "f14e4b11-d32f-4631-b150-6fb5afa2c859"
HEROKU_APP_NAME = "dzrobot"

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
            Alty.send_message(ID, TEXT)
            server = heroku3.from_key(HEROKU_API_KEY)
            app = server.app(HEROKU_APP_NAME)
            for line in app.stream_log(lines=1):
                txt = line.decode('utf-8')
                Alty.send_message(ID, txt)

#            time.sleep(TIME * 60)

main()
