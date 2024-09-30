import asyncio
from asyncio import exceptions
from email.quoprimime import unquote
from mailbox import Message
import os
from warnings import filters
import aiogram
from aiogram.types import Update
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
from aiogram.utils.exceptions import TelegramAPIError
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor, markdown
from aiogram import Bot, Dispatcher, types



# Переменные
API_TOKEN = '7564599954:AAHnfJ0f-nabcxOo62C1VTH0gCL3SkHNuDA'
CHANNEL_ID = -1002031648635  # ID канала, в котором будем следить за сообщениями
admin_id = 983681689, 1228200514


# Настройка бота
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# Глобальная переменная для состояния обработчика сообщений
enabled = True

@dp.message_handler(commands=['1'])
async def send_welcome(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\nЯ - бот, а ты пидор.")

####################################################################################################################

# Админские команды /start_admin и /help_admin.
@dp.message_handler(Command(commands=['start_admin', 'help_admin']), user_id=admin_id)
async def start_admin(message: types.Message):
    global enabled
    if message.text == '/start_admin':
        enabled = True
        await message.answer('✅Обработка сообщений включена.\nОбработка сообщений работает только на слова:\n\nГОЛЛЕР, Голлер, голлер, РАСУЛУ, Расул, РАСУЛ, расул, расулу, Расулу')
    elif message.text == '/help_admin':
        await message.answer(
            '👑Адмиские команды:\n\n'
            '📑Обработка сообщение:\n'
            '✅Включить обработку сообщений - "/start_admin"\n'
            '❌Выключить обработку сообщений -"/stop_admin"\n\n'
            '🤡ПОТОМ ЕЩЕ ДОБАВЛЮ)))'
            )
        
# Админская команда /stop_admin.
@dp.message_handler(Command(commands=['stop_admin']), user_id=admin_id)
async def stop_admin(message: types.Message):
    global enabled
    if message.text == '/stop_admin':
        enabled = False
        await message.answer('❌Обработка сообщений выключена.')

# Обработка сообщение с поиском слов 'ГОЛЛЕР','Голлер','голлер','РАСУЛУ','Расул','РАСУЛ','расул','расулу','Расулу'.
@dp.channel_post_handler(chat_id=CHANNEL_ID)
async def check_message(message: types.Message):
    if enabled:
        if 'ГОЛЛЕР' in message.text:
            await bot.send_photo(chat_id=CHANNEL_ID, photo=open('goller.jpg', 'rb'))
        if 'Голлер' in message.text:
            await bot.send_photo(chat_id=CHANNEL_ID, photo=open('goller.jpg', 'rb'))
        if 'голлер' in message.text:
            await bot.send_photo(chat_id=CHANNEL_ID, photo=open('goller.jpg', 'rb'))
        if 'РАСУЛУ' in message.text:
            await bot.send_audio(chat_id=CHANNEL_ID, audio=open('rasul.mp3', 'rb'))
        if 'Расул' in message.text:
            await bot.send_audio(chat_id=CHANNEL_ID, audio=open('rasul.mp3', 'rb'))
        if 'РАСУЛ' in message.text:
            await bot.send_audio(chat_id=CHANNEL_ID, audio=open('rasul.mp3', 'rb'))
        if 'расул' in message.text:
            await bot.send_audio(chat_id=CHANNEL_ID, audio=open('rasul.mp3', 'rb'))
        if 'расулу' in message.text:
            await bot.send_audio(chat_id=CHANNEL_ID, audio=open('rasul.mp3', 'rb'))
        if 'Расулу' in message.text:
            await bot.send_audio(chat_id=CHANNEL_ID, audio=open('rasul.mp3', 'rb'))
            
####################################################################################################################


# Функция для запуска и остановки бота.
async def main():
    try:
        await dp.start_polling()
    finally:
        await dp.stop_polling()
if __name__ == '__main__':
    asyncio.run(main())
