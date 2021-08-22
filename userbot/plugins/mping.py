# ==================================================================================================
# Made by https://t.me/deepaiims
# It is simillar to my other plugin 'pping' (ping with media)
# This randomly chooses from the given media links, i.e 'multi-pping', in short 'mping'

import asyncio
import os
import random
from datetime import datetime

from userbot import catub

from ..core.managers import edit_or_reply
from ..sql_helper.globals import gvarstatus
from . import catub, hmention, reply_id

plugin_category = "tools"

# =========Some integrated custom vars============
# Pre text i.e. before calculation ping
PING_TEXT = os.environ.get("PING_TEXT") or "𝔖𝔱𝔞𝔯𝔱𝔦𝔫𝔤 𝔗𝔥𝔢 𝔊𝔞𝔪𝔢!!"
# Post text i.e. the final message
PONG_TEXT = os.environ.get("PONG_TEXT") or "𝔑𝔬𝔴, 𝔏𝔢𝔱 𝔗𝔥𝔢 𝔊𝔞𝔪𝔢 𝔅𝔢𝔤𝔦𝔫!!"
# Custom mention line
PING_MENTION = os.environ.get("PING_MENTION") or "ℜ𝔲𝔩𝔢𝔰 𝔅𝔶"
# Text after the ping value
PING_PARTNER = os.environ.get("PING_PARTNER") or "𝔪𝔰"
normaltext = "1234567890."
pingfont = [
    "𝟏",
    "𝟐",
    "𝟑",
    "𝟒",
    "𝟓",
    "𝟔",
    "𝟕",
    "𝟖",
    "𝟗",
    "𝟎",
    "•",
]

# ================================================

# ===============================================


@catub.cat_cmd(
    pattern="mping$",
    command=("mping", plugin_category),
    info={
        "header": "Checks the latency of userbot from the server, with a media",
        "option": "VARS to customize the texts of mping\nPING_PICS add mutiple telegraph media link separated by spaces(in database).\nPING_TEXT Pre text i.e. before calculation ping.\nPONG_TEXT Post text i.e. the final message.\nPING_MENTION Custom mention line.\nPING_PARTNER Text after ping(that random number)\nAVG_TEXT Custom header in `{tr}ping -a`",
        "usage": "{tr}mping",
    },
)
async def _(event):
    "Shows ping with a given random media"
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    # add space b/w each telegraph link
    PING_PICS = (gvarstatus("PING_PICS") or "https://telegra.ph/file/1328d62db93ad22b69ba2.jpg https://telegra.ph/file/b2da6e4c55dd29600e4ed.jpg")
    PING_PICS = PING_PICS.rsplit(" ")
    start = datetime.now()
    cat = await edit_or_reply(event, f"{PING_TEXT}", "html")
    end = datetime.now()
    await cat.delete()
    ms = str((end - start).microseconds / 1000)
    for normal in ms:
        if normal in normaltext:
            pingchars = pingfont[normaltext.index(normal)]
            ms = ms.replace(normal, pingchars)
    PING_PIC = random.choice(PING_PICS)
    if PING_PIC:
        try:
            while PING_PIC == "":
                PING_PIC = random.choice(PING_PICS)
        except IndexError:
            error = "fix"  # This line is just to prevent any NoneType error
        caption = (
            f"{PONG_TEXT}\n<code>{ms}</code> {PING_PARTNER}\n{PING_MENTION} {hmention}"
        )
        await event.client.send_file(
            event.chat_id,
            PING_PIC,
            caption=caption,
            parse_mode="html",
            reply_to=reply_to_id,
            link_preview=False,
            allow_cache=True,
        )


# ==================================================================================================
