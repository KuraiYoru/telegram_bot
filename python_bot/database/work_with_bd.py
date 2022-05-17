import sqlite3 as sq
from handlers import client


def sql_start():
    global base, cur
    base = sq.connect('.//database//project.db')
    cur = base.cursor()
    base.commit()


def sql_read_material(num):
    return f"{next(cur.execute(f'Select material from lessons Where material_id = {num}'))[0]}"


def sql_read_quiz(num):
    return next(cur.execute(f'Select * from quizes Where quiz_id = {num}'))[1:]


class WorkWithUser:

    def __init__(self):
        self.cursor = cur

    def add_user(self, user_id):
        with base:
            self.cursor.execute("INSERT INTO users(user_id) VALUES(?)", (user_id,)).fetchall()

    def user_exists(self, user_id):
        with base:
            if (str(user_id),) not in self.cursor.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,)).fetchall():
                self.add_user(user_id)
    
    def set_file(self, file_id, user_id):
        with base:
            self.cursor.execute("UPDATE users SET file_id = ? WHERE user_id = ?", (file_id, user_id,))
    
    def get_file(self, user_id):
        with base:
            return next(self.cursor.execute("SELECT file_id from users WHERE user_id = ?", (user_id,)))