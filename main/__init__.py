#Join @dev_gagan

from telethon.errors import FloodWaitError
from datetime import datetime as dt, timedelta
import asyncio
import sys
from pyrogram import Client
import asyncio
import uvloop
from pyrogram.errors import FloodWait
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from decouple import config
import logging, time
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)

uvloop.install()
MDB = "mongodb+srv://ggn:ggn@ggn.upuljx5.mongodb.net/?retryWrites=true&w=majority&appName=ggn"
API_ID ="20544260" #config("API_ID", default=None, cast=int)
API_HASH ="a0b00461d3fba22aa186fa648d77787e" #config("API_HASH", default=None)
BOT_TOKEN ="6676441705:AAEydZsISO0n5lBYHSCYg5-bsb7jkbH1kXw" #config("BOT_TOKEN", default=None)
SESSION ="AQHDmCIAB8K0u6N-6070IBUeNFWCRDnUV-OKDhJcbOraYNK0YHA3_XyHdrm4NBJMwWoU_EQGL_OEa9rnb5BQt3vBcpX607GjSzp2_H06SEY3_i2GF8gT9bcuMWBd4gGN2zBnofcLESIPiqILO10aWonJnphf2Jr4xegzxIpyGSOKZPuc6kVe5aywYs0t6SNR37vfZ0p9urYRIuDnEzU-JU-iu1l9YaQXTFrJvrtzUKJ3qo1hqUrf0rGeGjmekGx8vlaeKG3s752e29Hhc5sC3Y_BaxYIapnR0CobLMdHPq-wxkp8cfs-HxDnkYLrg97dS77fFK4-BKAvMtaMHfIgx9xmNPGZFgAAAAF81lQuAA" #config("SESSION", default=None)
FORCESUB ="aajajakaak" #config("FORCESUB", default=None)
AUTH ="6389388334" #config("AUTH", default=None)
MONGODB ="mongodb+srv://ggn:ggn@ggn.upuljx5.mongodb.net/?retryWrites=true&w=majority&appName=ggn" #config("MONGODB", default=MDB)
OWN = 6389388334 # edit this
GROUP = -1001665693055 # edit this
OWNER_ID = int(config("OWNER_ID", default=OWN))
LOG_GROUP = int(config("LOG_GROUP", default=GROUP))

SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "ggnbot",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    sys.exit(1)
