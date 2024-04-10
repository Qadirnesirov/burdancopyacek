import sys

from pyrogram import Client

import config

from Romeo.logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="ZatraMusic1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="ZatraMusic2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="ZatraMusic3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="ZatraMusic4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="ZatraMusic5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Gettings Assistants Info...")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("zatrasport")
                await self.one.join_chat("zatrasport")
            except:
                pass
            assistants.append(1)
            get_me = await self.one.get_me()
            self.one.username = get_me.username
            self.one.id = get_me.id
            self.one.mention = get_me.mention
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.one.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.one.name = get_me.first_name
            LOGGER(__name__).info(
                f"Assistent olaraq başladı {self.one.name}"
            )
            try:
                await self.one.send_message(
                    config.LOG_GROUP_ID, f"Assistent başladı"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistent Hesabı 1 log Qrupuna daxil ola bilmədi. Köməkçinizi log qrupunuza əlavə etdiyinizə və admin kimi yüksəldiyinizə əmin olun! "
                )
                sys.exit()
        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("zatrasport")
                await self.two.join_chat("zatrasport")
            except:
                pass
            assistants.append(2)
            get_me = await self.two.get_me()
            self.two.username = get_me.username
            self.two.id = get_me.id
            self.two.mention = get_me.mention
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.two.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.two.name = get_me.first_name
            try:
                await self.two.send_message(
                    config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} İkinci köməkçi başladı :**\n\n✨ id : `{self.two.id}`\n❄ Name : {self.two.name}\n💫 Username : @{self.two.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistent Hesabı 2 log Qrupuna daxil ola bilmədi. Köməkçinizi log qrupunuza əlavə etdiyinizə və admin kimi yüksəldiyinizə əmin olun! "
                )
                sys.exit()
            LOGGER(__name__).info(
                f"İkinci köməkçi olaraq başladı {self.two.name}"
            )
        if config.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("zatrasport")
                await self.three.join_chat("zatrasport")
            except:
                pass
            assistants.append(3)
            get_me = await self.three.get_me()
            self.three.username = get_me.username
            self.three.id = get_me.id
            self.three.mention = get_me.mention
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.three.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.three.name = get_me.first_name
            try:
                await self.three.send_message(
                    config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} Üçüncü köməkçi başladı :**\n\n✨ id : `{self.three.id}`\n❄ Name  : {self.three.name}\n💫 Username : @{self.three.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistent Hesabı 3 log Qrupuna daxil ola bilmədi. Köməkçini günlük qrupunuza əlavə etdiyinizə və admin kimi yüksəldiyinizə əmin olun! "
                )
                sys.exit()
            LOGGER(__name__).info(
                f"Üç köməkçisi olaraq başladı {self.three.name}"
            )
        if config.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("zatrasport")
                await self.four.join_chat("zatrasport")
            except:
                pass
            assistants.append(4)
            get_me = await self.four.get_me()
            self.four.username = get_me.username
            self.four.id = get_me.id
            self.four.mention = get_me.mention
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.four.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.four.name = get_me.first_name
            try:
                await self.four.send_message(
                    config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} Dördüncü köməkçi başladı :**\n\n✨ id : `{self.four.id}`\n❄ Name : {self.four.name}\n💫 Username : @{self.four.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistent Hesabı 4 log Qrupuna daxil ola bilmədi. Köməkçinizi log qrupunuza əlavə etdiyinizə və admin kimi yüksəldiyinizə əmin olun! "
                )
                sys.exit()
            LOGGER(__name__).info(
                f"Dörd köməkçisi olaraq başladı {self.four.name}"
            )
        if config.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("zatrasport")
                await self.five.join_chat("zatrasport")
            except:
                pass
            assistants.append(5)
            get_me = await self.five.get_me()
            self.five.username = get_me.username
            self.five.id = get_me.id
            self.five.mention = get_me.mention
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.five.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.five.name = get_me.first_name
            try:
                await self.five.send_message(
                    config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} Beşinci köməkçi başladı :**\n\n✨ id : `{self.five.id}`\n❄ Name: {self.five.name}\n💫 username : @{self.five.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistent Hesabı 5 log Qrupuna daxil ola bilmədi. Köməkçinizi log qrupunuza əlavə etdiyinizə və admin kimi yüksəldiyinizə əmin olun!"
                )
                sys.exit()
            LOGGER(__name__).info(
                f"Köməkçi beş olaraq başladı {self.five.name}"
            )
