import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6547869034:AAEjHA9N7XIg5GeECVP_XTq3RJ_8VYbZicI")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "3477714"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1264d2d7d397c4635147ee25ab5808d1")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001971965786"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5672110846"))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "postgres://shikari:CrY80HWdrLaG8qyvcuHXHkOPO0a6DmUQ@dpg-cjce4bfdb61s73e90g90-a.oregon-postgres.render.com/shikari")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

SESSION_STRING = os.environ.get("SESSION_STRING", "AQA1ENIAXwMydnJJQys8397ZK0RSneLanxnbQ3ksWT-xSL6OvNH1iwKN4A5j3gsNrFF-HuN_udsV3yfhCwP9emq9qtMJOkN5Q2ypOYyRwdSYFOSZfNadCJjnIetlZjMEdyYgalziiS-xJwBdLikJdWFOZO0h2gIc1FcDV1vJ0-EbAP9MofLGj9_L479xqq1z_AdJznOkqHyI_UuwvAb-tYFMMj51Ja-GlixjXhXg1Eh9xhyKBGY8g1whtHAUjtLAnKV50zlEllUXT7UdKNc9fwl9tVFF16wPPUWFn2PJb3Je7OFH3mVb2RSr4WeWjKZXRRNGMueuHAuXj1y_YCReu58oAg9FfAAAAAEqfXedAA")
REQUEST_CHANNEL_ID = int(os.environ.get("REQUEST_CHANNEL_ID", "-1921112616"))
REQUEST_CHANNEL_LINK = os.environ.get("REQUEST_CHANNEL_LINK", "https://t.me/+usTx4Me9_a83MGQ1")

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
