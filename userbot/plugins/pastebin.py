import os
import re

import pygments
import requests
from pygments.formatters import ImageFormatter
from pygments.lexers import Python3Lexer
from requests import exceptions, get
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.utils import get_extension

from userbot import catub

from ..Config import Config
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.tools import media_type
from ..helpers.utils import pastetext, reply_id

plugin_category = "utils"

LOGS = logging.getLogger(__name__)

pastebins = {
    "Pasty": "p",
    "Neko": "n",
    "Spacebin": "s",
    "Dog": "d",
}


def get_key(val):
    for key, value in pastebins.items():
        if val == value:
            return key


@catub.cat_cmd(
    pattern="pcode(?: |$)(.*)",
    command=("pcode", plugin_category),
    info={
        "header": "Will paste the entire text on the blank page and will send as image",
        "usage": ["{tr}pcode <reply>", "{tr}paste text"],
    },
)
async def _(event):
    "To paste text to image."
    reply_to = await reply_id(event)
    d_file_name = None
    catevent = await edit_or_reply(event, "`Pasting the text on blank page`")
    input_str = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    text_to_print = ""
    if input_str:
        text_to_print = input_str
    if text_to_print == "" and reply.media:
        mediatype = media_type(reply)
        if mediatype == "Document":
            d_file_name = await event.client.download_media(reply, Config.TEMP_DIR)
            with open(d_file_name, "r") as f:
                text_to_print = f.read()
    if text_to_print == "":
        if reply.text:
            text_to_print = reply.raw_text
        else:
            return await edit_delete(
                catevent,
                "`Either reply to text/code file or reply to text message or give text along with command`",
            )
    pygments.highlight(
        text_to_print,
        Python3Lexer(),
        ImageFormatter(font_name="DejaVu Sans Mono", line_numbers=True),
        "out.png",
    )
    try:
        await event.client.send_file(
            event.chat_id, "out.png", force_document=False, reply_to=reply_to
        )
        await catevent.delete()
        os.remove("out.png")
        if d_file_name is not None:
            os.remove(d_file_name)
    except Exception as e:
        await edit_delete(catevent, f"**Error:**\n`{str(e)}`", time=10)


@catub.cat_cmd(
    pattern="(d|p|s|n)?(paste|neko)(?:\s|$)([\S\s]*)",
    command=("paste", plugin_category),
    info={
        "header": "To paste text to a paste bin.",
        "description": "Uploads the given text to website so that you can share text/code with others easily. If no flag is used then it will use p as default",
        "flags": {
            "d": "Will paste text to dog.bin",
            "p": "Will paste text to pasty.lus.pm",
            "s": "Will paste text to spaceb.in (language extension not there at present.)",
        },
        "usage": [
            "{tr}{flags}paste <reply/text>",
            "{tr}{flags}paste {extension} <reply/text>",
        ],
        "examples": [
            "{tr}spaste <reply/text>",
            "{tr}ppaste -py await event.client.send_message(chat,'Hello! testing123 123')",
        ],
    },
)
async def _(event):
    "To paste text to a paste bin."
    catevent = await edit_or_reply(event, "`pasting text to paste bin....`")
    input_str = event.pattern_match.group(3)
    reply = await event.get_reply_message()
    ext = re.findall(r"-\w+", input_str)
    try:
        extension = ext[0].replace("-", "")
        input_str = input_str.replace(ext[0], "").strip()
    except IndexError:
        extension = None
    if event.pattern_match.group(2) == "neko":
        pastetype = "n"
    else:
        pastetype = event.pattern_match.group(1) or "p"
    text_to_print = ""
    if input_str:
        text_to_print = input_str
    if text_to_print == "" and reply.media:
        mediatype = media_type(reply)
        if mediatype == "Document":
            d_file_name = await event.client.download_media(reply, Config.TEMP_DIR)
            if extension is None:
                extension = get_extension(reply.document)
            with open(d_file_name, "r") as f:
                text_to_print = f.read()
    if text_to_print == "":
        if reply.text:
            text_to_print = reply.raw_text
        else:
            return await edit_delete(
                catevent,
                "`Either reply to text/code file or reply to text message or give text along with command`",
            )
    if extension.startswith("."):
        extension = extension[1:]
    try:
        response = await pastetext(text_to_print, pastetype, extension)
        if "error" in response:
            return await edit_delete(
                catevent,
                f"**Error while pasting text:**\n`Unable to process your request may be pastebins are down.`",
            )
        result = ""
        if pastebins[response["bin"]] != pastetype:
            result += f"<b>{get_key(pastetype)} is down, So </b>"
        result += f"<b>Pasted to: <a href={response['url']}>{response['bin']}</a></b>"
        if response["raw"] != "":
            result += f"\n<b>Raw link: <a href={response['raw']}>Raw</a></b>"
        await catevent.edit(result, link_preview=False, parse_mode="html")
    except Exception as e:
        await edit_delete(catevent, f"**Error while pasting text:**\n`{str(e)}`")


@catub.cat_cmd(
    command=("neko", plugin_category),
    info={
        "header": "To paste text to a neko bin.",
        "description": "Uploads the given text to nekobin so that you can share text/code with others easily.",
        "usage": ["{tr}neko <reply/text>", "{tr}neko {extension} <reply/text>"],
        "examples": [
            "{tr}neko <reply/text>",
            "{tr}neko -py await event.client.send_message(chat,'Hello! testing123 123')",
        ],
    },
)
async def _(event):
    "To paste text to a neko bin."
    # just to show in help menu as seperate


@catub.cat_cmd(
    pattern="getpaste(?: |$)(.*)",
    command=("getpaste", plugin_category),
    info={
        "header": "To paste text into telegram from del dog link.",
        "description": "Gets the content of a paste or shortened url from dogbin https://del.dog/",
        "usage": ["{tr}getpaste <del dog link>"],
    },
)
async def get_dogbin_content(dog_url):
    "To paste text into telegram from del dog link."
    textx = await dog_url.get_reply_message()
    message = dog_url.pattern_match.group(1)
    catevent = await edit_or_reply(dog_url, "`Getting dogbin content...`")
    if not message and textx:
        message = str(textx.message)
    format_normal = "https://del.dog/"
    format_view = "https://del.dog/v/"

    if message.startswith(format_view):
        message = message[len(format_view) :]
    elif message.startswith(format_normal):
        message = message[len(format_normal) :]
    elif message.startswith("del.dog/"):
        message = message[len("del.dog/") :]
    else:
        await catevent.edit("`Is that even a dogbin url?`")
        return
    resp = get(f"https://del.dog/raw/{message}")
    try:
        resp.raise_for_status()
    except exceptions.HTTPError as HTTPErr:
        await catevent.edit(
            "Request returned an unsuccessful status code.\n\n" + str(HTTPErr)
        )
        return
    except exceptions.Timeout as TimeoutErr:
        await catevent.edit("Request timed out." + str(TimeoutErr))
        return
    except exceptions.TooManyRedirects as RedirectsErr:
        await catevent.edit(
            "Request exceeded the configured number of maximum redirections."
            + str(RedirectsErr)
        )
        return
    reply_text = (
        "`Fetched dogbin URL content successfully!`\n\n`Content:` \n" + resp.text
    )
    await edit_or_reply(catevent, reply_text)


@catub.cat_cmd(
    pattern="paster(?: |$)(.*)",
    command=("paster", plugin_category),
    info={
        "header": "Create a instant view or a paste it in telegraph file.",
        "usage": ["{tr}paster <reply>", "{tr}paster text"],
    },
)
async def _(event):
    "Create a instant view or a paste it in telegraph file."
    catevent = await edit_or_reply(event, "`pasting to del dog.....`")
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    previous_message = None
    if input_str:
        message = input_str
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.media:
            downloaded_file_name = await event.client.download_media(
                previous_message,
                Config.TEMP_DIR,
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            message = ""
            try:
                for m in m_list:
                    message += m.decode("UTF-8")
            except Exception:
                message = "Usage : .paste <long text to include/reply to text file>"
            os.remove(downloaded_file_name)
        else:
            message = previous_message.message
    else:
        message = "Usage : .paste <long text to include/reply to text file>"
    url = "https://del.dog/documents"
    r = requests.post(url, data=message.encode("UTF-8")).json()
    url = f"https://del.dog/{r['key']}"
    chat = "@chotamreaderbot"
    # This module is modded by @ViperAdnan #KeepCredit
    await catevent.edit("**Making instant view...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=272572121)
            )
            await event.client.send_message(chat, url)
            response = await response
        except YouBlockedUserError:
            await catevent.edit("```Please unblock me (@chotamreaderbot) u Nigga```")
            return
        await catevent.delete()
        await event.client.send_message(
            event.chat_id, response.message, reply_to=previous_message
        )
