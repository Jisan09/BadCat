# Userbot module containing various scrapers.
# Copyright (C) 2019 The Raphielscape Company LLC.(some are ported from there)
# Copyright (c) JeepBot | 2019(for imdb)
# # kanged from Blank-x ;---;

import os
import re

import bs4
import requests
from googletrans import LANGUAGES, Translator
from wikipedia import summary
from wikipedia.exceptions import DisambiguationError, PageError

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import BOTLOG, BOTLOG_CHATID, deEmojify

TTS_LANG = "en"
TRT_LANG = "en"
langi = "en"


@bot.on(admin_cmd(outgoing=True, pattern=r"wiki (.*)"))
@bot.on(sudo_cmd(allow_sudo=True, pattern=r"wiki (.*)"))
async def wiki(wiki_q):
    """ For .wiki command, fetch content from Wikipedia. """
    match = wiki_q.pattern_match.group(1)
    try:
        summary(match)
    except DisambiguationError as error:
        await edit_or_reply(wiki_q, f"Disambiguated page found.\n\n{error}")
        return
    except PageError as pageerror:
        await edit_or_reply(wiki_q, f"Page not found.\n\n{pageerror}")
        return
    result = summary(match)
    if len(result) >= 4096:
        with open("output.txt", "w+") as file:
            file.write(result)
        await wiki_q.client.send_file(
            wiki_q.chat_id,
            "output.txt",
            reply_to=wiki_q.id,
            caption="`Output too large, sending as file`",
        )
        await wiki_q.delete()
        if os.path.exists("output.txt"):
            os.remove("output.txt")
        return
    await edit_or_reply(
        wiki_q, "**Search:**\n`" + match + "`\n\n**Result:**\n" + result
    )
    if BOTLOG:
        await wiki_q.client.send_message(
            BOTLOG_CHATID, f"Wiki query `{match}` was executed successfully"
        )


@bot.on(admin_cmd(pattern="imdb (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="imdb (.*)", allow_sudo=True))
async def imdb(e):
    catevent = await edit_or_reply(e, "`searching........")
    try:
        movie_name = e.pattern_match.group(1)
        remove_space = movie_name.split(" ")
        final_name = "+".join(remove_space)
        page = requests.get(
            "https://www.imdb.com/find?ref_=nv_sr_fn&q=" + final_name + "&s=all"
        )
        str(page.status_code)
        soup = bs4.BeautifulSoup(page.content, "lxml")
        odds = soup.findAll("tr", "odd")
        mov_title = odds[0].findNext("td").findNext("td").text
        mov_link = (
            "http://www.imdb.com/" + odds[0].findNext("td").findNext("td").a["href"]
        )
        page1 = requests.get(mov_link)
        soup = bs4.BeautifulSoup(page1.content, "lxml")
        if soup.find("div", "poster"):
            poster = soup.find("div", "poster").img["src"]
        else:
            poster = ""
        if soup.find("div", "title_wrapper"):
            pg = soup.find("div", "title_wrapper").findNext("div").text
            mov_details = re.sub(r"\s+", " ", pg)
        else:
            mov_details = ""
        credits = soup.findAll("div", "credit_summary_item")
        director = credits[0].a.text
        if len(credits) == 1:
            writer = "Not available"
            stars = "Not available"
        elif len(credits) > 2:
            writer = credits[1].a.text
            actors = [x.text for x in credits[2].findAll("a")]
            actors.pop()
            stars = actors[0] + "," + actors[1] + "," + actors[2]
        else:
            writer = "Not available"
            actors = [x.text for x in credits[1].findAll("a")]
            actors.pop()
            stars = actors[0] + "," + actors[1] + "," + actors[2]
        if soup.find("div", "inline canwrap"):
            story_line = soup.find("div", "inline canwrap").findAll("p")[0].text
        else:
            story_line = "Not available"
        info = soup.findAll("div", "txt-block")
        if info:
            mov_country = []
            mov_language = []
            for node in info:
                a = node.findAll("a")
                for i in a:
                    if "country_of_origin" in i["href"]:
                        mov_country.append(i.text)
                    elif "primary_language" in i["href"]:
                        mov_language.append(i.text)
        if soup.findAll("div", "ratingValue"):
            for r in soup.findAll("div", "ratingValue"):
                mov_rating = r.strong["title"]
        else:
            mov_rating = "Not available"
        await catevent.edit(
            "<a href=" + poster + ">&#8203;</a>"
            "<b>Title : </b><code>"
            + mov_title
            + "</code>\n<code>"
            + mov_details
            + "</code>\n<b>Rating : </b><code>"
            + mov_rating
            + "</code>\n<b>Country : </b><code>"
            + mov_country[0]
            + "</code>\n<b>Language : </b><code>"
            + mov_language[0]
            + "</code>\n<b>Director : </b><code>"
            + director
            + "</code>\n<b>Writer : </b><code>"
            + writer
            + "</code>\n<b>Stars : </b><code>"
            + stars
            + "</code>\n<b>IMDB Url : </b>"
            + mov_link
            + "\n<b>Story Line : </b>"
            + story_line,
            link_preview=True,
            parse_mode="HTML",
        )
    except IndexError:
        await catevent.edit("Plox enter **Valid movie name** kthx")


@bot.on(admin_cmd(outgoing=True, pattern=r"trt(?: |$)([\s\S]*)"))
@bot.on(sudo_cmd(allow_sudo=True, pattern=r"trt(?: |$)([\s\S]*)"))
async def translateme(trans):
    """ For .trt command, translate the given text using Google Translate. """
    translator = Translator()
    textx = await trans.get_reply_message()
    message = trans.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await edit_or_reply(trans, "`Give a text or reply to a message to translate!`")
        return
    try:
        reply_text = translator.translate(deEmojify(message), dest=TRT_LANG)
    except ValueError:
        await edit_or_reply(trans, "Invalid destination language.")
        return
    source_lan = LANGUAGES[f"{reply_text.src.lower()}"]
    transl_lan = LANGUAGES[f"{reply_text.dest.lower()}"]
    reply_text = f"**From** __{source_lan.title()}__\n**To **__{transl_lan.title()}__**:**\n\n`{reply_text.text}``"

    await edit_or_reply(trans, reply_text)
    if BOTLOG:
        await trans.client.send_message(
            BOTLOG_CHATID,
            f"Translated some {source_lan.title()} stuff to {transl_lan.title()} just now.",
        )


@bot.on(admin_cmd(pattern="lang trt (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="lang trt (.*)", allow_sudo=True))
async def lang(value):
    # For .lang command, change the default langauge of userbot scrapers.
    scraper = "Translator"
    global TRT_LANG
    arg = value.pattern_match.group(1).lower()
    if arg in LANGUAGES:
        TRT_LANG = arg
        LANG = LANGUAGES[arg]
    else:
        await edit_or_reply(
            value,
            f"`Invalid Language code !!`\n`Available language codes for TRT`:\n\n`{LANGUAGES}`",
        )
        return
    await edit_or_reply(value, f"`Language for {scraper} changed to {LANG.title()}.`")
    if BOTLOG:
        await value.client.send_message(
            BOTLOG_CHATID, f"`Language for {scraper} changed to {LANG.title()}.`"
        )
