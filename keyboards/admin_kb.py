from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button_load = KeyboardButton('/Upload')
button_del = KeyboardButton('/Delete')

button_case_a = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load).add(button_del)
