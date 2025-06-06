from aiogram import Bot, Dispatcher, types
from aiogram.types import FSInputFile
from aiogram.utils import executor
import logging

API_TOKEN = str(os.environ.get('BOT_TOKEN'))

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_voice(message: types.Message):
    voice = FSInputFile("voice.ogg")  # путь к файлу .ogg
    await message.answer_voice(voice)
    await message.answer_audio(FSInputFile("voice.mp3"))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)