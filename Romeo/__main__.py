import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from Zatra import LOGGER, app, userbot
from Zatra.core.call import rj
from Zatra.misc import sudo
from Zatra.plugins import ALL_MODULES
from Zatra.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Zatra.plugins" + all_module)
    LOGGER("plugins").info("Uğurla Import edilmiş Modullar...")
    await userbot.start()
    await rj.start()
    await rj.decorators()
    LOGGER("Zatra").info(
        "bot başladı"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("Zatra").info("Musiqi Botunun dayandırılması...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
