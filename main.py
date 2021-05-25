# (C) @DamienSoukara

import os

import heroku3
import urllib3
from pyrogram import Client

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# get a token from @BotFather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# The Telegram API things
API_ID = int(os.environ.get("APP_ID", 12345))
API_HASH = os.environ.get("API_HASH")
# Get these values from my.telegram.org

# Your ID, Or Channel/Group ID :
ID = int(os.environ.get("ID", 12345))

HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
ALL_APPS = bool(os.environ.get("ALL_APPS", False))


Alty = Client("Alty-Logs", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)


def main():
    with Alty:
        while True:
            print("💬 [INFO] Starting To Stream Logs..")
            TEXT = "💬 [INFO] Starting To Stream Logs.."
            Alty.send_message(OWNER_ID, TEXT)

            server = heroku3.from_key(HEROKU_API_KEY)
            app = server.app(HEROKU_APP_NAME)
            apps = server.apps(order_by="name", sort="asc")

            if ALL_APPS is True:
                for ap in apps:
                    allapp = server.app(ap.name)
                    for line in allapp.stream_log(lines=1):
                        try:
                            txt = line.decode("utf-8")
                            done = f"➕ #{ap.name}\n" + txt
                            Alty.send_message(ID, done)
                        except Exception as e:
                            print(e)

            elif ALL_APPS is False:
                for line in app.stream_log(lines=1):
                    txt = line.decode("utf-8")
                    done = "➕ " + txt
                    Alty.send_message(ID, done)


main()
