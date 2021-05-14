# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from uuid import uuid4

# Inline Anime Search

def inline_search(client, inline_query):
    url = f"https://gogoanime.ai//search.html?keyword={inline_query.query}"
    session = HTMLSession()
    response = session.get(url)
    response_html = response.text
    soup = BeautifulSoup(response_html, 'html.parser')
    animes = soup.find("ul", {"class": "items"}).find_all("li")
    # print(animes)
    aAnimes = []
    for anime in animes:  # For every anime found
        rel = anime.find("p", {"class": "released"}).string
        r = rel.split()
        rr = ""
        released_year = rr.join(r)
        tits = anime.a["title"]
        urll = anime.a["href"]
        imgg = anime.img["src"]
        ur = urll.split('/')
        url_of_result = ur[2]
        aAnimes.append(InlineQueryResultArticle(title=f"{tits}", description=f"{released_year}",
                                                input_message_content=InputTextMessageContent(f"{url_of_result}"),
                                                thumb_url=f"{imgg}"))
    inline_query.answer(aAnimes, cache_time=1)