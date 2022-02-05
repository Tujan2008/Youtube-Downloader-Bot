import os
import requests
import time
import traceback
import logging
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.types import User, Message

#Database
import config
from handlers.broadcast import broadcast
from handlers.check_user import handle_user_status
from handlers.database import Database

LOG_CHANNEL = config.LOG_CHANNEL
AUTH_USERS = config.AUTH_USERS
DB_URL = config.DB_URL
DB_NAME = config.DB_NAME

db = Database(DB_URL, DB_NAME)

#Strings
HELP_STRING = """
⚊❮❮❮❮ ｢  Still Wonder How I Work ? 」❯❯❯❯⚊

● Use /start to Start The Bot 🚀
● Use /help to Get the help Menu ❔

**Currently Only Support Video Links. Playlists are not support😁**
"""
ABOUT_STRING = """
● **😀 BOT:** `YouTube Downloader` 
● **👦 CREATOR :** [Mʀ Dᴇᴠɪʟ ⌫](https://t.me/tujan3) 
● **🚀 SERVER :** `Heroku` 
● **📖 LIBRARY :** `Pyrogram` 
● **📃 LANGUAGE :** `Python 3.9` 
● **🤖 Updates :** [SLBotsOfficial](https://t.me/SLBotsOfficial) 
"""
START_STRING = """ 
Hi <b>{message.from_user.first_name}</b>, I'm a YouTube Downloader Bot
Use /help for More info.
A Project By [🇱🇰SL Bots™](https://t.me/SLBotsofficial)
"""

#Buttons
START_BUTTON = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="Help ❓", callback_data="cbhelp"),InlineKeyboardButton(text="About🤖",callback_data="cbabout")
                        ],
                        [
                            InlineKeyboardButton(text="Channel 😇",url="https://t.me/+IU1ta7Gg19VkYzE1"),InlineKeyboardButton("Our Group 😇", url="https://t.me/trtechguide")
                        ]
                    ]
                )

HELP_BUTTON = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="Home🏠",callback_data="cbstart"),InlineKeyboardButton(text="About🤖",callback_data="cbabout")
                        ],
                        [
                            InlineKeyboardButton(text="Channel 📢",url="https://t.me/+IU1ta7Gg19VkYzE1"),InlineKeyboardButton(text="Group 👨‍👨‍👧‍👦",url="https://t.me/trtechguide")
                        ]
                    ]
                )

ABOUT_BUTTON = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="Help❔",callback_data="cbhelp"),InlineKeyboardButton(text="Home🏠",callback_data="cbstart")
                        ],
                        [
                            InlineKeyboardButton(text="Channel 📢",url="https://t.me/+IU1ta7Gg19VkYzE1"),InlineKeyboardButton(text="Group 👨‍👨‍👧‍👦",url="https://t.me/trtechguide")
                        ]
                    ]
                )

START_IMG = "https://telegra.ph/file/88446249a9c8aedded515.jpg"


@Client.on_message(filters.command(["start"]), group=-2)
async def startprivate(client, message):
    chat_id = message.from_user.id
    if not await db.is_user_exist(chat_id):
        data = await client.get_me()
        BOT_USERNAME = data.username
        await db.add_user(chat_id)
        if LOG_CHANNEL:
            await client.send_message(
                LOG_CHANNEL,
                f"#NEWUSER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) started @{BOT_USERNAME} !!",
            )
        else:
            logging.info(f"#NewUser :- Name : {message.from_user.first_name} ID : {message.from_user.id}")
    await message.send_photo(
                START_IMG,
                caption=START_STRING,
                reply_markup=InlineKeyboardMarkup(START_BUTTON),
                quote=True,
            )
        
@Client.on_message(filters.command(["help"]))
async def help(bot, update):
    text = HELP_STRING.format(update.from_user.mention)
    reply_markup = HELP_BUTTON
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup,
        quote=True
    )        

@Client.on_message(filters.private & filters.command("broadcast"))
async def broadcast_handler_open(_, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    if m.reply_to_message is None:
        await m.delete()
    else:
        await broadcast(m, db)


@Client.on_message(filters.private & filters.command("stats"))
async def sts(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    await m.reply_text(
        text=f"**Total Users in Database 📂:** `{await db.total_users_count()}`",
        parse_mode="Markdown",
        quote=True
    )    

        
#Callback
    
@Client.on_callback_query()
async def cb_data(bot, update):  
    if update.data == "cbhelp":
        await update.message.edit_text(
            text=HELP_STRING,
            reply_markup=HELP_BUTTON,
            disable_web_page_preview=True
        )
    elif update.data == "cbabout":
        await update.message.edit_text(
            text=ABOUT_STRING,
            reply_markup=ABOUT_BUTTON,
            disable_web_page_preview=True
        )
    elif update.data == "cbstart":
        await update.message.edit_text(
            text=START_STRING,
            reply_markup=START_BUTTON,
            disable_web_page_preview=True
        )
