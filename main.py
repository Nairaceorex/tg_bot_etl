import asyncio
import logging
from datetime import datetime

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import aiohttp

TOKEN = ''

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher()
dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

# Хэндлер на команду /test1
@dp.message(Command("test1"))
async def cmd_test1(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://395b-95-221-215-34.ngrok-free.app/') as response:
            data = await response.text()
            await message.answer(data)

async def main():
    # Запускаем поллинг для получения обновлений от Telegram
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
