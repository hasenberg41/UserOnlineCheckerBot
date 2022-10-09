from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # for reply keyboard (sends message)
from time import sleep
from bot_key import KEY

bot = Bot(token=KEY)
dp = Dispatcher(bot)

answers = []  # store the answers they have given

lang1 = KeyboardButton('English 👍')  
lang2 = KeyboardButton('Русский 💪')
lang3 = KeyboardButton('Other language 🤝')
lang_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(lang1).add(lang2).add(lang3)

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.answer('Hello! Please select your language.\nПривет! Выберите язык.', reply_markup = lang_kb)


# this is the last line
executor.start_polling(dp)