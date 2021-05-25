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

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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

START_TEXT = "Hello {} I'm Alive\n-App Name : {}"
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("Dev", url="https://t.me/AmineSoukara"),
        InlineKeyboardButton("Source Code", url="https://github.com/AmineSoukara")
        ]]
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
                txt = line.decode('utf-8')
                Alty.send_message(OWNER_ID, txt)

#            time.sleep(TIME * 60)

@Alty.on_message(filters.private & filters.command(["start"]))
async def start(c, m):
    await m.reply_text(
        text=START_TEXT.format(m.from_user.mention, HEROKU_APP_NAME),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS
    )



main()
