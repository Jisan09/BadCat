# Created by @Jisan7509
# All rights reserved.

import asyncio
import requests
from bs4 import BeautifulSoup

from . import catub
from ..core.logger import logging
from ..core.managers import edit_delete,edit_or_reply
from ..helpers.functions import age_verification
from ..helpers.utils import _catutils, reply_id


API = "https://weaverbottest.herokuapp.com/gimme"

plugin_category = "useless"

pawn = ["nsfw_gifs","60fpsporn","porn","porn_gifs","porninfifteenseconds","CuteModeSlutMode","NSFW_HTML5","the_best_nsfw_gifs","verticalgifs","besthqporngifs","boobs","pussy","jigglefuck","gangbang","passionx","titfuck","HappyEmbarrassedGirls","suicidegirls","porninaminute","SexInFrontOfOthers","tiktoknsfw","tiktokporn","NSFWFunny",]

horny = "**Catagory :** "
for i in pawn:
    horny += f" `{i.lower()}` ||"
    
@catub.cat_cmd(
    pattern="porn(?: |$)(.*)",
    command=("porn", plugin_category),
    info={
        "header": "Get a porn video or gif.",
        "usage": [
        "{tr}porn",
        "{tr}porn <options/subreddit>",
    ],
        "examples": "{tr}porn nsfw_gifs",
        "options":horny,
    },
)
async def bad(event):
    """Random porn post"""
    reply_to = await reply_id(event)
    sub_r = event.pattern_match.group(1)
    await edit_or_reply(event, "**Just hold a sec u horny kid...**")
    max_try = 0
    while(max_try<5):
        subreddit_api = f"{API}/{sub_r}" if sub_r else f"{API}/60fpsporn"
        try:
            cn = requests.get(subreddit_api)
            r = cn.json()
        except ValueError:
            return await edit_delete(event, "Value error!.")
        if await age_verification(event, reply_to):
            return
        postlink = r["postLink"]
        title = r["title"]
        media_url = r["url"]
        captionx = f"<b><a href = {postlink}>{title}</a></b>\n"
        if "https://i.imgur.com" in media_url:
            media_url = media_url.replace(".gifv",".mp4")
        else:
            try:
                source = requests.get(media_url)
                soup = BeautifulSoup(source.text, "lxml")
                links = [itm['content'] for itm in soup.findAll("meta", property = "og:video")]
                try: media_url = links[1]
                except: media_url = links[0]
            except:
                pass
        try:
            sandy = await event.client.send_file(event.chat_id, media_url, caption=captionx,reply_to=reply_to,parse_mode="html")
            await event.delete()
            break
            if media_url.endswith(".gif"):
                await _catutils.unsavegif(event, sandy)
        except:
            await edit_or_reply(event,f"**Value error!!..Link is :** {media_url}")
            await asyncio.sleep(4)
            await edit_or_reply(event,f"**Just hold your dick and Sit tight....\n\nAuto retry limit = {max_try+1}/5**")
            await asyncio.sleep(1)
            max_try +=1
            if max_try==5: await edit_delete(event,"**ಥ‿ಥ   Sorry i could'nt found, try with difference catagory**")



@catub.cat_cmd(
    pattern="bulkporn(?: |$)(.*)",
    command=("bulkporn", plugin_category),
    info={
        "header": "download porn video or gif in bulk.",
        "usage": [
        "{tr}bulkporn",
        "{tr}bulkporn <count> <options/subreddit>",
    ],
        "examples": "{tr}bulkporn 10 nsfw_gifs",
        "options":horny,
    },
)
async def pussy(event):
    """Download porn in bulk"""
    reply_to = await reply_id(event)
    intxt = event.pattern_match.group(1)
    if intxt and " " in intxt:
        count,sub_r = intxt.split(" ")
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
    title = []
    postlink = []
    media_url = []
    for x in r["memes"]: postlink.append(x["postLink"])
    for x in r["memes"]: title.append(x["title"])
    for x in r["memes"]: media_url.append(x["url"])
    i=0
    await event.delete()
    for m,p,t in zip(media_url,postlink,title):
        if "https://i.imgur.com" in m:
            media_url = m.replace(".gifv",".mp4")
        else: 
            try:
                source = requests.get(m)
                soup = BeautifulSoup(source.text, "lxml")
                links = [itm['content'] for itm in soup.findAll("meta", property = "og:video")]
                try: media_url = links[1]
                except: media_url = links[0]
            except:
                    media_url = m
        try:
            sandy = await event.client.send_file(event.chat_id, media_url, caption=f"<b><a href = {p}>{t}</a></b>",reply_to=reply_to,parse_mode="html")
            if media_url.endswith(".gif"):
                await _catutils.unsavegif(event, sandy)
        except:
            await event.client.send_message(event.chat_id,f"**Value error!!..Link is :** {m}")
        i+=1


@catub.cat_cmd(
    pattern="listporn(?: |$)(.*)",
    command=("listporn", plugin_category),
    info={
        "header": "Get a list porn video or gif.",
        "usage": [
        "{tr}listporn",
        "{tr}listporn <count> <options/subreddit>",
    ],
        "examples": "{tr}listporn 10 nsfw_gifs",
        "options":horny,
    },
)
async def cat(event):
    """Send a list of porn"""
    reply_to = await reply_id(event)
    intxt = event.pattern_match.group(1)
    if intxt and " " in intxt:
        count,sub_r = intxt.split(" ")
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
    title = []
    postlink = []
    media_url = []
    for x in r["memes"]: postlink.append(x["postLink"])
    for x in r["memes"]: title.append(x["title"])
    for x in r["memes"]: media_url.append(x["url"])
    i=0
    pwnlist = f"<b>{count} results for {sub_r} :</b>\n\n"
    for m,p,t in zip(media_url,postlink,title):
        if "https://i.imgur.com" in m:
            media_url = m.replace(".gifv",".mp4")
        else:
            try:
                source = requests.get(m)
                soup = BeautifulSoup(source.text, "lxml")
                links = [itm['content'] for itm in soup.findAll("meta", property = "og:video")]
                try: media_url = links[1]
                except: media_url = links[0]
            except: media_url = m
        pwnlist+= f"<b><i>{i+1}. <a href = {p}>{t}</a></i> : [<a href = {media_url}>Download</a>]</b>\n"
        i+=1
    await edit_or_reply(event,pwnlist,parse_mode="html")
