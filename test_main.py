from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

API_TOKEN = str(os.environ.get('BOT_TOKEN')) # вставь свой токен

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_both(message: types.Message):
    # Отправка голосового сообщения (.ogg)
    with open('voice.ogg', 'rb') as voice_file:
        await message.answer_voice(voice_file)

    # Отправка аудиофайла (.mp3)
    with open('audio.mp3', 'rb') as audio_file:
        await message.answer_audio(audio_file)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)