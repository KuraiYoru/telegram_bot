from aiogram.utils import executor
from create_bot import dp
from database import work_with_bd

async def is_on(_):
    print('IS_ON!!!')
    work_with_bd.sql_start()


from handlers import client
client.register_handlers(dp)

executor.start_polling(dp, skip_updates=True, on_startup=is_on)