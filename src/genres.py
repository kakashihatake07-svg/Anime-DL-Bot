# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *
import requests
from bs4 import BeautifulSoup

# Lists out all Genres and related anime as callback_data

def genres(client, message):
    gen_keyb = []
    animelink = 'https://gogoanime.ai/'
    response = requests.get(animelink)
    plainText = response.text
    soup = BeautifulSoup(plainText, "lxml")
    anime = soup.find("nav", {"class": "menu_series genre right"}).find("ul")
    for link in anime.find_all('a'):
        genre_link = link.get('href')
        # print(genre_link)
        name = genre_link.split('/')
        genre_name = name[2]
        gen_keyb.append((InlineKeyboardButton(genre_name, callback_data=f"1_{genre_link}")))
        # print(gen_keyb)
    n = 2
    keybrd_genre_butt = [gen_keyb[i:i + n] for i in range(0, len(gen_keyb), n)]
    #print(keybrd_genre_butt)
    reply_markup = InlineKeyboardMarkup(keybrd_genre_butt)
    message.reply_text("Choose One Genre to See anime Related to: ", reply_markup=reply_markup, parse_mode="markdown")