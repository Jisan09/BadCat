"""NEKOS MODULE FOR PEPEBOT
Plugin Made by [NIKITA](https://t.me/kirito6969)
**DON'T EVEN TRY TO CHANGE CREDITS**'
"""

import os

import nekos
import requests
from fake_useragent import UserAgent
from PIL import Image

from userbot import catub

from ..core.managers import edit_or_reply
from ..helpers.functions import age_verification
from ..helpers.utils import reply_id

POSSIBLE = [
    "feet",
    "yuri",
    "trap",
    "futanari",
    "hololewd",
    "lewdkemo",
    "solog",
    "feetg",
    "cum",
    "erokemo",
    "les",
    "wallpaper",
    "lewdk",
    "ngif",
    "tickle",
    "lewd",
    "feed",
    "gecg",
    "eroyuri",
    "eron",
    "cum_jpg",
    "bj",
    "nsfw_neko_gif",
    "solo",
    "kemonomimi",
    "nsfw_avatar",
    "gasm",
    "poke",
    "anal",
    "slap",
    "hentai",
    "avatar",
    "erofeet",
    "holo",
    "keta",
    "blowjob",
    "pussy",
    "tits",
    "holoero",
    "lizard",
    "pussy_jpg",
    "pwankg",
    "classic",
    "kuni",
    "waifu",
    "pat",
    "8ball",
    "kiss",
    "femdom",
    "neko",
    "spank",
    "cuddle",
    "erok",
    "fox_girl",
    "boobs",
    "random_hentai_gif",
    "smallboobs",
    "hug",
    "ero",
    "smug",
    "goose",
    "baka",
    "woof",
]


agent = UserAgent()


def user_agent():
    return agent.random


plugin_category = "useless"

neko_help = "**ALL:**  "

for i in POSSIBLE:
    neko_help += f"`{i.lower()}`   "


@catub.cat_cmd(
    pattern="nn ?(.*)",
    command=("nn", plugin_category),
    info={
        "header": "Contains NSFW \nSearch images from nekos",
        "usage": "{tr}nn <argument from choice>",
        "examples": "{tr}nn neko",
        "Choice": neko_help,
    },
)
async def _(event):
    "Search images from nekos"
    reply_to = await reply_id(event)
    choose = event.pattern_match.group(1)
    if choose not in POSSIBLE:
        await edit_or_reply("`Bruh.. What I am supposed to do!`")
        return
    if await age_verification(event, reply_to):
        return
    catevent = await edit_or_reply(event, "`Processing Nekos...`")
    target = nekos.img(f"{choose}")
    await event.client.send_file(
        event.chat_id, file=target, caption=f"**{choose}**", reply_to=reply_to
    )
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
    nsfw = requests.get(
        "https://api.computerfreaker.cf/v1/dva", headers={"User-Agent": user_agent()}
    ).json()
    url = nsfw.get("url")
    if not url:
        await edit_or_reply(event, "`uuuf.. No URL found from the API`")
        return
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
    pattern="icat$",
    command=("icat", plugin_category),
    info={
        "header": "Search cute cats.",
        "usage": "{tr}icat",
    },
)
async def _(event):
    "Search cute cats."
    reply_to = await reply_id(event)
    target = nekos.cat()
    catevent = await edit_or_reply(event, "`Finding ur ket...`")
    await event.client.send_file(event.chat_id, file=target, reply_to=reply_to)
    await catevent.delete()


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
    nsfw = requests.get("https://nekos.life/api/lewd/neko").json()
    url = nsfw.get("neko")
    if not url:
        await edit_or_reply(event, "`Uff.. No NEKO found from the API`")
        return
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
