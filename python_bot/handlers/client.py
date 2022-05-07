from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client, lesson_btn, task, checker_button
from aiogram.types import ReplyKeyboardRemove
from database import work_with_bd
from aiogram.dispatcher.filters import Text
from checker import check_system
import os
import sqlite3 as sq


res = 1

async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, 'Привет! Я бот помощник в изучении Python.', reply_markup=kb_client)


async def introduction(message : types.Message):
    await bot.send_message(message.from_user.id, '''
Перед тем как начать кодить, нужно установить сам Python, сделать это можно по ссылке: https://www.python.org/downloads/
Далее рекомендую выбрать среду разработки PyCharm или Visual Studio code
После их иустановки, нужно создать файл с любым именем , но так, чтобы на конце было .py
    ''', reply_markup=kb_client)


async def advice(message : types.Message):
    await bot.send_message(message.from_user.id,
     '''Для чего изучать программирование?
Возможно вам попадались различные вакансии программистов, где говорится об очень высокой оплате и востребованности этой професии.
Это и вправду так, но если тебя привлекает эта деятельность лишь в коммерческих целях, то лучше забросить сразу. Программирование - это трудно,
зачастую человек не может развиваться, когда всю его мотивацию составляет финансовая зависимость. Программирование - это творчество, которое должно идти от души.
Тогда, и только тогда стоит делать программирование своим основным заработком.''', reply_markup=ReplyKeyboardRemove())


async def cancel(message : types.Message):
    await bot.send_message(message.from_user.id, 'Клавиатура закрыта', reply_markup=ReplyKeyboardRemove())

async def lessons(message : types.Message):
    await bot.send_message(message.from_user.id, '''Список уроков:
Lesson 1 - Функции print() и input()
Lesson 2 - математические операторы
Lesson 3 - Условный оператор 
Lesson 4 - Знакомство с циклом for
Lesson 5 - Знакомство с циклом while
Lesson 6 - Списки
Lesson 7 - Строки. Срезы
Lesson 8 - Множества
Lesson 9 - Словари
Lesson 10 - Функции
Lesson 11 - Лямбда-функция''', reply_markup=lesson_btn)
    

@dp.callback_query_handler(Text(startswith='btn_'))
async def process_callback_kb1btn1(callback : types.CallbackQuery):
    global res
    res = int(callback.data.split('_')[1])
    await callback.message.answer(work_with_bd.sql_read_material(res)[:1000])
    await callback.message.answer(work_with_bd.sql_read_material(res)[1000:], reply_markup=task)



@dp.poll_answer_handler()
async def handle_poll_answer(quiz_answer : types.PollAnswer):
    data = work_with_bd.sql_read_quiz(res)
    id = dict(quiz_answer)['from']['id']
    my_quiz = await bot.send_poll(id, data[0],
    list(data[1:-1]), type='quiz', correct_option_id=int(data[-1]), is_anonymous=False)


@dp.message_handler(content_types=['document'])
async def handle_file(message : types.Message):
    if os.path.isfile('tester.py'):
        os.remove("tester.py")
    global message_id, file_id
    message_id = message.from_user.id
    file_id = message.document.file_id
    id_file = work_with_bd.write_id_user()[0]
    print(id_file)
    file = await bot.get_file(id_file)
    file_path = file.file_path
    await bot.download_file(file_path, "tester.py")
    await bot.send_message(message.from_user.id, 'Файл скачан!', reply_markup=checker_button)


async def send_file(message: types.Document):
    if res == 3:
        await message.reply_document(open(f'lessons/task3_1.py', 'rb'))
        await message.reply_document(open(f'lessons/task3_2.py', 'rb'))
    elif res == 6:
        await message.reply_document(open(f'lessons/task6_1.py', 'rb'))
        await message.reply_document(open(f'lessons/task6_2.py', 'rb'))
    else:
        await message.reply_document(open(f'lessons/task{res}.py', 'rb'))


def register_handlers(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(introduction, commands=['introduction'])
    dp.register_message_handler(advice, commands=['advice'])
    dp.register_message_handler(lessons, commands=['lessons'])
    dp.register_message_handler(handle_poll_answer, commands=['quiz'])
    dp.register_message_handler(cancel, commands=['cancel'])
    dp.register_message_handler(send_file, commands=['send_the_task'])
    dp.register_message_handler(check_system.check_the_task, commands=['check_the_task'])



    
 