import os
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.context import FSMContext
from dotenv import find_dotenv, load_dotenv
import aiohttp
from aiogram.types import URLInputFile
from aiogram.fsm.state import StatesGroup,State
from .chat_types import ChatTypeFilter
from .messages import GREETING_MESSAGE,HELP_COMMAND

user_chat_router = Router()
user_chat_router.message.filter(ChatTypeFilter(['private']))
load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

class Filmfilter(StatesGroup):
    genres = State()
    year_min = State()
    year_max = State()
    countries = State()

@user_chat_router.message(CommandStart())
async def start(message: types.Message):
    await message.answer(GREETING_MESSAGE)


@user_chat_router.message(Command("help"))
async def help(message: types.Message):
    await message.answer(HELP_COMMAND)


@user_chat_router.message(F.text.contains('показать фильм'))
@user_chat_router.message(Command("showfilm"))
async def showfilm(message: types.Message):
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

url_middle = 'http://127.0.0.1:8000/api/v1/movie/?genres=&year_min=&year_max=&countries='
@user_chat_router.message(F.text.contains('Подборка фильмов'))
@user_chat_router.message(StateFilter(None),Command("filterfilm"))
async def filterfilm(message: types.Message,state: FSMContext):
    await bot.send_message(message.chat.id,'Введите жанры через пробел')
    await state.set_state(Filmfilter.genres)

@user_chat_router.message(Filmfilter.genres,F.text)
async def add_min_year(message: types.Message,state: FSMContext):
    await state.update_data(genres=message.text)
    await message.answer("Введите год от которого начать поиск")
    await state.set_state(Filmfilter.year_min)

@user_chat_router.message(Filmfilter.year_min,F.text)
async def add_min_year(message: types.Message,state: FSMContext):
    await state.update_data(year_min=message.text)
    await message.answer("Введите год до которого искать")
    await state.set_state(Filmfilter.year_max)

@user_chat_router.message(Filmfilter.year_max,F.text)
async def add_min_year(message: types.Message,state: FSMContext):
    await state.update_data(year_max=message.text)
    await message.answer("Введите страны")
    await state.set_state(Filmfilter.countries)

@user_chat_router.message(Filmfilter.countries,F.text)
async def add_min_year(message: types.Message,state: FSMContext):
    await state.update_data(countries=message.text)
    await message.answer("Фильтры заданы")
    dte = await state.get_data()
    await message.answer(str(dte))
    await state.clear()