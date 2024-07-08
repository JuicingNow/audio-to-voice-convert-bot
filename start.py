from aiogram import types
import keyboards as kb

async def start_func(message: types.Message, bot):
    await bot.send_message(
        message.chat.id,
        "<b>Привет! Это бот для конвертации аудиофайла в голосовое сообщение.</b>\n"
        "Для начала работы, нажми на соответствующую кнопку.",
        parse_mode='html',
        reply_markup=kb.convert_button
    )