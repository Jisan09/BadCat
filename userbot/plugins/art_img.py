"""
Created by @Jisan7509
plugin for Cat_Userbot
☝☝☝
You remove this, you gay.
"""
import os

from telethon.errors.rpcerrorlist import YouBlockedUserError

from . import convert_toimage, mention


@bot.on(admin_cmd("iascii ?(.*)"))
@bot.on(sudo_cmd(pattern="iascii ?(.*)", allow_sudo=True))
async def bad(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        return await edit_delete(event, "```Reply to any user message.```")
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        return await edit_delete(event, "```Reply to a media file...```")
    c_id = await reply_id(event)
    if not os.path.isdir("./temp"):
        os.mkdir("./temp")
    output_file = os.path.join("./temp", "jisan.jpg")
    if ".png" in reply_message.file.ext:
        output_file = await event.client.download_media(reply_message, output_file)
    else:
        output = await _cattools.media_to_pic(event, reply_message)
        outputt = convert_toimage(output[1], filename="./temp/jisan.jpg")
    chat = "@asciiart_bot"
    kakashi = await edit_or_reply(event, "```Wait making ASCII...```")
    async with event.client.conversation(chat) as conv:
        try:
            msg = await conv.send_file(output_file)
            response = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await kakashi.edit("```Please unblock @asciiart_bot and try again```")
            return
        if response.text.startswith("Forward"):
            await kakashi.edit(
                "```can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await kakashi.delete()
            await event.client.send_file(
                event.chat_id,
                response,
                reply_to=c_id,
                caption=f"**➥ Image Type :** ASCII Art\n**➥ Uploaded By :** {mention}",
            )
            await event.client.send_read_acknowledge(conv.chat_id)
    await event.client.delete_messages(conv.chat_id, [msg.id, response.id])
    if os.path.exists(output_file):
        os.remove(output_file)


@bot.on(admin_cmd(pattern="line ?(.*)"))
@bot.on(sudo_cmd(pattern="line ?(.*)", allow_sudo=True))
async def pussy(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        return await edit_delete(event, "```Reply to any user message.```")
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        return await edit_delete(event, "```Reply to a media file...```")
    c_id = await reply_id(event)
    if not os.path.isdir("./temp"):
        os.mkdir("./temp")
    output_file = os.path.join("./temp", "jisan.jpg")
    if ".png" in reply_message.file.ext:
        output_file = await event.client.download_media(reply_message, output_file)
    else:
        output = await _cattools.media_to_pic(event, reply_message)
        outputt = convert_toimage(output[1], filename="./temp/jisan.jpg")
    chat = "@Lines50Bot"
    reply_message.sender
    if reply_message.sender.bot:
        await edit_or_reply(event, "```Reply to actual users message.```")
        return
    kakashi = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation(chat) as conv:
        try:
            msg = await conv.send_file(output_file)
            pic = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await kakashi.edit("```Please unblock @Lines50Bot and try again```")
            return
        await kakashi.delete()
        await event.client.send_file(
            event.chat_id,
            pic,
            reply_to=c_id,
            caption=f"**➥ Image Type :** LINE Art \n**➥ Uploaded By :** {mention}",
        )
    await event.client.delete_messages(conv.chat_id, [msg.id, pic.id])
    if os.path.exists(output_file):
        os.remove(output_file)


@bot.on(admin_cmd(pattern="clip ?(.*)"))
@bot.on(sudo_cmd(pattern="clip ?(.*)", allow_sudo=True))
async def cat(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        return await edit_delete(event, "```Reply to any user message.```")
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        return await edit_delete(event, "```Reply to a media file...```")
    c_id = await reply_id(event)
    if not os.path.isdir("./temp"):
        os.mkdir("./temp")
    output_file = os.path.join("./temp", "jisan.jpg")
    if ".png" in reply_message.file.ext:
        output_file = await event.client.download_media(reply_message, output_file)
    else:
        output = await _cattools.media_to_pic(event, reply_message)
        outputt = convert_toimage(output[1], filename="./temp/jisan.jpg")
    chat = "@clippy"
    reply_message.sender
    if reply_message.sender.bot:
        await edit_or_reply(event, "```Reply to actual users message.```")
        return
    kakashi = await edit_or_reply(event, "```Processing...```")
    async with event.client.conversation(chat) as conv:
        try:
            msg = await conv.send_file(output_file)
            pic = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await kakashi.edit("```Please unblock @clippy and try again```")
            return
        await kakashi.delete()
        await event.client.send_file(
            event.chat_id,
            pic,
            reply_to=c_id,
        )
    await event.client.delete_messages(conv.chat_id, [msg.id, pic.id])
    if os.path.exists(output_file):
        os.remove(output_file)


CMD_HELP.update(
    {
        "art_img": "__**PLUGIN NAME :** Art Image__\
      \n\n📌** CMD ➥** `.iascii` reply to any image file:\
      \n**USAGE   ➥  **Makes an image ascii style, try out your own.\
      \n\n📌** CMD ➥** `.line` reply to any image file:\
      \n**USAGE   ➥  **Makes an image line style.\
      \n\n📌** CMD ➥** `.clip` reply to any image file:\
      \n**USAGE   ➥  **Makes a stylish sticker."
    }
)
