from aiogram.utils import executor
from create_bot import dp
from database import work_with_bd
from create_bot import dp, bot
from aiogram import types

async def is_on(_):
    print('IS_ON!!!')
    work_with_bd.sql_start()


from handlers import client
client.register_handlers(dp)

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Я не предназначен для общения :( 🦥")

executor.start_polling(dp, skip_updates=True, on_startup=is_on)