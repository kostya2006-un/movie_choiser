import asyncio
from bot_app import dp,bot


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot,)

asyncio.run(main())

