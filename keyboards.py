from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


inline_btn_1 = InlineKeyboardButton('Подписаться', callback_data='subscribe')
inline_btn_2 = InlineKeyboardButton('Отписаться', callback_data='unsubscribe')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_2)