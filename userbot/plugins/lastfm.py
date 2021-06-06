# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.from asyncio import sleep
from asyncio import sleep
from os import environ
from re import sub
from sys import setrecursionlimit
from urllib import parse

from pylast import LastFMNetwork, User, WSError, md5
from telethon.errors import AboutTooLongError
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.users import GetFullUserRequest

from userbot import catub

from ..Config import Config
from ..core.logger import logging
from ..helpers.functions import deEmojify, hide_inlinebot
from ..helpers.utils import reply_id
from . import BOTLOG, BOTLOG_CHATID, DEFAULT_BIO

LOGS = logging.getLogger(__name__)
plugin_category = "extra"


BIO_PREFIX = Config.BIO_PREFIX
LASTFM_API = Config.LASTFM_API
LASTFM_SECRET = Config.LASTFM_SECRET
LASTFM_USERNAME = Config.LASTFM_USERNAME
LASTFM_PASSWORD_PLAIN = Config.LASTFM_PASSWORD_PLAIN

LASTFM_PASS = md5(LASTFM_PASSWORD_PLAIN)
if LASTFM_API and LASTFM_SECRET and LASTFM_USERNAME and LASTFM_PASS:
    lastfm = LastFMNetwork(
        api_key=LASTFM_API,
        api_secret=LASTFM_SECRET,
        username=LASTFM_USERNAME,
        password_hash=LASTFM_PASS,
    )
else:
    lastfm = None

# =================== CONSTANT ===================
LFM_BIO_ENABLED = "```last.fm current music to bio is now enabled.```"
LFM_BIO_DISABLED = (
    "```last.fm current music to bio is now disabled. Bio reverted to default.```"
)
LFM_BIO_RUNNING = "```last.fm current music to bio is already running.```"
LFM_BIO_ERR = "```No option specified.```"
LFM_LOG_ENABLED = "```last.fm logging to bot log is now enabled.```"
LFM_LOG_DISABLED = "```last.fm logging to bot log is now disabled.```"
LFM_LOG_ERR = "```No option specified.```"
ERROR_MSG = "```last.fm module halted, got an unexpected error.```"
# ================================================


class LASTFM:
    def __init__(self):
        self.ARTIST = 0
        self.SONG = 0
        self.USER_ID = 0
        self.LASTFMCHECK = False
        self.RUNNING = False
        self.LastLog = False


LASTFM_ = LASTFM()


async def gettags(track=None, isNowPlaying=None, playing=None):
    if isNowPlaying:
        tags = playing.get_top_tags()
        arg = playing
        if not tags:
            tags = playing.artist.get_top_tags()
    else:
        tags = track.track.get_top_tags()
        arg = track.track
    if not tags:
        tags = arg.artist.get_top_tags()
    tags = "".join(" #" + t.item.__str__() for t in tags[:5])
    tags = sub("^ ", "", tags)
    tags = sub(" ", "_", tags)
    tags = sub("_#", " #", tags)
    return tags


async def artist_and_song(track):
    return f"{track.track}"


async def get_curr_track(lfmbio):  # sourcery no-metrics
    oldartist = ""
    oldsong = ""
    while LASTFM_.LASTFMCHECK:
        try:
            if LASTFM_.USER_ID == 0:
                LASTFM_.USER_ID = (await lfmbio.client.get_me()).id
            user_info = await catub(GetFullUserRequest(LASTFM_.USER_ID))
            LASTFM_.RUNNING = True
            playing = User(LASTFM_USERNAME, lastfm).get_now_playing()
            LASTFM_.SONG = playing.get_title()
            LASTFM_.ARTIST = playing.get_artist()
            oldsong = environ.get("oldsong", None)
            oldartist = environ.get("oldartist", None)
            if (
                playing is not None
                and LASTFM_.SONG != oldsong
                and LASTFM_.ARTIST != oldartist
            ):
                environ["oldsong"] = str(LASTFM_.SONG)
                environ["oldartist"] = str(LASTFM_.ARTIST)
                if BIO_PREFIX:
                    lfmbio = f"{BIO_PREFIX} 🎧: {LASTFM_.ARTIST} - {LASTFM_.SONG}"
                else:
                    lfmbio = f"🎧: {LASTFM_.ARTIST} - {LASTFM_.SONG}"
                try:
                    if BOTLOG and LASTFM_.LastLog:
                        await catub.send_message(
                            BOTLOG_CHATID, f"Attempted to change bio to\n{lfmbio}"
                        )
                    await catub(UpdateProfileRequest(about=lfmbio))
                except AboutTooLongError:
                    short_bio = f"🎧: {LASTFM_.SONG}"
                    await catub(UpdateProfileRequest(about=short_bio))
            if playing is None and user_info.about != DEFAULT_BIO:
                await sleep(6)
                await catub(UpdateProfileRequest(about=DEFAULT_BIO))
                if BOTLOG and LASTFM_.LastLog:
                    await catub.send_message(
                        BOTLOG_CHATID, f"Reset bio back to\n{DEFAULT_BIO}"
                    )
        except AttributeError:
            try:
                if user_info.about != DEFAULT_BIO:
                    await sleep(6)
                    await catub(UpdateProfileRequest(about=DEFAULT_BIO))
                    if BOTLOG and LASTFM_.LastLog:
                        await catub.send_message(
                            BOTLOG_CHATID, f"Reset bio back to\n{DEFAULT_BIO}"
                        )
            except FloodWaitError as err:
                if BOTLOG and LASTFM_.LastLog:
                    await catub.send_message(
                        BOTLOG_CHATID, f"Error changing bio:\n{err}"
                    )
        except FloodWaitError as err:
            if BOTLOG and LASTFM_.LastLog:
                await catub.send_message(BOTLOG_CHATID, f"Error changing bio:\n{err}")
        except WSError as err:
            if BOTLOG and LASTFM_.LastLog:
                await catub.send_message(BOTLOG_CHATID, f"Error changing bio:\n{err}")
        await sleep(2)
    LASTFM_.RUNNING = False


@catub.cat_cmd(
    pattern="lastfm$",
    command=("lastfm", plugin_category),
    info={
        "header": "To fetch scrobble data from last.fm",
        "description": "Shows currently scrobbling track or most recent scrobbles if nothing is playing.",
        "usage": "{tr}lastfm",
    },
)
async def last_fm(lastFM):
    ".lastfm command, fetch scrobble data from last.fm."
    await lastFM.edit("Processing...")
    preview = None
    playing = User(LASTFM_USERNAME, lastfm).get_now_playing()
    username = f"https://www.last.fm/user/{LASTFM_USERNAME}"
    if playing is not None:
        try:
            image = User(LASTFM_USERNAME, lastfm).get_now_playing().get_cover_image()
        except IndexError:
            image = None
        tags = await gettags(isNowPlaying=True, playing=playing)
        rectrack = parse.quote(f"{playing}")
        rectrack = sub("^", "https://open.spotify.com/search/", rectrack)
        if image:
            output = f"[‎]({image})[{LASTFM_USERNAME}]({username}) __is now listening to:__\n\n• [{playing}]({rectrack})\n"
            preview = True
        else:
            output = f"[{LASTFM_USERNAME}]({username}) __is now listening to:__\n\n• [{playing}]({rectrack})\n"
    else:
        recent = User(LASTFM_USERNAME, lastfm).get_recent_tracks(limit=3)
        playing = User(LASTFM_USERNAME, lastfm).get_now_playing()
        output = f"[{LASTFM_USERNAME}]({username}) __was last listening to:__\n\n"
        for i, track in enumerate(recent):
            LOGS.info(i)
            printable = await artist_and_song(track)
            tags = await gettags(track)
            rectrack = parse.quote(str(printable))
            rectrack = sub("^", "https://open.spotify.com/search/", rectrack)
            output += f"• [{printable}]({rectrack})\n"
            if tags:
                output += f"`{tags}`\n\n"
    if preview is not None:
        await lastFM.edit(f"{output}", parse_mode="md", link_preview=True)
    else:
        await lastFM.edit(f"{output}", parse_mode="md")


@catub.cat_cmd(
    pattern="now$",
    command=("now", plugin_category),
    info={
        "header": "Send your current listening song from Lastfm/Spotify/Deezer.",
        "usage": "{tr}now",
        "note": "For working of this command, you need to authorize @NowPlayBot.",
    },
)
async def now(event):
    "Send your current listening song."
    text = " "
    reply_to_id = await reply_id(event)
    bot_name = "@nowplaybot"
    text = deEmojify(text)
    await event.delete()
    await hide_inlinebot(event.client, bot_name, text, event.chat_id, reply_to_id)


@catub.cat_cmd(
    pattern="inow$",
    command=("inow", plugin_category),
    info={
        "header": "Show your current listening song in the form of a cool image.",
        "usage": "{tr}inow",
        "note": "For working of this command, you need to authorize @SpotiPieBot.",
    },
)
async def nowimg(event):
    "Show your current listening song."
    text = " "
    reply_to_id = await reply_id(event)
    bot_name = "@Spotipiebot"
    text = deEmojify(text)
    await event.delete()
    await hide_inlinebot(event.client, bot_name, text, event.chat_id, reply_to_id)


@catub.cat_cmd(
    pattern="lastbio (on|off)",
    command=("lastbio", plugin_category),
    info={
        "header": "To Enable or Disable the last.fm current playing to bio",
        "usage": [
            "{tr}lastbio on",
            "{tr}lastbio off",
        ],
    },
)
async def lastbio(lfmbio):
    "To Enable or Disable the last.fm current playing to bio"
    arg = lfmbio.pattern_match.group(1).lower()
    if arg == "on":
        setrecursionlimit(700000)
        if not LASTFM_.LASTFMCHECK:
            LASTFM_.LASTFMCHECK = True
            environ["errorcheck"] = "0"
            await lfmbio.edit(LFM_BIO_ENABLED)
            await sleep(4)
            await get_curr_track(lfmbio)
        else:
            await lfmbio.edit(LFM_BIO_RUNNING)
    elif arg == "off":
        LASTFM_.LASTFMCHECK = False
        LASTFM_.RUNNING = False
        await lfmbio.client(UpdateProfileRequest(about=DEFAULT_BIO))
        await lfmbio.edit(LFM_BIO_DISABLED)
    else:
        await lfmbio.edit(LFM_BIO_ERR)


@catub.cat_cmd(
    pattern="lastlog (on|off)",
    command=("lastlog", plugin_category),
    info={
        "header": "To Enable or Disable the last.fm current playing to bot log group",
        "usage": [
            "{tr}lastlog on",
            "{tr}lastlog off",
        ],
    },
)
async def lastlog(lstlog):
    "To Enable or Disable the last.fm current playing to bot log group"
    arg = lstlog.pattern_match.group(1).lower()
    LASTFM_.LastLog = False
    if arg == "on":
        LASTFM_.LastLog = True
        await lstlog.edit(LFM_LOG_ENABLED)
    elif arg == "off":
        LASTFM_.LastLog = False
        await lstlog.edit(LFM_LOG_DISABLED)
    else:
        await lstlog.edit(LFM_LOG_ERR)
