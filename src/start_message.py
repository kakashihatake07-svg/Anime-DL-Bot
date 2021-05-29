# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *

# Attractive Welcome message

def start_message(client, message):
    kkeeyyb = [
        [InlineKeyboardButton("Instructions", callback_data="instructions")],
    ]
    reply_markup = InlineKeyboardMarkup(kkeeyyb)
    pic_url = "https://drive.google.com/file/d/1TzmuSj05qF6Sm5Z_CSm3AGUCBx4Oe0F0/view?usp=sharing"
    message.reply_photo(pic_url, caption=f"""**Hi {message.chat.first_name}**,

Welcome to Anime DL Bot, Here you can Download all Anime for FREE 😁 ,For TG Anime Join @Anime_Collectors 
!!!

__Please read all the instructions about the bot before surfing on...__

See /whats_new to know about latest updates...""", reply_markup=reply_markup, parse_mode="markdown")
