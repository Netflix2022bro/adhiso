import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6451520717:AAEZOgW1-2AUl38OJEfYj7D3KnHSpP-Vg0o")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "27604683"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ed52a1d0803b2ed84c5cca7f20535aac")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001639151193"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1264280791"))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "postgres://test01_87qb_user:thnY3zXJFpXaPuwRzsY16eFKEZfgLHu8@dpg-ck5kb6mi9prc73d1ho20-a.oregon-postgres.render.com/test01_87qb")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

SESSION_STRING = os.environ.get("SESSION_STRING", "BQGlNssAvRQqHf9bWoS-r4RAktXMrU6PjZg1zLPHTGy_fhfatqgCfSS2z8w7a3P55jQGpwskRk45sGmkhX3crmBPacI850ZkjowrO6v4WVDX1CPe87NX_YnMLOYBaBsvynQhJXqiferORxBvxt_pM1s_4-hYG3cwqIuUDuZgFjBCROSNJIo-8HxElXJ2zmg4crTg92UC16L5BDViXZlrHU0D0J5g601Q-JXvvujPJ7K8K2V4xaR2bkCXgIu_YSdqHXRvdHqlJoPtvaHVWTuLd-eFweKGg37uKo7uQ8LQJvtXcEDVtNQQv2KPoUeB93iTkFeZHns-qCfZ_CUKSc6V0ReE8_zZwAAAAAGBaU6tAQ")
REQUEST_CHANNEL_ID = int(os.environ.get("REQUEST_CHANNEL_ID", "-1001702486980"))
REQUEST_CHANNEL_LINK = os.environ.get("REQUEST_CHANNEL_LINK", "https://t.me/+D2GFTThYIFsyNDRl")
REQUEST_JOIN_MSG = "Click the  𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐭𝐨 𝐣𝐨𝐢𝐧 and then click 𝐓𝐫𝐲 𝐀𝐠𝐚𝐢𝐧 and you will get the serial & movie File...😜\n\n𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐭𝐨 𝐣𝐨𝐢𝐧 क्लिक करें और फिर 𝐓𝐫𝐲 𝐀𝐠𝐢𝐢𝐧 क्लिक करें और आपको सीरियल & मूवी फ़ाइल मिल जाएगी...😜"
#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1264280791").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "This bot has been online for you since<b> {uptime} </b>."
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1264280791)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
