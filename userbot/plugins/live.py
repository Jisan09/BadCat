from telethon.tl.types import InputMessagesFilterPhotos
from telethon.tl import types
import random
import os
import re
import requests
import time
from datetime import datetime
from platform import python_version

from telethon import version

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import StartTime, catub, catversion, mention

plugin_category = "utils"


@catub.cat_cmd(
    pattern="live$",
    command=("live", plugin_category),
    info={
        "header": "To check bot's alive status",
        "options": "It gives random alive pic, for that you need to set `ALIVE_CHANNEL` __(in dv or heroku)__ with the channel's id or username`(with @)`",
        "usage": [
            "{tr}live",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details"
    start = datetime.now()
    await edit_or_reply(event, "`Checking...`")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "〣"
    #================================================
    api_url = 'https://animechan.vercel.app/api/random'
    quote = False
    while not quote:
        try:
            response = requests.get(api_url).json()
            is_quote = True 
        except:
            pass
    quote = response["quote"]
    while len(quote) > 150:
        res = requests.get(api_url).json()
        quote = res["quote"]
    ANIME_QUOTE = f"__{quote}__"
    ALIVE_CHANNEL = gvarstatus(
        "ALIVE_CHANNEL") or os.environ.get("ALIVE_CHANNEL")
    if ALIVE_CHANNEL.startswith("-"):
        ALIVE_CHANNEL = int(ALIVE_CHANNEL)
    #================================================
    ALIVE_TEXT = ANIME_QUOTE or gvarstatus("ALIVE_TEXT")
    cat_caption = gvarstatus("ALIVE_TEMPLATE") or temp
    caption = cat_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        EMOJI=EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        catver=catversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
    )
    # Auto pic by the gawd Lee @TheLoneEssence
    if ALIVE_CHANNEL:
        done = False
        while not done:
            chat = await event.client.get_entity(ALIVE_CHANNEL)
            photos = await event.client.get_messages(chat.id, 0, filter=InputMessagesFilterPhotos)
            num = photos.total
            pic_id = random.choice(range(num))
            try:
                async for pic in event.client.iter_messages(chat.id, ids=pic_id):
                    if type(pic.media) == types.MessageMediaPhoto:
                        await event.delete()
                        await event.respond(caption, file=pic, reply_to=reply_to_id)
                        done = True
                    else:
                        done = False
            except:
                continue
    else:
        await edit_or_reply(event, caption)


temp = "{ALIVE_TEXT}\n\n\
**{EMOJI} Master : {mention}**\n\
**{EMOJI} Uptime :** `{uptime}`\n\
**{EMOJI} Telethon version :** `{telever}`\n\
**{EMOJI} Catuserbot Version :** `{catver}`\n\
**{EMOJI} Python Version :** `{pyver}`\n\
**{EMOJI} Database :** `{dbhealth}`\n"
