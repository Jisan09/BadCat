# By @kirito6969 for PepeBot
# Don't edit credits Madafaka
"""
This module can search images in danbooru and send in to the chat!
──「 **Danbooru Search** 」──
"""

import os
import urllib

import requests

from userbot import catub

from ..helpers.functions import age_verification
from . import edit_delete, edit_or_reply, reply_id, useless

plugin_category = "useless"


@catub.cat_cmd(
    pattern="ani(mu|nsfw) ?([\s\S]*)",
    command=("ani", plugin_category),
    info={
        "header": "Contains NSFW 🔞.\nTo search images in danbooru!",
        "usage": [
            "{tr}animu <query>",
            "{tr}aninsfw <nsfw query>",
        ],
        "examples": [
            "{tr}animu naruto",
            "{tr}aninsfw naruto",
        ],
    },
)
async def danbooru(event):
    "Get anime charecter pic or nsfw"
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    await edit_or_reply(event, "`Processing…`")
    flag = await useless.importent(event)
    if flag:
        return
    rating = "Explicit" if "nsfw" in event.pattern_match.group(1) else "Safe"
    search_query = event.pattern_match.group(2)
    params = {
        "limit": 1,
        "random": "true",
        "tags": f"Rating:{rating} {search_query}".strip(),
    }
    with requests.get(
        "http://danbooru.donmai.us/posts.json", params=params
    ) as response:
        if response.status_code == 200:
            response = response.json()
        else:
            return await edit_delete(
                event, f"**An error occurred, response code: **`{response.status_code}`"
            )

    if not response:
        return await edit_delete(event, f"**No results for query:** __{search_query}__")
    valid_urls = [
        response[0][url]
        for url in ["file_url", "large_file_url", "source"]
        if url in response[0].keys()
    ]
    if not valid_urls:
        return await edit_delete(
            event, f"**Failed to find URLs for query:** __{search_query}__"
        )
    for image_url in valid_urls:
        try:
            await event.client.send_file(event.chat_id, image_url, reply_to=reply_to)
            await event.delete()
            return
        except Exception as e:
            await edit_or_reply(event, f"{e}")
    await edit_delete(event, f"**Failed to fetch media for query:** __{search_query}__")


@catub.cat_cmd(
    pattern="boobs(?:\s|$)([\s\S]*)",
    command=("boobs", plugin_category),
    info={
        "header": "NSFW 🔞\nYou know what it is, so do I !",
        "usage": "{tr}boobs",
        "examples": "{tr}boobs",
    },
)
async def boobs(e):
    "Search boobs"
    reply_to = await reply_id(e)
    if await age_verification(e, reply_to):
        return
    a = await edit_or_reply(e, "`Sending boobs...`")
    flag = await useless.importent(e)
    if flag:
        return
    nsfw = requests.get("http://api.oboobs.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve(f"http://media.oboobs.ru/{nsfw}", "boobs.jpg")
    await e.client.send_file(e.chat_id, "boobs.jpg", reply_to=reply_to)
    os.remove("boobs.jpg")
    await a.delete()


@catub.cat_cmd(
    pattern="butts(?:\s|$)([\s\S]*)",
    command=("butts", plugin_category),
    info={
        "header": "NSFW 🔞\nBoys and some girls likes to Spank this 🍑",
        "usage": "{tr}butts",
        "examples": "{tr}butts",
    },
)
async def butts(e):
    "Search beautiful butts"
    reply_to = await reply_id(e)
    if await age_verification(e, reply_to):
        return
    a = await edit_or_reply(e, "`Sending beautiful butts...`")
    flag = await useless.importent(e)
    if flag:
        return
    nsfw = requests.get("http://api.obutts.ru/butts/10/1/random").json()[0]["preview"]
    urllib.request.urlretrieve(f"http://media.obutts.ru/{nsfw}", "butts.jpg")
    await e.client.send_file(e.chat_id, "butts.jpg", reply_to=reply_to)
    os.remove("butts.jpg")
    await a.delete()
