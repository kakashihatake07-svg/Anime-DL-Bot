# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.handlers import *
from src.anime_search import anime_search
from src.start_message import start_message
from src.dev_info import dev_info
import logging
from src.genres import genres
from src.genre_results import genre_results
from src.get_anime_details import anime_details
from src.inline_search import inline_search
from src.get_episodes_index import get_epIndex
from src.get_episode_link import get_ep_link
from src.instructions import instructions
from src.airing import airing_eps
from src.inline_search_results import anime_inline_details
from src.get_ep_numbers import get_ep
import config

# Logging is optional
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Creating a Session to activate all Handlers
bot = Client(
    "YOUR_SESSION_NAME",
    api_id=config.api_id,
    api_hash=config.api_hash,
    bot_token=config.bot_token
)

# Adding all functions to Handlers in main() function
def main():
    bot.add_handler(MessageHandler(anime_search, filters.regex(r'search')), group=1)
    bot.add_handler(MessageHandler(start_message, filters.command('start')), group=2)
    bot.add_handler(MessageHandler(dev_info, filters.command('info')), group=3)
    bot.add_handler(MessageHandler(genres, filters.command('genres')), group=4)
    bot.add_handler(InlineQueryHandler(inline_search), group=6)
    bot.add_handler(MessageHandler(airing_eps, filters.command("airing")), group=7)
    bot.add_handler(CallbackQueryHandler(anime_details, filters.regex('dt_*')), group=8)
    bot.add_handler(CallbackQueryHandler(get_epIndex, filters.regex('dl_*')), group=9)
    bot.add_handler(CallbackQueryHandler(get_ep_link, filters.regex('eps_*')), group=10)
    bot.add_handler(CallbackQueryHandler(genre_results, filters.regex('genre/')), group=11)
    bot.add_handler(CallbackQueryHandler(instructions, filters.regex('instructions')), group=12)
    bot.add_handler(MessageHandler(anime_inline_details, filters.text), group=13)
    bot.add_handler(CallbackQueryHandler(get_ep, filters.regex('eplink_*')), group=14)

# Calling main method and handlers, polling state
if __name__ == '__main__':
    bot.run(main())