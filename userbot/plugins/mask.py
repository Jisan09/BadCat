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
        await edit_or_reply(event,"```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await edit_or_reply(event,"```reply to media message```")
        return
    chat = "@hazmat_suit_bot"
    reply_message.sender
    if reply_message.sender.bot:
        await edit_or_reply(event,"```Reply to actual users message.```")
        return
    catevent = await edit_or_reply(event,"```Processing```")
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


CMD_HELP.update(
    {
        "mask": "`.mask` reply to any image file:\
      \nUSAGE:makes an image a different style try out your own.\
      "
    }
)
