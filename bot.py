from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # for reply keyboard (sends message)
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

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer('This is an application for monitoring user online, Press /start to get started.\nЭто приложение для мониторинга активности пользователей. Нажмите /start для запуска.')

@dp.message_handler(regexp='English 👍')
async def english(message: types.Message):
    answers.append(message.text)
    await message.answer('Input a user id (with @)')

@dp.message_handler(regexp='Русский 💪')
async def russian(message: types.Message):
    answers.append(message.text)
    await message.answer('Введите идентификатор пользователя (вместе с @)')

@dp.message_handler(regexp='(^@)')
async def input_id(message: types.Message):
    await message.answer('Ok') # Временно

# this is the last line
executor.start_polling(dp)