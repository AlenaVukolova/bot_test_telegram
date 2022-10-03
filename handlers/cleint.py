from cgitb import text
from gc import callbacks
import logging
from aiogram import Bot, Dispatcher, executor, types
import os
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


logging.basicConfig(
    level = logging.DEBUG,
    format = "%(asctime)s : %(levelname)s", filename = "error.log"
    
)





async def on_startup(_):
    print("Bot went online")


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token="5579467700:AAGa1Ej4OAIxOwS0uocZ_N_Up09grAyf_AE")
#bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot)





@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    mess = f"Привет, <b>{message.from_user.first_name}</b> "
    await message.answer(mess, parse_mode="html")
    await message.answer("Я - бот для пополнения баланса.\nНажмите на кнопку, чтобы пополнить баланс",parse_mode="html")
    #инлайн кнопка
    inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text ="нажми меня"\
        ,callback_data="www"))
    await message.answer("инлайн кнопка", reply_markup=inkb)





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)










































     