import asyncio
from bot_app import dp,bot,private,user_group_router,user_chat_router
from aiogram.types import BotCommandScopeAllPrivateChats


dp.include_router(user_chat_router)
dp.include_router(user_group_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private,scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)

asyncio.run(main())

