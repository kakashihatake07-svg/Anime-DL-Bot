# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *
from requests_html import HTMLSession
from bs4 import BeautifulSoup

# Searching anime by regex pattern "/search <space> Anime Name"

def anime_search(client, message):
    q = message.text
    q1 = q.split()
    q1.remove(q1[0])
    str = " "
    query = str.join(q1)
    if query == "":
        # If no query string is mentioned
        message.reply_animation("https://media.tenor.com/images/cfe564edcb140705ce45aeeca8183812/tenor.gif",
                                caption=f"""**Your Query should be in This format:** 

`/search <space> Name of the Anime you want to Search.`""", parse_mode="markdown")
    else:
        url = f"https://gogoanime.ai//search.html?keyword={query}"
        session = HTMLSession()
        response = session.get(url)
        response_html = response.text
        soup = BeautifulSoup(response_html, 'html.parser')
        animes = soup.find("ul", {"class": "items"}).find_all("li")
        # print(animes)
        keyb = []
        for anime in animes:  # For every anime found
            tit = anime.a["title"]
            urll = anime.a["href"]
            r = urll.split('/')
            # aAnimes.append({"title" : anime.a["title"] , "link" : "https://www2.gogoanime.sh{}".format(anime.a["href"])})
            keyb.append([InlineKeyboardButton("{}".format(tit), callback_data="dt_{}".format(r[2]))])
        if keyb == []:
            # If returned list is empty, Send the following message.
            message.reply_text("No results found, Check your Spelling and Search Again...")
        else:
            rep = InlineKeyboardMarkup(keyb)
            message.reply_text(text=f"Your Search results for **{query}**", reply_markup=rep, parse_mode="markdown")

