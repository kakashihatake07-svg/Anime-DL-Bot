# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *

# Totally Optional

def instructions(client, callback_query):
    query = callback_query
    query.answer("Please Read Carefully!!!")
    keyb = [
        [InlineKeyboardButton("Search Anime Inline", switch_inline_query_current_chat="")]
    ]
    reply_markup = InlineKeyboardMarkup(keyb)
    query.edit_message_caption(caption="""**This Bot can Get your favourite Anime and It provides FREE Download Link with a fastest server(Google drive). ❤️😍**

**Points to Be Noted :-**

__👉Since gogoanime changes their domain often, The bot will go for frequent maintenance. Don't worry, the bot will still be online during maintenance.__

__👉For streaming in mobile, open the links with VLC Media Player. You can also use MX Player.__

__👉For streaming in PC, use VLC media player network stream.__

__👉For downloads, just open the links in a browser.__

**That's it, You are all caught up, just start and enjoy your favourite otaku anime😁😆**

**Type /search to Search for an Anime...**""", parse_mode="markdown", reply_markup=reply_markup)