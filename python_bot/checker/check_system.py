import os
from importlib import reload
from loguru import logger as l
from create_bot import bot
from aiogram import types
from aiogram.types import ReplyKeyboardRemove 
from create_bot import dp, bot
from keyboards import kb_client


testers = {
    '1': [('abc', 'def')], '2': [(10, 2), (18, 4)], '3.1': [(10, 2), (10, 0)], '3.2':[(4, 2, 6), (2, 10, 7), (5, 12, 100), (387, 13, 2709)],
    '4': [(4, 2, 6), (2, 10, 7), (5, 12, 100), (387, 13, 2709)], '5': [(3,), (1,), (69,), (243,)], '6.1': [[1, 2, 3, 1523], [6, 8, 3, 14, 25], [7, -18, -150, 100]],
    '6.2': [[7, -18, -150, 100], [100], [75843, 264, 55334, 90000]], '7': [(3, 'АБВ'), (5, 'Пайтон бог, С для лохов'), (5, 'пдалтовдрж яьъхзь ыапВПР')],
    '8': [('1 2 3 4 5 1 2 3 4 5'), ('10 10 10 10 10 10 10 10'), ('3 4 5 6')], '9': [('abc - 3, def - 4'), ('abc - 3, def - 4, abc - 3, def - 4'), ('abc - 3, def - 4, hij - 10')],
    '10': [('1, 2, 3'), ('fdgh dfg')], '11': [range(10, 100)]
}

correct_answers = {
    '1': [('def', 'abc')], '2': [(20, 5, 5, 0), (72, 4.5, 4, 2)], '3.1': [5, 'Деление на 0'], '3.2': ['YES', 'NO', 'NO', 'YES'], '4': [8, -1, 93, 3083],
    '5': [1, 0, 'НЕТ', 5], '6.1': [(382.25, 6), (11.2, 17), (-15.25, -168)], '6.2': [[7, 100], [100], [75843, 90000]], '7': ['ГДЕ', 'Феочут жуи, Ц йрд руъуз', 'фйерчузйхл дбяъмб аефЗФХ'],
    '8': [5, 1], '9': [{'abc': 3, 'def': 4, 'hij': 0}, {'abc': 6, 'def': 8, 'hij': 0}, {'abc': 3, 'def': 4, 'hij': 10}], '10': ['SPACE', 'space'], '11': [161580]
}

class CheckSystem:

    def __init__(self, checker, func, num):
        self.func = func
        self.num = num
        self.checker = checker
        self.counter = 0
        self.answer = False

    def catch_tests(self):
        for i in range(len(testers[str(self.num)])):
            if self.checker(self.func, *testers[str(self.num)][i]) == correct_answers[str(self.num)][i]:
                self.counter += 1
            print(self.checker(self.func, *testers[str(self.num)][i]))

        if self.counter == len(testers[str(self.num)]):
            self.answer = True


@dp.message_handler(content_types=['document'])
async def check_the_task(message : types.Message):
    if os.path.isfile('tester.py'):
        os.remove("tester.py")
    global message_id, file_id
    message_id = message.from_user.id
    file_id = message.document.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    await bot.download_file(file_path, "tester.py")
    if not os.path.isfile('tester.py'):
        await bot.send_message(message.from_user.id, 'Вы ещё не отправили файл', reply_markup=kb_client)
    else:
        try:
            import tester
            reload(tester)
        except Exception:
            await bot.send_message(message.from_user.id, "ОШИБКА В КОДЕ, невозможно импортировать!", reply_markup=kb_client)
        else:
            
            await bot.send_message(message.from_user.id, f'отправлено задание с номером: {tester.NUMBER}.', reply_markup=kb_client)
            l.add('log.log', format="{message}", level='DEBUG')
            is_on = True
            answer = ''
            data = open('log.log', 'w')
            data.write('')
            data.close()


            @l.catch
            def main(function, *args, **kwargs):
                return function(*args, **kwargs)


            tests = CheckSystem(main, tester.function, tester.NUMBER)
            tests.catch_tests()
                
            with open("log.log", "r") as data:
                data = data.readlines()

            if data:
                is_on = False
                answer = data[-1]
                answer = answer.strip('\n')
            if not is_on:
                await bot.send_message(message.from_user.id, f'''К сожалению, у вас ошибка в коде:❌❌❌\n{answer}''', reply_markup=kb_client)
                
            else:
                if tests.answer:
                    await bot.send_message(message.from_user.id, 'Поздравляем! Все тесты пройдены✅', reply_markup=kb_client)
                else:
                    await bot.send_message(message.from_user.id, f'''Тест {tests.counter + 1} не пройден!❌''', reply_markup=kb_client)
            os.remove("tester.py")
            


