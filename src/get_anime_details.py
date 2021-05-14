# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *
import requests
from bs4 import BeautifulSoup

# Get anime Details on anime_search callback_data

def anime_details(client, callback_query):
    global list_more_anime
    query = callback_query
    dt = query.data
    dt1 = dt.split("_")
    data = dt1[1]
    query.answer("Fetching Anime Details...")
    animelink = 'https://gogoanime.ai/category/{}'.format(data)
    response = requests.get(animelink)
    plainText = response.text
    soup = BeautifulSoup(plainText, "lxml")
    source_url = soup.find("div", {"class": "anime_info_body_bg"}).img
    # url of anime image
    imgg = source_url.get('src')
    # title name of the anime
    tit_url = soup.find("div", {"class": "anime_info_body_bg"}).h1.string
    lis = soup.find_all('p', {"class": "type"})
    plot_sum = lis[1]
    pl = plot_sum.get_text().split(':')
    pl.remove(pl[0])
    sum = ""
    plot_summary = sum.join(pl)
    type_of_show = lis[0].a['title']
    ai = lis[2].find_all('a')  # .find_all('title')
    # get list of genres by using genres variable
    genres = []
    for link in ai:
        genres.append(link.get('title'))
    # get released year
    year = lis[3].get_text()
    # status completed or airing,,,
    status = lis[4].a.get_text()
    # other names
    oth_names = lis[5].get_text()
    lnk = soup.find(id="episode_page")
    source_url = lnk.find("li").a
    # ending ep no
    try:
        source_url = lnk.findAll("li")
        for link in source_url:
            list_more_anime = []
            list_more_anime.append(link.a)
        ep_num = list_more_anime[0].get("ep_end")
    except:
        source_url = lnk.find("li").a
        ep_num = source_url.get("ep_end")
    kkeeyyb = [
        [InlineKeyboardButton("Download for Free", callback_data=f"dl_{data}")],
    ]
    reply_markup = InlineKeyboardMarkup(kkeeyyb)
    query.edit_message_text(f"""[{tit_url}]({imgg})
    
**{tit_url} ({year})**

**{oth_names}**

**Type:** `{type_of_show}`

**Status: **__{status}__

**Genres: **`{genres}`

**Episodes: **__{ep_num}__

**Summary: **`{plot_summary}`""", reply_markup=reply_markup, parse_mode="markdown")