import asyncio

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP

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
        await catevent.delete()
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
            msg = await conv.send_message(link)
            response = await conv.get_response()
            respond = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("```Please unblock @WooMaiBot and try again```")
            return
        await catevent.edit("`Sending Your Music...`")
        await asyncio.sleep(3)
        await catevent.delete()
        await event.client.send_file(event.chat_id, respond)
    await event.client.delete_messages(conv.chat_id, [msg.id, response.id, respond.id])


@bot.on(admin_cmd(outgoing=True, pattern="dzd(?: |$)(.*)"))
@bot.on(sudo_cmd(outgoing=True, pattern="dzd(?: |$)(.*)", allow_sudo=True))
async def kakashi(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    if ".com" not in link:
        catevent = await edit_or_reply(
            event, "` I need a link to download something pro.`**(._.)**"
        )
    else:
        catevent = await edit_or_reply(event, "**Initiating Download!**")
    chat = "@DeezLoadBot"
    async with event.client.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            response = await conv.get_response()
            r = await conv.get_response()
            msg = await conv.send_message(link)
            details = await conv.get_response()
            song = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("**Error:** `unblock` @DeezLoadBot `and retry!`")
            return
        await catevent.delete()
        await event.client.send_file(event.chat_id, song, caption=details.text)
        await event.client.delete_messages(
            conv.chat_id, [msg_start.id, response.id, r.id, msg.id, details.id, song.id]
        )


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
