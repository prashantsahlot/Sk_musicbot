import asyncio
import time

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.future import VideosSearch

import config
from config import BANNED_USERS
from config import OWNER_ID
from strings import get_command, get_string
from AnonX import Telegram, YouTube, app
from AnonX.misc import SUDOERS, _boot_
from AnonX.plugins.playlist import del_plist_msg
from AnonX.plugins.sudoers import sudoers_list
from AnonX.utils.database import (
    add_served_chat,
    add_served_user,
    get_served_chats,
    get_served_users,
    blacklisted_chats,
    get_assistant,
    get_lang,
    get_userss,
    is_on_off,
    is_served_private_chat,
)
from AnonX.utils.decorators.language import LanguageStart
from AnonX.utils.formatters import get_readable_time
from AnonX.utils.inline import help_pannel, private_panel, start_pannel

loop = asyncio.get_running_loop()

@app.on_message(
    filters.command(get_command("MSTART_COMMAND"))
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@LanguageStart
async def start_comm(client, message: Message, _):
    OWNER = OWNER_ID[0]
    out = start_pannel(_, app.username, OWNER)
    return await message.reply_photo(
               photo=config.START_IMG_URL,
               caption=_["start_1"].format(
            message.chat.title, config.MUSIC_BOT_NAME
        ),
        reply_markup=InlineKeyboardMarkup(out),
    )

welcome_group = 2

@app.on_message(filters.new_chat_members, group=welcome_group)
async def welcome(client, message: Message):
    chat_id = message.chat.id
    if config.PRIVATE_BOT_MODE == str(True):
        if not await is_served_private_chat(message.chat.id):
            await message.reply_text(
                "𝐏𝐫𝐢𝐯𝐚𝐭𝐞 𝐃𝐨𝐫𝐞𝐚𝐦𝐨𝐧 𝐑𝐨𝐛𝐨𝐭\n\n𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐓𝐡𝐞 𝐂𝐡𝐚𝐭𝐬 𝐀𝐥𝐥𝐨𝐰𝐞𝐝 𝐁𝐲 𝐌𝐲 𝐎𝐰𝐧𝐞𝐫, 𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐈𝐧 𝐌𝐲 𝐎𝐰𝐧𝐞𝐫'𝐬 𝐏𝐦 𝐓𝐨 𝐀𝐥𝐥𝐨𝐰 𝐘𝐨𝐮𝐫 𝐂𝐡𝐚𝐭 𝐀𝐧𝐝 𝐈𝐟 𝐘𝐨𝐮 𝐃𝐨𝐧𝐭 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐃𝐨 𝐓𝐡𝐞𝐧 𝐌𝐚𝐚 𝐂𝐡𝐮𝐝𝐚𝐨👿 𝐛𝐜𝐨𝐳 𝐈'𝐦 𝐋𝐞𝐚𝐯𝐢𝐧𝐠..."
            )
            return await app.leave_chat(message.chat.id)
    else:
        await add_served_chat(chat_id)
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if member.id == app.id:
                chat_type = message.chat.type
                if chat_type != "supergroup":
                    await message.reply_text(_["start_6"])
                    return await app.leave_chat(message.chat.id)
                if chat_id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_7"].format(
                            f"https://t.me/{app.username}?start=sudolist"
                        )
                    )
                    return await app.leave_chat(chat_id)
                userbot = await get_assistant(message.chat.id)
                OWNER = OWNER_ID[0]
                out = start_pannel(_, app.username, OWNER)
                await message.reply_photo(
                    photo=config.START_IMG_URL,
                    caption=_["start_3"].format(
                        config.MUSIC_BOT_NAME,
                        userbot.username,
                        userbot.id,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
            if member.id in config.OWNER_ID:
                return await message.reply_text(
                    _["start_4"].format(
                        config.MUSIC_BOT_NAME, member.mention
                    )
                )
            if member.id in SUDOERS:
                return await message.reply_text(
                    _["start_5"].format(
                        config.MUSIC_BOT_NAME, member.mention
                    )
                )
            return
        except:
            return
