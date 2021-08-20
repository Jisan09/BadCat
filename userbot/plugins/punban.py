# Created by @Jisan7509
# All rights reserved.

import asyncio
import os

import requests
from bs4 import BeautifulSoup
from pySmartDL import SmartDL
from telethon.errors.rpcerrorlist import WebpageCurlFailedError
from urlextract import URLExtract

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import age_verification
from ..helpers.utils import _catutils, reply_id
from . import catub, useless

API = useless.API
horny = useless.nsfw(useless.pawn)

plugin_category = "useless"


@catub.cat_cmd(
    pattern="porn(?:\s|$)([\s\S]*)",
    command=("porn", plugin_category),
    info={
        "header": "Get a porn video or gif or pic.",
        "usage": [
            "{tr}porn",
            "{tr}porn <options/subreddit>",
        ],
        "examples": "{tr}porn nsfw_gifs",
        "options": horny,
    },
)
async def very(event):
    """Random porn post"""
    reply_to = await reply_id(event)
    sub_r = event.pattern_match.group(1)
    await edit_or_reply(event, "**Just hold a sec u horny kid...**")
    if await age_verification(event, reply_to):
        return
    flag = await useless.importent(event)
    if flag:
        return
    max_try = 0
    while max_try < 5:
        subreddit_api = f"{API}/{sub_r}" if sub_r else f"{API}/60fpsporn"
        try:
            cn = requests.get(subreddit_api)
            r = cn.json()
        except ValueError:
            return await edit_delete(event, "Value error!.")
        try:
            postlink = r["postLink"]
            title = r["title"]
            media_url = r["url"]
        except KeyError:
            return await edit_delete(
                event,
                "**(ノಠ益ಠ)ノ  Tou sure this a vaid catagory/subreddit ??**",
                time=20,
            )
        if "https://i.imgur.com" in media_url and media_url.endswith(".gifv"):
            media_url = media_url.replace(".gifv", ".mp4")
        elif "https://redgifs.com/watch" in media_url:
            try:
                source = requests.get(media_url)
                soup = BeautifulSoup(source.text, "lxml")
                links = [
                    itm["content"] for itm in soup.findAll("meta", property="og:video")
                ]
                try:
                    media_url = links[1]
                except IndexError:
                    media_url = links[0]
            except IndexError:
                pass
        try:
            sandy = await event.client.send_file(
                event.chat_id,
                media_url,
                caption=f"<b><a href = {postlink}>{title}</a></b>",
                reply_to=reply_to,
                parse_mode="html",
            )
            if media_url.endswith((".mp4", ".gif")):
                await _catutils.unsavegif(event, sandy)
            await event.delete()
            break
        except WebpageCurlFailedError:
            await edit_or_reply(event, f"**Value error!!..Link is :** {media_url}")
            await asyncio.sleep(3)
            await edit_or_reply(
                event,
                f"**Just hold your candel and Sit tight....\n\nAuto retry limit = {max_try+1}/5**",
            )
            await asyncio.sleep(1)
            max_try += 1
            if max_try == 5:
                await edit_delete(
                    event,
                    "**ಥ‿ಥ   Sorry i could'nt found, try with difference catagory**",
                )


@catub.cat_cmd(
    pattern="bulkporn(?:\s|$)([\s\S]*)",
    command=("bulkporn", plugin_category),
    info={
        "header": "download porn videos or gifs or pics in bulk.",
        "usage": [
            "{tr}bulkporn",
            "{tr}bulkporn <count> <options/subreddit>",
        ],
        "examples": "{tr}bulkporn 10 nsfw_gifs",
        "options": horny,
    },
)
async def bad(event):
    """Download porn in bulk"""
    reply_to = await reply_id(event)
    intxt = event.pattern_match.group(1)
    if intxt and " " in intxt:
        count, sub_r = intxt.split(" ")
    else:
        count = 1
        sub_r = "60fpsporn"
    count = int(count)
    if count > 30:
        return await edit_delete(event, "**Value error!.. Count value 1 to 30**")
    await edit_or_reply(event, "**Just hold a sec u horny kid...**")
    if await age_verification(event, reply_to):
        return
    flag = await useless.importent(event)
    if flag:
        return
    subreddit_api = f"{API}/{sub_r}/{count}"
    try:
        cn = requests.get(subreddit_api)
        r = cn.json()
    except ValueError:
        return await edit_delete(event, "Value error!.")
    title = []
    postlink = []
    media_url = []
    try:
        for x in r["memes"]:
            postlink.append(x["postLink"])
        for x in r["memes"]:
            title.append(x["title"])
        for x in r["memes"]:
            media_url.append(x["url"])
    except KeyError:
        return await edit_delete(
            event, "**(ノಠ益ಠ)ノ  Tou sure this a vaid catagory/subreddit ??**", time=20
        )
    i = 0
    for m, p, t in zip(media_url, postlink, title):
        if "https://i.imgur.com" in m and m.endswith(".gifv"):
            media_url = m.replace(".gifv", ".mp4")
        elif "https://redgifs.com/watch" in m:
            try:
                source = requests.get(m)
                soup = BeautifulSoup(source.text, "lxml")
                links = [
                    itm["content"] for itm in soup.findAll("meta", property="og:video")
                ]
                try:
                    media_url = links[1]
                except IndexError:
                    media_url = links[0]
            except IndexError:
                media_url = m
        else:
            media_url = m
        try:
            sandy = await event.client.send_file(
                event.chat_id,
                media_url,
                caption=f"<b><a href = {p}>{t}</a></b>",
                reply_to=reply_to,
                parse_mode="html",
            )
            if media_url.endswith((".mp4", ".gif")):
                await _catutils.unsavegif(event, sandy)
            await edit_or_reply(
                event,
                f"**Bluk Download Started.\n\nCatagory :  `{sub_r}`\nFile Downloaded :  {i+1}/{count}**",
            )
            await asyncio.sleep(2)
        except WebpageCurlFailedError:
            await event.client.send_message(
                event.chat_id, f"**Value error!!..Link is :** {m}"
            )
        i += 1
        if i == count:
            await event.delete()


@catub.cat_cmd(
    pattern="rsearch(?:\s|$)([\s\S]*)",
    command=("rsearch", plugin_category),
    info={
        "header": "Get a list porn video or gif or pic from reddit /redgif /imgur.",
        "usage": [
            "{tr}rsearch",
            "{tr}rsearch <count> <options/subreddit>",
        ],
        "examples": "{tr}rsearch 10 nsfw_gifs",
        "options": horny,
    },
)
async def pussy(event):
    """Send a list of reddit posts"""
    reply_to = await reply_id(event)
    intxt = event.pattern_match.group(1)
    if intxt and " " in intxt:
        count, sub_r = intxt.split(" ")
    else:
        count = 1
        sub_r = "60fpsporn"
    count = int(count)
    if count > 30:
        return await edit_delete(event, "**Value error!.. Count value 1 to 30**")
    await edit_or_reply(event, "**Just hold a sec u horny kid...**")
    subreddit_api = f"{API}/{sub_r}/{count}"
    try:
        cn = requests.get(subreddit_api)
        r = cn.json()
    except ValueError:
        return await edit_delete(event, "Value error!.")
    if await age_verification(event, reply_to):
        return
    flag = await useless.importent(event)
    if flag:
        return
    title = []
    media_url = []
    try:
        for x in r["memes"]:
            title.append(x["title"])
        for x in r["memes"]:
            media_url.append(x["url"])
    except KeyError:
        return await edit_delete(
            event, "**(ノಠ益ಠ)ノ  Tou sure this a vaid catagory/subreddit ??**", time=20
        )
    pwnlist = f"<b>{count} results for {sub_r} :</b>\n\n"
    for i, (m, t) in enumerate(zip(media_url, title), start=1):
        if "https://i.imgur.com" in m and m.endswith(".gifv"):
            media_url = m.replace(".gifv", ".mp4")
        elif "https://redgifs.com/watch" in m:
            try:
                source = requests.get(m)
                soup = BeautifulSoup(source.text, "lxml")
                links = [
                    itm["content"] for itm in soup.findAll("meta", property="og:video")
                ]
                try:
                    media_url = links[1]
                except IndexError:
                    media_url = links[0]
            except IndexError:
                media_url = m
        else:
            media_url = m
        pwnlist += f"<b><i>{i}. <a href = {media_url}>{t}</a></b>\n"
    await edit_or_reply(event, pwnlist, parse_mode="html")


@catub.cat_cmd(
    pattern="xsearch(?:\s|$)([\s\S]*)",
    command=("xsearch", plugin_category),
    info={
        "header": "Get a list of porn videos from xvideo",
        "usage": [
            "{tr}xsearch",
            "{tr}xsearch <search> <count> ",
            "{tr}xsearch <search> ; <count> ; <page no>",
        ],
        "examples": [
            "{tr}xsearch",
            "{tr}xsearch stepsis ; 10",
            "{tr}xsearch stepsis ; 10 ; 3",
        ],
    },
)
async def cat(event):
    """Send a list of xvideos posts"""
    reply_to = await reply_id(event)
    intxt = event.pattern_match.group(1)
    page = 0
    xcount = None
    if intxt and ";" in intxt:
        try:
            xtext, xcount, page = intxt.split(";")
        except ValueError:
            xtext, xcount = intxt.split(";")
    elif intxt:
        xtext = intxt
    else:
        xtext = "stepsis"
    if await age_verification(event, reply_to):
        return
    flag = await useless.importent(event)
    if flag:
        return
    page = requests.get(f"https://www.xvideos.com/?k={xtext}&p={int(page)}")
    soup = BeautifulSoup(page.text, "lxml")
    col = soup.findAll("div", {"class": "thumb"})
    if not col:
        return await edit_delete(
            event, "`No links found for that query , try differnt search...`", 60
        )
    await edit_or_reply(event, "**Just hold a min you horny kid...**")
    listlink = []
    listname = []
    for i in col:
        a = i.find("a")
        tmplink = a.get("href")
        links = f"https://www.xvideos.com{tmplink}"
        listlink.append(links)
        name = tmplink.split("/")[2]
        listname.append(name)
    await edit_or_reply(
        event,
        f"**{len(listlink)} results found for {xtext} :\nSending {xcount} results out of them.**",
    )
    string = f"<b>Showing {xcount}/{len(listlink)} results for {xtext}.</b>\n\n"
    mylink = listlink[: int(xcount)] if xcount else listlink
    for count, (l, n) in enumerate(zip(mylink, listname), start=1):
        req = requests.get(l)
        soup = BeautifulSoup(req.text, "lxml")
        soups = soup.find("div", {"id": "video-player-bg"})
        for a in soups.find_all("a", href=True):
            link = a["href"]
        string += (
            f"<b><i>{count}. <a href = {link}>{n.replace('_',' ').title()}</a></b>\n"
        )
    await edit_or_reply(event, string, parse_mode="html")


@catub.cat_cmd(
    pattern="linkdl(?: |$)([\s\S]*)",
    command=("linkdl", plugin_category),
    info={
        "header": "download porn video or gif in bulk or single from xvideos, imgur or redgif or direct link.\n\nFor multiple link give one space between links or reply to to any link contain text, like listporn or xsearch post",
        "usage": "{tr}linkdl <input link /reply to link>",
        "examples": "{tr}linkdl https://redgifs.com/watch/virtuousgorgeousindianspinyloach https://i.imgur.com/3Ffkon9.gifv",
    },
)
async def wants_ur_noods(event):
    """Download ~~porns~~ *posts from link"""
    reply_to = await reply_id(event)
    intxt = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    if not intxt and reply:
        intxt = reply.text
    if not intxt:
        return await edit_delete(
            event,
            "**ಠ∀ಠ  Reply to valid link or give valid link url as input...you moron!!**",
        )
    extractor = URLExtract()
    plink = extractor.find_urls(intxt)
    await edit_or_reply(event, "** Just hold a sec u horny kid...**")
    if await age_verification(event, reply_to):
        return
    flag = await useless.importent(event)
    if flag:
        return
    i = 0
    for m in plink:
        if not m.startswith("https://"):
            return await edit_delete(
                event, "**(ノಠ益ಠ)ノ Give me a vaid link to download**"
            )
        if "xvideo" in m:
            if ".mp4" not in m:
                req = requests.get(m)
                soup = BeautifulSoup(req.text, "lxml")
                soups = soup.find("div", {"id": "video-player-bg"})
                for a in soups.find_all("a", href=True):
                    m = a["href"]
            await edit_or_reply(
                event,
                "**Just hold your candel & sit tight, It will take some time...**",
            )
            if not os.path.isdir("./xvdo"):
                os.mkdir("./xvdo")
            xvdo = SmartDL(m, "./xvdo/porn.mp4", progress_bar=False)
            xvdo.start(blocking=False)
            xvdo.wait("finished")
            media_url = "./xvdo/porn.mp4"
        elif "https://i.imgur.com" in m and m.endswith(".gifv"):
            media_url = m.replace(".gifv", ".mp4")
        elif "https://redgifs.com/watch" in m:
            try:
                source = requests.get(m)
                soup = BeautifulSoup(source.text, "lxml")
                links = [
                    itm["content"] for itm in soup.findAll("meta", property="og:video")
                ]
                try:
                    media_url = links[1]
                except IndexError:
                    media_url = links[0]
            except IndexError:
                media_url = m
        else:
            media_url = m
        try:
            sandy = await event.client.send_file(
                event.chat_id, media_url, reply_to=reply_to
            )
            if media_url.endswith((".mp4", ".gif")):
                await _catutils.unsavegif(event, sandy)
            if os.path.exists(media_url):
                os.remove(media_url)
            await edit_or_reply(
                event, f"**Download Started.\n\nFile Downloaded :  {i+1}/{len(plink)}**"
            )
            await asyncio.sleep(2)
        except WebpageCurlFailedError:
            await event.client.send_message(
                event.chat_id, f"**Value error!!..Link is :** {m}"
            )
        i += 1
        if i == len(plink):
            await event.delete()
            if os.path.isdir("./xvdo"):
                os.rmdir("./xvdo")
