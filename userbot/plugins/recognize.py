# credits: @Mr_Hops

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.utils import admin_cmd, sudo_cmd
from userbot import CMD_HELP


@borg.on(admin_cmd(pattern="recognize ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("Reply to any user's media message.")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("reply to media file")
        return
    chat = "@Rekognition_Bot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("Reply to actual users message.")
        return
    cat = await event.edit("recognizeing this media")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=461083923))
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("unblock @Rekognition_Bot and try again")
            await cat.delete()
            return
        if response.text.startswith("See next message."):
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=461083923))
            response = await response
            cat = response.message.message
            await event.edit(cat)

        else:
            await event.edit("sorry, I couldnt find it")


@borg.on(sudo_cmd(pattern="recognize ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.reply("Reply to any user's media message.")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.reply("reply to media file")
        return
    chat = "@Rekognition_Bot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.reply("Reply to actual users message.")
        return
    cat = await event.reply("recognizeing this media")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=461083923))
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("unblock @Rekognition_Bot and try again")
            await cat.delete()
            return
        if response.text.startswith("See next message."):
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=461083923))
            response = await response
            cat = response.message.message
            await event.reply(cat)
            await cat.delete()
        else:
            await event.reply("sorry, I couldn't find it")
            await cat.delete()

CMD_HELP.update({
    "recognize":
    "`.recognize` reply this to any media file\
    \nUSAGE : Get information about an image using AWS Rekognition.\
    \nFind out information including detected labels, faces. text and moderation tags."
})
