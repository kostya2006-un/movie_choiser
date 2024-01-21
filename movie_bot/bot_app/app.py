import os
from aiogram import Bot,Dispatcher,types
from aiogram.filters import CommandStart
from dotenv import find_dotenv, load_dotenv
import aiohttp
from aiogram.types import URLInputFile


load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:8000/api/v1/random_film/') as response:
            print("Status:", response.status)
            movie = await response.json()

        if movie:
            genres = ', '.join(genre['name'] for genre in movie.get('genres'))
            countries = ', '.join(country['name'] for country in movie.get('countries'))
            name = movie['name']
            year = movie['year']
            movie_info = (f"Название: {name}\n"
                          f"Страны: {countries}\n"
                          f"Жанры: {genres}\n"
                          f"Год: {year}\n"
                          )
            image = URLInputFile(
                f"http://127.0.0.1:8000{movie['img']}",
                filename="movie.jpg"
            )
            await bot.send_photo(message.chat.id, image,caption=movie_info)

        else:
            movie_info = 'Фильм не найден'
            await message.reply(movie_info)

@dp.message()
async def start(message: types.Message):
    await message.reply(message.text)
