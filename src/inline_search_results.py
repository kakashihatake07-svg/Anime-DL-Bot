# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup

# Shows anime details on returned inline search id

def anime_inline_details(client,message):
    try:
        animelink = 'https://gogoanime.ai/category/{}'.format(message.text)
        response = requests.get(animelink)
        plainText = response.text
        soup = BeautifulSoup(plainText, "lxml")
        source_url = soup.find("div", {"class": "anime_info_body_bg"}).img
        # url of anime image
        imgg = source_url.get('src')
        # print(imgg)
        # title name of the anime
        tit_url = soup.find("div", {"class": "anime_info_body_bg"}).h1.string
        # print(tit_url)
        lis = soup.find_all('p', {"class": "type"})
        plot_sum = lis[1]
        # print(plot_sum)
        pl = plot_sum.get_text().split(':')
        pl.remove(pl[0])
        sum = ""
        # print plot summary
        plot_summary = sum.join(pl)
        # print the type of show
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
        ep_num = int(source_url.get("ep_end"))
        kkeeyyb = [
            [InlineKeyboardButton("Download Ad-Free", callback_data=f"dl {message.text}")],
        ]
        reply_markup = InlineKeyboardMarkup(kkeeyyb)
        message.reply_text(f"""[{tit_url}]({imgg})
        
**{tit_url} ({year})**
        
**{oth_names}**
        
**Type: **`{type_of_show}`
        
**Status: **`{status}`
        
**Genres: **`{genres}`
        
**Episodes: **`{ep_num}`
        
**Summary: **`{plot_summary}`""", reply_markup=reply_markup, parse_mode="markdown")
    except:
        pass