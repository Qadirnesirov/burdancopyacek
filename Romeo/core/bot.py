import sys
import config
from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import BotCommand
from Romeo.logging import LOGGER


class ZatraBot(Client):
    def __init__(self):       
        LOGGER(__name__).info(f"Başlanğıc Bot")
        super().__init__(
            name="RomeoRJ",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,        
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.id = get_me.id
        self.name = get_me.first_name
        self.username = get_me.username                
        try:
            await self.send_message(
                config.LOG_GROUP_ID, "Zatra başladı"
            )
        except:
            LOGGER(__name__).error(
                "Bot jurnal qrupuna daxil ola bilmədi. Botunuzu log kanalınıza əlavə etdiyinizə və admin kimi yüksəldiyinizə əmin olun!"
            )
            sys.exit()
        if config.SET_CMDS == str(True):
            try:
                await self.set_bot_commands(
                    [
                        BotCommand("ping", "Botun sağ və ya ölü olduğunu yoxlayın"),
                        BotCommand("play", "Tələb olunan mahnını ifa etməyə başlayır"),
                        BotCommand("skip", "Növbədə olan növbəti trekə keçir"),
                        BotCommand("pause", "Cari ifa olunan mahnını dayandırın"),
                        BotCommand("resume", "Dayandırılmış mahnını davam etdirin"),
                        BotCommand("end", "Növbəni təmizləyin və səsli söhbəti tərk edin"),
                        BotCommand("shuffle", "Növbəyə qoyulmuş pleylisti təsadüfi qarışdırır."),
                        BotCommand("playmode", "Söhbətiniz üçün standart oyun rejimini dəyişməyə imkan verir"),
                        BotCommand("settings", "Söhbətiniz üçün musiqi botunun parametrlərini açın.")
                        ]
                    )
            except:
                pass
        else:
            pass
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "Zəhmət olmasa Botu Logger Qrupunda Admin kimi tanıtın"
            )
            sys.exit()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"ZatraMusicBot kimi başladı {self.name}")
