# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import sys

# Getting currently airing Anime from the API
# Returns an "Inline Keyboard List" of Currently airing Anime

def airing_eps(client, message):
    url = f"https://gogoanime.ai/"
    session = HTMLSession()
    response = session.get(url)
    response_html = response.text
    soup = BeautifulSoup(response_html, 'html.parser')
    anime = soup.find("nav", {"class": "menu_series cron"}).find("ul")
    air = []
    for link in anime.find_all('a'):
        airing_link = link.get('href')
        name = link.get('title')
        link = airing_link.split('/')
        lnk_final = link[2]
        res = sys.getsizeof(lnk_final)
        if int(res) > 64:
            pass
        else:
            air.append([InlineKeyboardButton(f"{name}", callback_data=f"dt_{lnk_final}")])
    repl = InlineKeyboardMarkup(air)
    message.reply_text("**Currently Airing Anime: **", reply_markup=repl, parse_mode="markdown")