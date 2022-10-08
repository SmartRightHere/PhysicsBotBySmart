from aiogram import types, Dispatcher, Bot, executor
from create import dp, bot
import json, string

async def tg_send(message : types.Message):
        if message.text in ['Привет', 'привет', 'Здравствуй', 'здравствуй']:
            await message.answer('И тебе привет!')

        elif message.text in ['Hello', 'hello', 'hi', 'Hi']:
            await message.answer('Hello too!')

        else:
            await message.reply('Я не понимаю вас...')

def reg_handlers_m(dp : Dispatcher):
    dp.register_message_handler(tg_send)
