from aiogram.utils import executor
from create import dp
from data_base import sqlite_db

async def on_startup(_):
    print('Bot is working')
    sqlite_db.sql_start()

from project import clients, admin, main

clients.reg_handlers_c(dp)
admin.register_handlers_a(dp)
main.reg_handlers_m(dp)

executor.start_polling(dp, skip_updates = True, on_startup=on_startup)
