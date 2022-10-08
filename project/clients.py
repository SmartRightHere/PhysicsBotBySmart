from aiogram import types, Dispatcher
from create import dp, bot
from keyboards import kb_client
from keyboards import url_kb
from data_base import sqlite_db

link = 'https://t.me/parrotsmartbot'

async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет, я тестовый бот, в процессе разработки', reply_markup=kb_client)
    except:
        await message.reply(f'Напиши боту, чтобы пообщаться! \n{link}')

async def command_help(message : types.Message):
    await bot.send_message(message.from_user.id, 'Чем могу помочь?')

async def command_info(message : types.Message):
    await bot.send_message(message.from_user.id, f'Это тестовый бот, созданный на базе Aiogram\n{link}', reply_markup=url_kb)

async def menu_command(message : types.Message):
    await sqlite_db.sql_read(message)

def reg_handlers_c(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_help, commands=['help'])
    dp.register_message_handler(command_info, commands=['info'])
    dp.register_message_handler(menu_command, commands=['menu'])
    #dp.register_message_handler() другие будут аналогично
