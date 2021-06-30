"""NEKOS MODULE FOR PEPEBOT
Plugin Made by [NIKITA](https://t.me/kirito6969)
**DON'T EVEN TRY TO CHANGE CREDITS**'
"""

import os

import nekos
import requests
from fake_useragent import UserAgent
from PIL import Image
from simplejson.errors import JSONDecodeError

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import age_verification
from ..helpers.utils import _catutils, reply_id
from . import catub, useless

plugin_category = "useless"


def user_agent():
    return UserAgent().random


@catub.cat_cmd(
    pattern="nn ?([\s\S]*)",
    command=("nn", plugin_category),
    info={
        "header": "Contains NSFW \nSearch images from nekos",
        "usage": "{tr}nn <argument from choice>",
        "examples": "{tr}nn neko",
        "Choice": useless.nsfw(useless.hemtai),
    },
)
async def _(event):
    "Search images from nekos"
    reply_to = await reply_id(event)
    choose = event.pattern_match.group(1)
    if choose not in useless.hemtai:
        return await edit_delete(
            event,
            f"**Wrong catagory!! Choose from here:**\n\n{useless.nsfw(useless.hemtai)}",
            60,
        )
    if await age_verification(event, reply_to):
        return
    catevent = await edit_or_reply(event, "`Processing Nekos...`")
    flag = await useless.importent(event)
    if flag:
        return
    target = nekos.img(f"{choose}")
    nohorny = await event.client.send_file(
        event.chat_id, file=target, caption=f"**{choose}**", reply_to=reply_to
    )
    await _catutils.unsavegif(event, nohorny)
    await catevent.delete()


@catub.cat_cmd(
    pattern="dva$",
    command=("dva", plugin_category),
    info={
        "header": "Search dva images",
        "usage": "{tr}dva",
    },
)
async def dva(event):
    "Search dva images"
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    try:
        nsfw = requests.get(
            "https://api.computerfreaker.cf/v1/dva",
            headers={"User-Agent": user_agent()},
        ).json()
        url = nsfw.get("url")
    except JSONDecodeError:
        return await edit_delete(
            event, "`uuuf.. seems like api down, try again later.`"
        )
    if not url:
        return await edit_delete(event, "`uuuf.. No URL found from the API`")
    await event.client.send_file(event.chat_id, file=url, reply_to=reply_to)
    await event.delete()


@catub.cat_cmd(
    pattern="nsfw$",
    command=("nsfw", plugin_category),
    info={
        "header": "NSFW \nSearch nsfw from nekos",
        "usage": "{tr}nsfw",
    },
)
async def avatarlewd(event):
    "NSFW. Search nsfw from nekos"
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    flag = await useless.importent(event)
    if flag:
        return
    with open("temp.png", "wb") as f:
        target = "nsfw_avatar"
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    await event.client.send_file(
        event.chat_id, file=open("temp.webp", "rb"), reply_to=reply_to
    )
    os.remove("temp.webp")
    await event.delete()


@catub.cat_cmd(
    pattern="lewdn$",
    command=("lewdn", plugin_category),
    info={
        "header": "NSFW \nSearch lewd nekos",
        "usage": "{tr}lewdn",
    },
)
async def lewdn(event):
    "NSFW.Search lewd nekos"
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    flag = await useless.importent(event)
    if flag:
        return
    nsfw = requests.get("https://nekos.life/api/lewd/neko").json()
    url = nsfw.get("neko")
    if not url:
        return await edit_delete(event, "`Uff.. No NEKO found from the API`")
    await event.client.send_file(event.chat_id, file=url, reply_to=reply_to)
    await event.delete()


@catub.cat_cmd(
    pattern="gasm$",
    command=("gasm", plugin_category),
    info={
        "header": "NSFW \nIt's gasm",
        "usage": "{tr}gasm",
    },
)
async def gasm(event):
    "NSFW. It's gasm"
    reply_to = await reply_id(event)
    if await age_verification(event, reply_to):
        return
    flag = await useless.importent(event)
    if flag:
        return
    with open("temp.png", "wb") as f:
        target = "gasm"
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    await event.client.send_file(
        event.chat_id, file=open("temp.webp", "rb"), reply_to=reply_to
    )
    os.remove("temp.webp")
    await event.delete()


@catub.cat_cmd(
    pattern="ifu$",
    command=("ifu", plugin_category),
    info={
        "header": "Search waifus from nekos",
        "usage": "{tr}ifu",
    },
)
async def waifu(event):
    "Search waifus from nekos"
    reply_to = await reply_id(event)
    with open("temp.png", "wb") as f:
        target = "waifu"
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    await event.client.send_file(
        event.chat_id, file=open("temp.webp", "rb"), reply_to=reply_to
    )
    os.remove("temp.webp")
    await event.delete()
