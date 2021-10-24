# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [DigitalOcean](https://digitalocean.com)

🧑🏻‍💻 **Hosted By:** @FZBOTS

👥 **Support Group:** [Linux Repositories](https://t.me/DevsZone)

📢 **Updates Channel:** [Discovery Projects](https://t.me/Discovery_Updates)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Hosted By:** @FZBOTS

♻️ Tʜᴇꜱᴇ ᴄᴏᴅᴇꜱ ᴀʀᴇ ᴛᴀᴋᴇɴ ꜰʀᴏᴍ ᴛʜᴇ ɪɴᴛᴇʀɴᴇᴛ ᴀɴᴅ ꜱᴏᴍᴇ ᴏᴛʜᴇʀ ꜱᴏᴜʀᴄᴇ. Tʀᴜᴇ ᴏᴡɴᴇʀꜱ ᴅᴇꜱᴇʀᴠᴇ ᴄʀᴇᴅɪᴛꜱ.♻️

Also remember that we will Delete Adult Contents from Database. So better don't Store Those Kind of Things.

"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check **About Bot** Button.
"""
