from aiogram.types import BotCommand

private = [
    BotCommand(command='start', description='Запускает работу бота'),
    BotCommand(command='help', description='Инстукция как работает бот'),
    BotCommand(command='showfilm', description='Показывает рандомный фильм'),
    BotCommand(command='filterfilm', description='Подбирает фильмы по определнным фильтрам')
]