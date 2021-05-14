# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *

# Dev Info is Completely Optional

def dev_info(client, message):
    keyb = [
        [InlineKeyboardButton("Rate me on BotsArchive", url="https://t.me/BotsArchive/1858")]
    ]
    reply_markup = InlineKeyboardMarkup(keyb)
    message.reply_text("""Made with ❤️ in 🇮🇳 by <YOUR_TELEGRAM_USERNAME>.

Language: [Python3](https://www.python.org/)

Bot Framework: [Pyrogram Asyncio](https://github.com/pyrogram/pyrogram)

Server: <YOUR_SERVER_NAME>

Please share the bot if you like it 👍👍""", reply_markup=reply_markup, parse_mode="markdown")