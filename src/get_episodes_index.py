# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup

# Splits Inline buttons into ranges of episodes when Episodes counts is greater than 120

def get_epIndex(client, callback_query):
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
        if int(ep_num_tot) > 120:
            listInitial = []
            for i in range(1, ep_num_tot_range):
                listInitial.append(i)
            n = 40
            listOrganisedInitial = [listInitial[i:i + n] for i in range(0, len(listInitial), n)]
            listIndex = []
            for item in listOrganisedInitial:
                listIndex.append(
                    (InlineKeyboardButton(f"{item[0]}-{item.pop()}",
                                          callback_data=f"eplink_{data_spl[1]}_{listOrganisedInitial.index(item)}")))
            o = 3
            listIndexFinal = [listIndex[i:i + o] for i in range(0, len(listIndex), o)]
            listIndexFinal.append([InlineKeyboardButton("◀️ Back", callback_data=f"dt_{data_spl[1]}")])
            repl = InlineKeyboardMarkup(listIndexFinal)
            # print(listIndex)
            query.edit_message_text(text=f"""You selected **{tit_url}**,
    
Select the Episode you want :-""", reply_markup=repl, parse_mode="markdown")
        elif int(ep_num_tot) < 120:
            source_url = lnk.find("li").a
            ep_num_tot = source_url.get("ep_end")
            ep_num_tot_range = int(ep_num_tot) + 1
            n = 5
            keyb_eps = []
            for i in range(1, ep_num_tot_range):
                keyb_eps.append((InlineKeyboardButton(f'{i}', callback_data=f"eps_{i}_{data_spl[1]}")))
            keybrd_inline_butt = [keyb_eps[i:i + n] for i in range(0, len(keyb_eps), n)]
            reply_markups = InlineKeyboardMarkup(keybrd_inline_butt)
            query.edit_message_text(text=f"""You selected **{tit_url}**,

Select the Episode you want :-""", reply_markup=reply_markups, parse_mode="markdown")
    except:
        source_url = lnk.find("li").a
        ep_num_tot = source_url.get("ep_end")
        ep_num_tot_range = int(ep_num_tot) + 1
        n = 5
        keyb_eps = []
        for i in range(1, ep_num_tot_range):
            keyb_eps.append((InlineKeyboardButton(f'{i}', callback_data=f"eps_{i}_{data_spl[1]}")))
        keybrd_inline_butt = [keyb_eps[i:i + n] for i in range(0, len(keyb_eps), n)]
        reply_markups = InlineKeyboardMarkup(keybrd_inline_butt)
        query.edit_message_text(text=f"""You selected **{tit_url}**,

Select the Episode you want :-""", reply_markup=reply_markups, parse_mode="markdown")