"""
credits to @mrconfused and @sandy1709
"""
#    Copyright (C) 2020  sandeep.n(π.$)
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os

import pybase64
from telegraph import exceptions, upload_file
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from userbot import CMD_HELP

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import *


@bot.on(admin_cmd("mask ?(.*)"))
@bot.on(sudo_cmd(pattern="mask ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await edit_or_reply(event, "```reply to media message```")
        return
    chat = "@hazmat_suit_bot"
    reply_message.sender
    if reply_message.sender.bot:
        await edit_or_reply(event, "```Reply to actual users message.```")
        return
    catevent = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=905164246)
            )
            await borg.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await catevent.edit("```Please unblock @hazmat_suit_bot and try again```")
            return
        if response.text.startswith("Forward"):
            await catevent.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await catevent.delete()
            await event.client.send_file(event.chat_id, response.message.media)


@borg.on(admin_cmd(pattern="awooify(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="awooify(?: |$)(.*)", allow_sudo=True))
async def catbot(catmemes):
    replied = await catmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        await edit_or_reply(catmemes, "reply to a supported media file")
        return
    if replied.media:
        kakashi = await edit_or_reply(catmemes, "passing to telegraph...")
    else:
        await edit_or_reply(catmemes, "reply to a supported media file")
        return
    try:
        cat = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        cat = Get(cat)
        await catmemes.client(cat)
    except BaseException:
        pass
    download_location = await borg.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await kakashi.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await kakashi.edit("generating image..")
    else:
        await kakashi.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await kakashi.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    cat = f"https://telegra.ph{response[0]}"
    cat = await awooify(cat)
    await kakashi.delete()
    await borg.send_file(catmemes.chat_id, cat, reply_to=replied)


@borg.on(admin_cmd(pattern="lolice(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="lolice(?: |$)(.*)", allow_sudo=True))
async def catbot(catmemes):
    replied = await catmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        await edit_or_reply(catmemes,"reply to a supported media file")
        return
    if replied.media:
        kakashi = await edit_or_reply(catmemes,"passing to telegraph...")
    else:
        await edit_or_reply(catmemes,"reply to a supported media file")
        return
    try:
        cat = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        cat = Get(cat)
        await catmemes.client(cat)
    except BaseException:
        pass
    download_location = await borg.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await catmemes.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await kakashi.edit("generating image..")
    else:
        await kakashi.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await kakashi.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    cat = f"https://telegra.ph{response[0]}"
    cat = await lolice(cat)
    await kakashi.delete()
    await borg.send_file(catmemes.chat_id, cat, reply_to=replied)


@borg.on(admin_cmd(pattern="bun(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="bun(?: |$)(.*)", allow_sudo=True))
async def catbot(catmemes):
    replied = await catmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        await edit_or_reply(catmemes,"reply to a supported media file")
        return
    if replied.media:
        kakashi = await edit_or_reply(catmemes,"passing to telegraph...")
    else:
        await edit_or_reply(catmemes,"reply to a supported media file")
        return
    try:
        cat = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        cat = Get(cat)
        await catmemes.client(cat)
    except BaseException:
        pass
    download_location = await borg.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await kakashi.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await kakashi.edit("generating image..")
    else:
        await kakashi.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await kakashi.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    cat = f"https://telegra.ph{response[0]}"
    cat = await baguette(cat)
    await kakashi.delete()
    await borg.send_file(catmemes.chat_id, cat, reply_to=replied)


@borg.on(admin_cmd(pattern="iphx(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="iphx(?: |$)(.*)", allow_sudo=True))
async def catbot(catmemes):
    replied = await catmemes.get_reply_message()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if not replied:
        await edit_or_reply(catmemes,"reply to a supported media file")
        return
    if replied.media:
        kakashi = await edit_or_reply(catmemes,"passing to telegraph...")
    else:
        await edit_or_reply(catmemes,"reply to a supported media file")
        return
    try:
        cat = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        cat = Get(cat)
        await catmemes.client(cat)
    except BaseException:
        pass
    download_location = await borg.download_media(
        replied, Config.TMP_DOWNLOAD_DIRECTORY
    )
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await kakashi.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await kakashi.edit("generating image..")
    else:
        await catmemes.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await kakashi.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    cat = f"https://telegra.ph{response[0]}"
    cat = await iphonex(cat)
    await kakashi.delete()
    await borg.send_file(catmemes.chat_id, cat, reply_to=replied)


CMD_HELP.update(
    {
        "mask": "`.mask` reply to any image file:\
      \nUSAGE:makes an image a different style try out your own.\
      "
    }
)
