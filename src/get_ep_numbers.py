# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *
import requests
from bs4 import BeautifulSoup

# get episodes from specific range, specified in get_episodes_index

def get_ep(client, callback_query):
    dataInitial = callback_query.data
    dataSplit = dataInitial.split("_")
    animeid = dataSplit[1]
    ep_index_num = dataSplit[2]
    global list_more_anime
    query = callback_query
    data = query.data
    query.answer("Fetching Episodes...")
    data_spl = data.split("_")
    # print(data_spl)
    animelink = f'https://gogoanime.ai/category/{data_spl[1]}'
    response = requests.get(animelink)
    plainText = response.text
    soup = BeautifulSoup(plainText, "lxml")
    tit_url = soup.find("div", {"class": "anime_info_body_bg"}).h1.string
    lnk = soup.find(id="episode_page")
    try:
        source_url = lnk.findAll("li")
        for link in source_url:
            list_more_anime = []
            list_more_anime.append(link.a)
        ep_num_tot = list_more_anime[0].get("ep_end")
        ep_num_tot_range = int(ep_num_tot) + 1
    except:
        source_url = lnk.find("li").a
        ep_num_tot = source_url.get("ep_end")
        ep_num_tot_range = int(ep_num_tot) + 1
    listInitial = []
    for i in range(1, ep_num_tot_range):
        listInitial.append(i)
    n = 40
    listOrganisedInitial = [listInitial[i:i + n] for i in range(0, len(listInitial), n)]
    keyb_eps = []
    for i in listOrganisedInitial[int(ep_index_num)]:
        keyb_eps.append((InlineKeyboardButton(f'{i}', callback_data=f"eps_{i}_{animeid}")))
    m=5
    keybrd_inline_butt = [keyb_eps[i:i + m] for i in range(0, len(keyb_eps), m)]
    keybrd_inline_butt.append([InlineKeyboardButton("◀️ Back", callback_data=f"dl_{animeid}")])
    reply_markups = InlineKeyboardMarkup(keybrd_inline_butt)
    query.edit_message_reply_markup(reply_markup=reply_markups)