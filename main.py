from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from dotenv import load_dotenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
import keyboards as kb

import start
import convert

load_dotenv()
bot = Bot(token=os.getenv("TOKEN"))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    await start.start_func(message, bot)

@dp.message_handler()
async def get_message(message: types.Message):
    if message.text.lower() == '🔊преобразовать файл в голосовое сообщение':
        await convert.start_convert(message, bot)

@dp.message_handler(content_types=['audio', 'document'], state=convert.ConvertForm.wait_audio)
async def get_audio(message: types.Message, state: FSMContext):
    if message.audio or (message.document and message.document.mime_type == 'audio/mpeg'):
        await convert.handle_audio(message, state, bot)

@dp.message_handler(state=convert.ConvertForm.wait_audio)
async def check_is_audio(message: types.Message, state: FSMContext):
    if isinstance(message.text, str):
        await message.answer('Отправленный файл не является MP3-файлом. Пожалуйста, отправьте файл нужного формата.',
                             reply_markup=kb.cancel_button)

@dp.callback_query_handler(lambda text: text.data == 'cancel', state=convert.ConvertForm.wait_audio)
async def cancel_convert(callback_query: types.CallbackQuery, state: FSMContext):
    await convert.canc_convert(callback_query, state, bot)

@dp.callback_query_handler(lambda text: text.data.startswith('desc'), state=convert.ConvertForm.wait_check_desc)
async def check_desc(callback_query: types.CallbackQuery, state: FSMContext):
    if callback_query.data == 'desc-accept':
        await convert.set_desc(callback_query, state, bot)
    elif callback_query.data == 'desc-reject':
        await convert.send_convert(callback_query.message, state, bot, callback_query.data)

@dp.message_handler(state=convert.ConvertForm.wait_desc)
async def send_ready(message: types.Message, state: FSMContext):
    await convert.send_convert(message, state, bot, "none")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)