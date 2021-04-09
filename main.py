# (C) @DamienSoukara 

import os
import time
import datetime
import pytz
import pyrogram

# api strings from my.telegram.org
api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")

# your session strings
user_session_string = os.environ.get("SESSION_STRING")

# your all bots username without '@' with a space 1 to another
bots = [i.strip() for i in os.environ.get("BOTS").split(' ')]

# your username without '@'
bot_owner = os.environ.get("BOT_OWNER")

# your channel username without '@'
update_channel = os.environ.get("UPDATE_CHANNEL")

# message id of your channel bot status message
status_message_id = int(os.environ.get("STATUS_MESSAGE_ID"))

# time and limits
timelimit = int(os.environ.get("TIME"))

user_client = pyrogram.Client(user_session_string, api_id=api_id, api_hash=api_hash)

def main():
    with user_client:
        while True:
            print("[INFO] Starting To Check uptime..")
            edit_text = f"<u><b>My Bots Online Status</u></b>\n"
            for bot in bots:
                print(f"[INFO] checking @{bot}")
                snt = user_client.send_message(bot, '/start')
                time.sleep(30)
                msg = user_client.get_history(bot, 1)[0]
                if snt.message_id == msg.message_id:
                    print(f"[WARNING] @{bot} is down")
                    edit_text += f"\n🤖 <b>Bot :-</b> <a href='https://telegram.me/{bot}'>{bot}</a>\n<b>⚜ Status :-</b> <code>Offline</code> ❎\n"
                    user_client.send_message(bot_owner, f"@{bot} status: <code>Down</code>")
                else:
                    print(f"[INFO] all good with @{bot}")
                    edit_text += f"\n🤖 <b>Bot :-</b> <a href='https://telegram.me/{bot}'>{bot}</a>\n<b>⚜ Status :-</b> <code>Online</code> ✅\n"
                user_client.read_history(bot)
            utc_now = datetime.datetime.now(pytz.timezone('UTC')).strftime("%I:%M %p %d/%m/%y")
            edit_text += f"""\n<b>Last checked:</b>\n{str(utc_now)} UTC ⏰\n<code>Updated on every {round(timelimit / 60)} hours</code>"""
            user_client.edit_message_text(update_channel, status_message_id, text=edit_text, disable_web_page_preview=True, parse_mode="html")
            print(f"[INFO] everything done! sleeping for {round(timelimit / 60)} hours...")
            time.sleep(timelimit * 60)


main()
