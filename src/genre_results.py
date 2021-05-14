# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *
import requests
from bs4 import BeautifulSoup
from pyrogram.errors.exceptions.bad_request_400 import ButtonDataInvalid
import sys

# Get Inline Keyboard List of Anime with the returned Genre Callback_Data

def genre_results(client, callback_query):
    query = callback_query
    data = query.data
    data_pre = data.split("_")
    gen = data_pre[1].split("/")
    gen_name = gen[2]
    try:
        url = f"https://gogoanime.ai{data_pre[1]}?page={data_pre[0]}"
        response = requests.get(url)
        plainText = response.text
        soup = BeautifulSoup(plainText, "lxml")
        animes = soup.find("ul", {"class": "items"}).find_all("li")
        keybrd_genre_butt = []
        for anime in animes:  # For every anime found
            tit = anime.a["title"]
            urll = anime.a["href"]
            r = urll.split('/')
            res = sys.getsizeof(r[2])
            if int(res) > 64:
                pass
            else:
                keybrd_genre_butt.append([(InlineKeyboardButton(tit, callback_data=f"dt_{r[2]}"))])
        # n = 3
        # keybrd_genre_butt = [keybrd_genre_butts[i:i + n] for i in range(0, len(keybrd_genre_butts), n)]
        callback_query.answer("Fetching Genres...")
        keybrd_genre_butt.append([InlineKeyboardButton("Back", callback_data=f"{int(data_pre[0]) - 1}_{data_pre[1]}"),
                                  (InlineKeyboardButton(f"Page {data_pre[0]}", callback_data="none")),
                                  (InlineKeyboardButton("Next", callback_data=f"{int(data_pre[0]) + 1}_{data_pre[1]}"))])
        reply_markup = InlineKeyboardMarkup(keybrd_genre_butt)
        query.edit_message_text(f"Anime under genre **{gen_name}**: ", reply_markup=reply_markup, parse_mode="markdown")
    except AttributeError:
        callback_query.answer("End of search Results...", show_alert=True)
