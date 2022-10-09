from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # for reply keyboard (sends message)
from time import sleep

import token

bot = Bot(token=token.get_token())
dp = Dispatcher(bot)

answers = []  # store the answers they have given

### add stuff here


# this is the last line
executor.start_polling(dp)