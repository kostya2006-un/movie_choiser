from aiogram import Bot,Dispatcher,types
from aiogram.filters import CommandStart
from .local_settings import API_KEY

bot = Bot(token=API_KEY)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.reply('Начата работа!')

@dp.message()
async def start(message: types.Message):
    await message.reply(message.text)
