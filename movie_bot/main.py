import asyncio
from bot_app import dp,bot

async def main():
    await dp.start_polling(bot,)

asyncio.run(main())

