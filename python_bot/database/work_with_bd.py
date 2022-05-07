import sqlite3 as sq
from handlers import client


def sql_start():
    global base, cur
    base = sq.connect('E://aiogram_bot//python_bot//database//project.db')
    cur = base.cursor()
    base.commit()


def sql_read_material(num):
    return f"{next(cur.execute(f'Select material from lessons Where material_id = {num}'))[0]}"


def sql_read_quiz(num):
    return next(cur.execute(f'Select * from quizes Where quiz_id = {num}'))[1:]


def write_id_user():
    cur.execute('Select chat_id from users')
    row = cur.fetchall()
    data = list(map(lambda x: ''.join(list(x)), row))
    if str(client.message_id) not in data:
        cur.execute('''INSERT INTO users(chat_id, file_id) VALUES(?, ?)''', (str(client.message_id), str(client.file_id)))
    else:
        cur.execute(f'''UPDATE users SET file_id = {str(client.file_id)} WHERE {str(client.message_id)} = chat_id''')
    return next(cur.execute(f'SELECT file_id from users WHERE {str(client.message_id)} = chat_id'))
    
# if __name__ == '__main__':
#     sql_start()
#     write_id_user()