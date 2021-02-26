import os
import time
import datetime
import pyrogram

try:
    import secrets
except:
    import fake_secrets as secrets

SESSION_STRING = os.environ.get(
    "SESSION_STRING",
    secrets.SESSION_STRING
)
API_ID = int(
    os.environ.get(
        "API_ID",
        secrets.API_ID
    )
)
API_HASH = os.environ.get(
    "API_HASH",
    secrets.API_HASH
)
BOT_OWNER = os.environ.get(
    "BOT_OWNER",
    secrets.BOT_OWNER
)
BOTS = [
    i.strip().rstrip().replace("@", "") for i in os.environ.get(
        "BOTS",
        secrets.BOTS
    ).split()
]
UPDATE_CHANNEL = os.environ.get(
    "UPDATE_CHANNEL",
    secrets.UPDATE_CHANNEL
)
SATUS_MESSAGE_MESSAGE_ID = int(
    os.environ.get(
        "SATUS_MESSAGE_MESSAGE_ID", secrets.SATUS_MESSAGE_MESSAGE_ID
    )
)

client = pyrogram.Client(
    SESSION_STRING,
    api_id=API_ID,
    api_hash=API_HASH
)


def main():
    with client:
        while True:
            edit_text = "<b>👾 Our Bots' Status (Updating Every 45 Minutes)</b>\n\n"

            for bot in BOTS:
                snt = client.send_message(bot, "/start")
                time.sleep(5)
                msg = client.get_history(bot, 1)[0]

                if snt.message_id == msg.message_id:
                    edit_text += f"❌ - @{bot} : DOWN\n\n"
                    client.send_message(
                        BOT_OWNER,
                        f"❌ - @{bot} IS DOWN !"
                    )
                else:
                    edit_text += f"✅ - @{bot} : UP\n\n"

                client.read_history(bot)

            utc_now = datetime.datetime.utcnow()

            edit_text += f"⏱ <i>LAST UPDATE : {str(utc_now)} UTC</i>"

            client.edit_message_text(
                UPDATE_CHANNEL,
                SATUS_MESSAGE_MESSAGE_ID,
                edit_text
            )
            time.sleep(45 * 60)


main()
