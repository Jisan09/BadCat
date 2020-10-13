# Originally from Bothub
# Port to UserBot by @heyworld
# Copyright (C) 2020 azrim.

import asyncio

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP, bot

from ..utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd(outgoing=True, pattern="spd(?: |$)(.*)"))
@bot.on(sudo_cmd(outgoing=True, pattern="spd(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    chat = "@SpotifyMusicDownloaderBot"
    catevent = await edit_or_reply(event, "`wi8..! I am finding your song....`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=752979930)
            )
            await event.client.send_message(chat, input_str)
            respond = await response
        except YouBlockedUserError:
            await catevent.edit("` unblock` @SpotifyMusicDownloaderBot `and try again`")
            return
        await event.delete()
        await event.client.forward_messages(event.chat_id, respond.message)
        await event.client.send_read_acknowledge(conv.chat_id)


@bot.on(admin_cmd(outgoing=True, pattern="netease(?: |$)(.*)"))
@bot.on(sudo_cmd(outgoing=True, pattern="netease(?: |$)(.*)", allow_sudo=True))
async def kakashi(event):
    if event.fwd_from:
        return
    song = event.pattern_match.group(1)
    chat = "@WooMaiBot"
    link = f"/netease {song}"
    catevent = await edit_or_reply(event, "`wi8..! I am finding your song....`")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(link)
            await conv.get_response()
            respond = await conv.get_response()
        except YouBlockedUserError:
            await catevent.edit("```Please unblock @WooMaiBot and try again```")
            return
        await catevent.edit("`Sending Your Music...`")
        await asyncio.sleep(3)
        await event.delete()
        await bot.send_file(event.chat_id, respond)
        await event.client.delete_messages(
            conv.chat_id, [msg.id, response.id, respond.id]
        )
        await event.client.send_read_acknowledge(conv.chat_id)


CMD_HELP.update(
    {
        "music": "__**PLUGIN NAME :** Music__\
            \n\n📌** CMD ➥** `.spd` <Artist - Song Title>\
            \n**USAGE   ➥  **For searching songs from Spotify.\
            \n\n📌** CMD ➥** `.netease` <Artist - Song Title>\
            \n**USAGE   ➥  **Download music with @WooMaiBot\
            \n\n📌** CMD ➥** `.dzd` <Spotify/Deezer Link>\
            \n**USAGE   ➥  **Download music from Spotify or Deezer."
    }
)
