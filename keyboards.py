from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

convert_button = ReplyKeyboardMarkup(resize_keyboard=True)
convert_button.add('🔊Преобразовать файл в голосовое сообщение')

check_desc_button = InlineKeyboardMarkup(row_width=2)
check_desc_button.add(
    InlineKeyboardButton('Добавить описание', callback_data='desc-accept'),
    InlineKeyboardButton('Преобразовать без описания', callback_data='desc-reject')
)

cancel_button = InlineKeyboardMarkup(row_width=1)
cancel_button.add(InlineKeyboardButton('Отменить', callback_data='cancel'))