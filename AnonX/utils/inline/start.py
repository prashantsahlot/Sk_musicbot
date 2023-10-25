from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🌹𝐀ԃ𝐃 𝐌ҽ 𝐌σ𝐈 𝐋ꪮꪜ𝐄🌹",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="❤️𝐎ɯɳҽ𝐑❤️",
                url=f"https://t.me/HereShiva2",
            )
        ],
        [
            InlineKeyboardButton(
                text="💖𝐇ҽʅ𝐏💖",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="🌸𝐒ҽƚƚιɳɠ𝐒🌸", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="•🌷𝐀ԃ𝐃 𝐌ҽ 𝐓σ 𝐘συ𝐑 𝐆ɾσυ𝐏🌷•",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🍒𝐂σɱɱαɳԃ𝐒🍒", callback_data="settings_back_helper"
            ),
            InlineKeyboardButton(
                text="🥀𝐅συɳԃҽ𝐑🥀", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="💘𝐆ɾσυ𝐏💘", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="💞𝐂нαииє𝐋💞", url=f"https://t.me/over_powered"
            )
        ],
     ]
    return buttons
