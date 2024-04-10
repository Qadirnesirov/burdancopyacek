from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Romeo import app

def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            # text=_["BACK_BUTTON"],
            text="Yeniləmələr",
            url=f"https://t.me/ZaTRaBLoG",
        ),
        InlineKeyboardButton(
            text="Sports Group",
            url=f"t.me/ZatraSport",
        ),
        InlineKeyboardButton(
            text="BiTiR", callback_data=f"close"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Admin",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="Auth",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="BlackList",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="BroAdCast",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="Gban",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="Truth Dare",
                    callback_data="help_callback hb13",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Ping",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="Play 🔊",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="PlayList",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Videochats",
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text="Start",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="Sudo",
                    callback_data="help_callback hb9",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    # text=_["BACK_BUTTON"],
                    text="▷ Back ◁",
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                )
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="▷ Back ◁",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
