from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

GitHubLink = 'https://github.com/SmartRightHere'
VKLink = 'https://vk.com/fuck1ngsmart'

url_kb = InlineKeyboardMarkup(row_width=2)
linkGH = InlineKeyboardButton(text='GitHub', url=GitHubLink)
linkVK = InlineKeyboardButton(text='VK', url=VKLink)

url_kb.add(linkGH, linkVK)

b1 = KeyboardButton('/start')
b2 = KeyboardButton('/help')
b3 = KeyboardButton('/info')
b4 = KeyboardButton('/menu')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b1).add(b2).add(b3).add(b4)
