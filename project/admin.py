from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from create import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import admin_kb
ID = None

class FSMadmin(StatesGroup):
    photo = State()
    name = State()
    inf = State()

async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'ADMIN MODE IS ON', reply_markup=admin_kb.button_case_a)

async def cm_start(message: types.Message):
    if message.from_user.id == ID:
        await FSMadmin.photo.set()
        await message.reply('Input the formula')

async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('Canceled')

async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMadmin.next()
        await message.reply('Write the title')

async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMadmin.next()
        await message.reply('Write something about')

async def load_inf(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['inf'] = (message.text)
        await sqlite_db.sql_add_command(state)
        await state.finish()

def register_handlers_a(dp : Dispatcher):
    dp.register_message_handler(cm_start, commands=['Upload'], state=None)
    dp.register_message_handler(cancel_handler, Text(equals='/cancel', ignore_case=True), state="*")
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMadmin.photo)
    dp.register_message_handler(load_name, state=FSMadmin.name)
    dp.register_message_handler(load_inf, state=FSMadmin.inf)
    dp.register_message_handler(cancel_handler, state="*", commands='cancel')

    #dp.register_message_handler()
