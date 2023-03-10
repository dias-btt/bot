import random
import telebot
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import time
from bs4 import BeautifulSoup

bot = Bot(token='5815959183:AAHCo4ZbBWoWFE9hPKkO-zYCjeaRyZFCyMM')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(message.chat.id, f"Hello {message.from_user.mention}! Press /check to check tickets for Gauhartas (16 March)")
@dp.message_handler(commands=['check'])
async def checkTicketon(message):
    ticketonG16 = "https://m.ticketon.kz/show/4482233"
    rG16 = requests.get(ticketonG16)

    soup = BeautifulSoup(rG16.text, "lxml")
    articles_card = soup.find_all("div", class_="b-hall_error")

    for article in articles_card:
        article_desc = article.find('p').text.strip()
    await bot.send_message(message.chat.id, f"{article_desc}"
                                            f"\nhttps://m.ticketon.kz/show/4482233")


if __name__ == '__main__':
    executor.start_polling(dp)