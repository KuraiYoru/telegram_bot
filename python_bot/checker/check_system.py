import os
from importlib import reload
from loguru import logger as l
from create_bot import bot
from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from handlers import client


async def check_the_task(message : types.Message):
    if not os.path.isfile('tester.py'):
        await bot.send_message(message.from_user.id, 'Вы ещё не отправили файл', reply_markup=ReplyKeyboardRemove())
    else:
        import tester
        if str(client.res) != tester.NUMBER:
            await bot.send_message(message.from_user.id, f'Отправлено другое задание\nНа данный момент проверяется задание {client.res}.'
'\nЧтобы проверять другое задание выберете урок с подходящим номером, а затем оптравьте задание!', reply_markup=ReplyKeyboardRemove())
        else:


            await bot.send_message(message.from_user.id, 'Задание проверяется!', reply_markup=ReplyKeyboardRemove())
            
            reload(tester)
            l.add('log.log', format="{message}", level='DEBUG')
            is_on = True
            answer = ''
            data = open('log.log', 'w')
            data.write('')
            data.close()


            @l.catch
            def main(function, *args, **kwargs):
                function(*args, **kwargs)


            if tester.NUMBER == '1':
                main(tester.function, 'abc', 'def')
            elif tester.NUMBER == '2':
                main(tester.function, 10, 2)
                main(tester.function, 18, 4)
            elif tester.NUMBER == '3.1':
                main(tester.function, 10, 2)
                main(tester.function, 10, 0)
            elif tester.NUMBER == '3.2':
                main(tester.function, 4, 2, 6)
                main(tester.function, 2, 10, 7)
                main(tester.function, 5, 12, 100)
                main(tester.function, 387, 13, 2709)
            elif tester.NUMBER == '4':
                main(tester.function, (1, 2, 3, 4))
                main(tester.function, (3, 3))
            elif tester.NUMBER == '5':
                main(tester.function, 3)
                main(tester.function, 1)
                main(tester.function, 69)
                main(tester.function, 243)
            elif tester.NUMBER == '6.1':
                main(tester.function, [1, 2, 3, 1523])
                main(tester.function, [6, 8, 3, 14, 25])
                main(tester.function, [7, -18, -150, 100])
            elif tester.NUMBER == '6.2':
                main(tester.function, [7, -18, -150, 100])
                main(tester.function, [100])
                main(tester.function, [75843, 264, 55334, 90000])
            elif tester.NUMBER == '7':
                main(tester.function, 3, 'АБВ')
                main(tester.function, 5, 'Пайтон бог, С для лохов')
                main(tester.function, 5, 'пдалтовдрж яьъхзь ыапВПР')
            elif tester.NUMBER == '8':
                main(tester.function, '1 2 3 4 5 1 2 3 4 5')
                main(tester.function, '10 10 10 10 10 10 10 10')
                main(tester.function, '3 4 5 6')
            elif tester.NUMBER == '9':
                main(tester.function, 'abc - 3, def - 4')
                main(tester.function, 'abc - 3, def - 4, abc - 3, def - 4')
                main(tester.function, 'abc - 3, def - 4, hij - 10')
            elif tester.NUMBER == '10':
                main(tester.function, '1, 2, 3')
                main(tester.function, 'fdgh dfg')
            elif tester.NUMBER == '11':
                main(tester.function, range(10, 100))
            else:
                await bot.send_message(message.from_user.id, f"Задания с таким номером не существует")

                
            with open("log.log", "r") as data:
                data = data.readlines()

            if data:
                is_on = False
                answer = data[-1]
                answer = answer.strip('\n')
            if not is_on:
                await bot.send_message(message.from_user.id, '''К сожалению, у вас ошибка в коде:''')
                await bot.send_message(message.from_user.id, f"{answer}")
                

            if is_on:
                if tester.NUMBER == '1':
                    if tester.function('abc', 'def') == ('def', 'abc'):
                        await bot.send_message(message.from_user.id, f"Все задания выполнены правильно!\nПоздравляем!")
                    else:
                        await bot.send_message(message.from_user.id, '''Тест 1 не пройден''')
                elif tester.NUMBER == '2':
                    if tester.function(10, 2) == (20, 5, 5, 0):
                        if tester.function(18, 4) == (72, 4.5, 4, 2):
                            await bot.send_message(message.from_user.id, f"Все задания выполнены правильно!\nПоздравляем!")
                        else:
                            await bot.send_message(message.from_user.id, '''Тест 2 не пройден''')
                    else:
                        await bot.send_message(message.from_user.id, '''Тест 1 не пройден''')
                elif tester.NUMBER == '3.1':
                    if tester.function(10, 2) == 5:
                        if tester.function(10, 0) == 'Деление на 0':
                            await bot.send_message(message.from_user.id, f"Все задания выполнены правильно!\nПоздравляем!")
                        else:
                            await bot.send_message(message.from_user.id, f"Тест 2 не пройден")
                    else:
                        await bot.send_message(message.from_user.id, f"Тест 1 не пройден")
                elif tester.NUMBER == '3.2':
                    if tester.function(4, 2, 6) == 'YES':
                        if tester.function(2, 10, 7) == 'NO':
                            if tester.function(5, 12, 100) == 'NO':
                                if tester.function(387, 13, 2709) == 'YES':
                                    await bot.send_message(message.from_user.id, f"Все задания выполнены правильно!\nПоздравляем!")
                                else:
                                    await bot.send_message(message.from_user.id, f"Тест 4 не пройден")
                            else:
                                await bot.send_message(message.from_user.id, f"Тест 3 не пройден")
                        else:
                            await bot.send_message(message.from_user.id, f"Тест 2 не пройден")
                    else:
                        await bot.send_message(message.from_user.id, f"Тест 1 не пройден")
                elif tester.NUMBER == '4':
                    if tester.function((1, 2, 3, 4)) == -2:
                        if tester.function((3, 3)) == 0:
                            await bot.send_message(message.from_user.id, f"Все задания выполнены правильно!\nПоздравляем!")
                        else:
                            await bot.send_message(message.from_user.id, f"Тест 2 не пройден")
                    else:
                        await bot.send_message(message.from_user.id, f"Тест 1 не пройден")
                elif tester.NUMBER == '5':
                    if tester.function(3) == 1:
                        if tester.function(1) == 0:
                            if tester.function(69) == 'НЕТ':
                                if tester.function(243) == 5:
                                    await bot.send_message(message.from_user.id, f"Все задания выполнены правильно!\nПоздравляем!")
                                else:
                                    await bot.send_message(message.from_user.id, f"Тест 4 не пройден")
                            else:
                                await bot.send_message(message.from_user.id, f"Тест 3 не пройден")
                        else:
                            await bot.send_message(message.from_user.id, f"Тест 2 не пройден")
                    else:
                        await bot.send_message(message.from_user.id, f"Тест 1 не пройден")
                elif tester.NUMBER == '6.1':
                    if tester.function([1, 2, 3, 1523]) == (382.25, 6):
                        if tester.function([6, 8, 3, 14, 25]) == (11.2, 17):
                            if tester.function([7, -18, -150, 100]) == (-15.25, -168):
                                await bot.send_message(message.from_user.id, f"Все задания выполнены правильно!\nПоздравляем!")
                            else:
                                await bot.send_message(message.from_user.id, f"Тест 3 не пройден")
                        else:
                            await bot.send_message(message.from_user.id, f"Тест 2 не пройден")
                    else:
                        await bot.send_message(message.from_user.id, f"Тест 1 не пройден")
                elif tester.NUMBER == '6.2':
                    if tester.function([7, -18, -150, 100]) == [7, 100]:
                        if tester.function([100]) == [100]:
                            if tester.function([75843, 264, 55334, 90000]) == [75843, 90000]:
                                await bot.send_message(message.from_user.id, f"Все задания выполнены правильно!\nПоздравляем!")
                            else:
                                await bot.send_message(message.from_user.id, f"Тест 3 не пройден")
                        else:
                            await bot.send_message(message.from_user.id, f"Тест 2 не пройден")
                    else:
                        await bot.send_message(message.from_user.id, f"Тест 1 не пройден")
                elif tester.NUMBER == '7':
                    if tester.function(3, 'АБВ') == 'ГДЕ':
                        if tester.function(5, 'Пайтон бог, С для лохов') == 'Феочут жуи, Ц йрд руъуз':
                            if tester.function(5, 'пдалтовдрж яьъхзь ыапВПР') == 'фйерчузйхл дбяъмб аефЗФХ':
                                await bot.send_message(message.from_user.id, f"Все задания выполнены правильно!\nПоздравляем!")
                            else:
                                await bot.send_message(message.from_user.id, f"Тест 3 не пройден")
                        else:
                            await bot.send_message(message.from_user.id, f"Тест 2 не пройден")
                    else:
                        await bot.send_message(message.from_user.id, f"Тест 1 не пройден")
                elif tester.NUMBER == '8':
                    if tester.function('1 2 3 4 5 1 2 3 4 5') == 5:
                        if tester.function('10 10 10 10 10 10 10 10') == 1:
                            if tester.function('3 4 5 6') == 4:
                                await bot.send_message(message.from_user.id, f"Все задания выполнены правильно!\nПоздравляем!")
                            else:
                                await bot.send_message(message.from_user.id, f"Тест 3 не пройден")
                        else:
                            await bot.send_message(message.from_user.id, f"Тест 2 не пройден")
                    else:
                        await bot.send_message(message.from_user.id, f"Тест 1 не пройден")
                elif tester.NUMBER == '9':
                    if tester.function('abc - 3, def - 4') == {'abc': 3, 'def': 4, 'hij': 0}:
                        if tester.function('abc - 3, def - 4, abc - 3, def - 4') == {'abc': 6, 'def': 8, 'hij': 0}:
                            if tester.function('abc - 3, def - 4, hij - 10') == {'abc': 3, 'def': 4, 'hij': 10}:
                                await bot.send_message(message.from_user.id, f"Все задания выполнены правильно!\nПоздравляем!")
                            else:
                                await bot.send_message(message.from_user.id, f"Тест 3 не пройден")
                        else:
                            await bot.send_message(message.from_user.id, f"Тест 2 не пройден")
                    else:
                        await bot.send_message(message.from_user.id, f"Тест 3 не пройден")
                elif tester.NUMBER == '10':
                    if tester.function('1, 2, 3') == 'SPACE':
                        if tester.function('fdgh dfg') == 'space':
                            await bot.send_message(message.from_user.id, f"Все задания выполнены правильно!\nПоздравляем!")
                        else:
                            await bot.send_message(message.from_user.id, f"Тест 2 не пройден")
                    else:
                        await bot.send_message(message.from_user.id, f"Тест 1 не пройден")
                elif tester.NUMBER == '11':
                    if tester.function(range(10, 100)) == 161580:
                        await bot.send_message(message.from_user.id, f"Все задания выполнены правильно!\nПоздравляем!")
                    else:
                        await bot.send_message(message.from_user.id, f"Тест 1 не пройден")       
            os.remove("tester.py")