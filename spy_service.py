import collections
from telethon import TelegramClient, events, sync
from bot_key import API_ID, API_HASH, BOT_NAME, KEY
import time

bot = TelegramClient('session/' + BOT_NAME, API_ID, API_HASH).start(bot_token=KEY)

print('OK')

bot.run_until_disconnected()