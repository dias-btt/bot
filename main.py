import random
import telebot
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import time

bot = Bot(token='6184649771:AAEMI_6Q5nua1XWYiil9JQS9Ullp5CU-prk')
dp = Dispatcher(bot)

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
WORDS = response.content.splitlines()

@dp.message_handler(commands=['malik'])
async def malik(message):
    while True:
        word = random.choice(WORDS)
        await bot.send_message(message.chat.id, f"{word.decode('utf-8')} you malik")
        time.sleep(3600)

if __name__ == '__main__':
    executor.start_polling(dp)