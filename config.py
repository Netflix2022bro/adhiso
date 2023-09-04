import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6175869878:AAE9rjaVfCJX8AqTHl-YmmjpqdpGfxGKIIA")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "3477714"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1264d2d7d397c4635147ee25ab5808d1")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001971965786"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5672110846"))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "postgres://shikari:piX83BSERGtqizW9slx1OYsVGLNmAFVS@dpg-cjr00kojbais739q50lg-a.singapore-postgres.render.com/shikari_udum")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

SESSION_STRING = os.environ.get("SESSION_STRING", "BQA1ENIAq3P5SiDYgXbCpBEnyfceLDb4ENYvrP1DB20RR3q5Z8Iv-bWuGZuJTNUQUmdqU5Pk1SvYViBI0fGsLZnSGesW52oWpzlKIUrMudFX2ZfgsnTD4dAHvyW8kqS7hBW2CilMCTN2jhoe9JVaYyHwPbMCsgtvFb4T_-kofr2Ju2uZtPY4RDjHHSlGhMtPRaAlVW0Mhx1eXox9N8y-845Q9SA-PVbgMQMMhIKQy5Ux4in2YizjIKnWLaObSw0qsfYmB07rUaW8_REAp5Zv-6HSUakgBetST92s5iCz3SXJ3b7eyVG-a0VKKsJ_MPsBbg9IDrkZdmx67zBXZ0dwKthYo2BfkQAAAABpspdLAA")
REQUEST_CHANNEL_ID = int(os.environ.get("REQUEST_CHANNEL_ID", "-1001818783065"))
REQUEST_CHANNEL_LINK = os.environ.get("REQUEST_CHANNEL_LINK", "https://t.me/+CpOSmVrewr5mMDRl")

REQUEST_JOIN_MSG = "Click the  𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐭𝐨 𝐣𝐨𝐢𝐧 and then click 𝐓𝐫𝐲 𝐀𝐠𝐚𝐢𝐧 and you will get the serial & movie File...😜\n\n𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐭𝐨 𝐣𝐨𝐢𝐧 क्लिक करें और फिर 𝐓𝐫𝐲 𝐀𝐠𝐢𝐢𝐧 क्लिक करें और आपको सीरियल & मूवी फ़ाइल मिल जाएगी...😜"
#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5672110846").split()):
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
ADMINS.append(1250450587)

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
