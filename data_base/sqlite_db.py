import sqlite3 as sq
from create import dp, bot

def sql_start():
    global base, cur
    base = sq.connect('physics.dp')
    cur = base.cursor()
    if base:
        print('Data base connected')
    base.execute('CREATE TABLE IF NOT EXISTS menu(photo TEXT, name TEXT PRIMARY KEY, inf TEXT)')
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nTitle: {ret[2]}\nAbout: {ret[-1]}')
