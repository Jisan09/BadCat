import os

import pygments
import requests
from pygments.formatters import ImageFormatter
from pygments.lexers import Python3Lexer
from requests import exceptions, get
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import catub

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.tools import media_type
from ..helpers.utils import _format, reply_id

plugin_category = "utils"


def progress(current, total):
    logger.info(
        "Downloaded {} of {}\nCompleted {}".format(
            current, total, (current / total) * 100
        )
    )


@catub.cat_cmd(
    pattern="paste(?: |$)(.*)",
    command=("paste", plugin_category),
    info={
        "header": "To paste text to a paste bin.",
        "description": "Create a paste or a shortened url using dogbin https://del.dog/",
        "usage": ["{tr}paste <reply>", "{tr}paste text"],
    },
)
async def _(event):
    "To paste text to a paste bin."
    catevent = await edit_or_reply(event, "`pasting to del dog.....`")
    input_str = "".join(event.text.split(maxsplit=1)[1:])
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
    if r["isUrl"]:
        nurl = f"https://del.dog/v/{r['key']}"
        rawurl = f"https://del.dog/raw/{r['key']}"
        await catevent.edit(
            f"**Pasted to dogbin : **[dog]({nurl}).\n**Raw url :** [raw link]({rawurl})\n**GoTo Original URL: **[link]({url})"
        )
    else:
        await catevent.edit(
            f"**Pasted to dogbin : **[dog]({url})\n**Raw url :** [raw link](https://del.dog/raw/{r['key']})"
        )


@catub.cat_cmd(
    pattern="neko(?: |$)(.*)",
    command=("neko", plugin_category),
    info={
        "header": "To paste text to a paste bin.",
        "description": "Create a paste or a shortened url using dogbin https://nekobin.com",
        "usage": ["{tr}neko <reply>", "{tr}neko text"],
    },
)
async def _(event):
    "To paste text to a paste bin."
    catevent = await edit_or_reply(event, "`pasting to neko bin.....`")
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    if input_str:
        message = input_str
        downloaded_file_name = None
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
                message = (
                    "**Usage : **`.neko <long text to include/reply to text file>`"
                )
            os.remove(downloaded_file_name)
        else:
            downloaded_file_name = None
            message = previous_message.message
    else:
        downloaded_file_name = None
        message = "**Usage : **`.neko <long text to include/reply to text file>`"
    if downloaded_file_name and downloaded_file_name.endswith(".py"):
        py_file = ".py"
        data = message
        key = (
            requests.post("https://nekobin.com/api/documents", json={"content": data})
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}{py_file}"
    else:
        data = message
        key = (
            requests.post("https://nekobin.com/api/documents", json={"content": data})
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}"
    reply_text = f"**Pasted to Nekobin : **[neko]({url})\n**Raw url : **[Raw](https://nekobin.com/raw/{key})"
    await catevent.edit(reply_text)


@catub.cat_cmd(
    pattern="iffuci(?: |$)(.*)",
    command=("iffuci", plugin_category),
    info={
        "header": "To paste text to a paste bin.",
        "description": "Create a paste or a shortened url using dogbin https://www.iffuci.tk",
        "usage": ["{tr}iffuci <reply>", "{tr}iffuci text"],
    },
)
async def _(event):
    "To paste text to a paste bin."
    catevent = await edit_or_reply(event, "`pasting to del dog.....`")
    input_str = "".join(event.text.split(maxsplit=1)[1:])
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
    url = "https://www.iffuci.tk/documents"
    r = requests.post(url, data=message.encode("UTF-8")).json()
    url = f"https://iffuci.tk/{r['key']}"
    if r["isUrl"]:
        nurl = f"https://iffuci.tk/v/{r['key']}"
        await catevent.edit(
            "code is pasted to {}. GoTo Original URL: {}".format(nurl, url)
        )
    else:
        await catevent.edit("code is pasted to {}".format(url))


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
    catevent = await edit_or_reply(event, "`printing the text on blank page`")
    input_str = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    text_to_print = ""
    if reply:
        mediatype = media_type(reply)
        if mediatype == "Document":
            d_file_name = await event.client.download_media(reply, "./temp/")
            f = open(d_file_name, "r")
            text_to_print = f.read()
    if text_to_print == "":
        if input_str:
            text_to_print = input_str
        elif event.reply_to_msg_id:
            text_to_print = reply.message
        else:
            await edit_delete(
                catevent,
                "`Either reply to document or reply to text message or give text along with command`",
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
    except Exception as e:
        await edit_delete(catevent, str(e), parse_mode=_format.parse_pre)
    await catevent.delete()
    os.remove("out.png")
    if d_file_name is not None:
        os.remove(d_file_name)


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
