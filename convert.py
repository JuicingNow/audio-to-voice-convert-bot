from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram import types
import keyboards as kb
import time
import os

import change

class ConvertForm(StatesGroup):
    wait_audio = State()
    wait_check_desc = State()
    wait_desc = State()

async def start_convert(message: types.Message, bot):
    await ConvertForm.wait_audio.set()
    await message.answer('Для начала, отправь MP3 файл, который хочешь преобразовать в голосовое сообщение!')

async def handle_audio(message: types.Message, state: FSMContext, bot):
    if message.audio or (message.document and message.document.mime_type == 'audio/mpeg'):
        file_id = message.audio.file_id if message.audio else message.document.file_id
        file = await bot.get_file(file_id)
        file_path = file.file_path

        download_file = await bot.download_file(file_path)
        with open("input.mp3", "wb") as f:
            f.write(download_file.read())

        async with state.proxy() as data:
            data['file_path'] = "input.mp3"

        await ConvertForm.next()
        await message.answer(
            'Выберите нужно ли описание голосового сообщения!',
            reply_markup=kb.check_desc_button
        )
async def set_desc(callback_query: types.CallbackQuery, state: FSMContext, bot):
    await bot.send_message(
        callback_query.from_user.id,
        'Отправьте описание к голосовому сообщению!'
    )

    await ConvertForm.next()

async def send_convert(message: types.Message, state: FSMContext, bot, capt):
    async with state.proxy() as data:
        file_path = data['file_path']
        caption = "" if capt == 'desc-reject' else message.text
        change.conv_to_ogg(file_path)

        time.sleep(2)
        await message.answer('✅ Ваше голосовое сообщение было успешно создано!\n'
                             'Ожидайте загрузки голосового сообщения...')

        time.sleep(3)
        with open("output.ogg", "rb") as voice:
            await bot.send_voice(message.chat.id, voice, caption=caption, reply_markup=kb.convert_button)

        os.remove(file_path)
        os.remove("output.ogg")

        await state.finish()

async def canc_convert(callback_query: types.CallbackQuery, state: FSMContext, bot):
    await state.finish()
    await bot.send_message(
        callback_query.from_user.id,
        'Преобразование аудиофайла в голосовое сообщение отменено.',
        reply_markup=kb.convert_button
    )