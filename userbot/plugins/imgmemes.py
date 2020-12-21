# credits to @mrconfused (@sandy1709)

#  Copyright (C) 2020  sandeep.n(π.$)
import asyncio
import base64
import os
import re

from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from . import (
    changemymind,
    deEmojify,
    fakegs,
    kannagen,
    moditweet,
    reply_id,
    trumptweet,
    tweets,
)


@bot.on(admin_cmd(outgoing=True, pattern="fakegs(?: |$)(.*)", command="fakegs"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="fakegs(?: |$)(.*)", command="fakegs"))
async def nekobot(cat):
    if cat.fwd_from:
        return
    text = cat.pattern_match.group(1)
    reply_to_id = await reply_id(cat)
    if not text:
        if cat.is_reply and not reply_to_id.media:
            text = reply_to_id.message
        else:
            await edit_delete(cat, "`What should i search in google.`", 5)
            return
    cate = await edit_or_reply(cat, "`Connecting to https://www.google.com/ ...`")
    text = deEmojify(text)
    if ";" in text:
        search, result = text.split(";")
    else:
        await edit_delete(
            cat,
            "__How should i create meme follow the syntax as show__ `.fakegs top text ; bottom text`",
            5,
        )
        return
    catfile = await fakegs(search, result)
    await asyncio.sleep(2)
    await cat.client.send_file(cat.chat_id, catfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(catfile):
        os.remove(catfile)


@bot.on(admin_cmd(outgoing=True, pattern="trump(?: |$)(.*)", command="trump"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="trump(?: |$)(.*)", command="trump"))
async def nekobot(cat):
    if cat.fwd_from:
        return
    text = cat.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(cat)
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    reply = await cat.get_reply_message()
    if not text:
        if cat.is_reply and not reply.media:
            text = reply.message
        else:
            await edit_delete(cat, "**Trump : **`What should I tweet`", 5)
            return
    cate = await edit_or_reply(cat, "`Requesting trump to tweet...`")
    try:
        hmm = Get(hmm)
        await cat.client(hmm)
    except BaseException:
        pass
    text = deEmojify(text)
    await asyncio.sleep(2)
    catfile = await trumptweet(text)
    await cat.client.send_file(cat.chat_id, catfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(catfile):
        os.remove(catfile)


@bot.on(admin_cmd(outgoing=True, pattern="modi(?: |$)(.*)", command="modi"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="modi(?: |$)(.*)", command="modi"))
async def nekobot(cat):
    if cat.fwd_from:
        return
    text = cat.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(cat)
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    reply = await cat.get_reply_message()
    if not text:
        if cat.is_reply and not reply.media:
            text = reply.message
        else:
            await edit_delete(cat, "**Modi : **`What should I tweet`", 5)
            return
    cate = await edit_or_reply(cat, "Requesting modi to tweet...")
    try:
        hmm = Get(hmm)
        await cat.client(hmm)
    except BaseException:
        pass
    text = deEmojify(text)
    await asyncio.sleep(2)
    catfile = await moditweet(text)
    await cat.client.send_file(cat.chat_id, catfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(catfile):
        os.remove(catfile)


@bot.on(admin_cmd(outgoing=True, pattern="cmm(?: |$)(.*)", command="cmm"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="cmm(?: |$)(.*)", command="cmm"))
async def nekobot(cat):
    if cat.fwd_from:
        return
    text = cat.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(cat)
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    reply = await cat.get_reply_message()
    if not text:
        if cat.is_reply and not reply.media:
            text = reply.message
        else:
            await edit_delete(cat, "`Give text to write on banner, man`", 5)
            return
    cate = await edit_or_reply(cat, "`Your banner is under creation wait a sec...`")
    try:
        hmm = Get(hmm)
        await cat.client(hmm)
    except BaseException:
        pass
    text = deEmojify(text)
    await asyncio.sleep(2)
    catfile = await changemymind(text)
    await cat.client.send_file(cat.chat_id, catfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(catfile):
        os.remove(catfile)


@bot.on(admin_cmd(outgoing=True, pattern="kanna(?: |$)(.*)", command="kanna"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="kanna(?: |$)(.*)", command="kanna"))
async def nekobot(cat):
    if cat.fwd_from:
        return
    text = cat.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(cat)
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    reply = await cat.get_reply_message()
    if not text:
        if cat.is_reply and not reply.media:
            text = reply.message
        else:
            await edit_delete(cat, "**Kanna : **`What should i show you`", 5)
            return
    cate = await edit_or_reply(cat, "`Kanna is writing your text...`")
    try:
        hmm = Get(hmm)
        await e.client(hmm)
    except BaseException:
        pass
    text = deEmojify(text)
    await asyncio.sleep(2)
    catfile = await kannagen(text)
    await cat.client.send_file(cat.chat_id, catfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(catfile):
        os.remove(catfile)


@bot.on(admin_cmd(outgoing=True, pattern="tweet(?: |$)(.*)", command="tweet"))
@bot.on(sudo_cmd(allow_sudo=True, pattern="tweet(?: |$)(.*)", command="tweet"))
async def nekobot(cat):
    if cat.fwd_from:
        return
    text = cat.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(cat)
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    reply = await cat.get_reply_message()
    if not text:
        if cat.is_reply and not reply.media:
            text = reply.message
        else:
            await edit_delete(
                cat,
                "what should I tweet? Give some text and format must be like `.tweet username ; your text` ",
                5,
            )
            return
    try:
        hmm = Get(hmm)
        await cat.client(hmm)
    except BaseException:
        pass
    if ";" in text:
        username, text = text.split(";")
    else:
        await edit_delete(
            cat,
            "__what should I tweet? Give some text and format must be like__ `.tweet username ; your text`",
            5,
        )
        return
    cate = await edit_or_reply(cat, f"`Requesting {username} to tweet...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    catfile = await tweets(text, username)
    await cat.client.send_file(cat.chat_id, catfile, reply_to=reply_to_id)
    await cate.delete()
    if os.path.exists(catfile):
        os.remove(catfile)


CMD_HELP.update(
    {
        "imgmemes": """__**PLUGIN NAME :** Imgmemes__
      \n\n📌** CMD ➥** `.fakegs search query ; what you mean text`
      \n**USAGE   ➥  **__Shows you image meme for your google search query__ 
      \n\n📌** CMD ➥** `.trump` <reply/text>
      \n**USAGE   ➥  **__Sends you the trump tweet sticker with given custom text__
      \n\n📌** CMD ➥** `.modi` <reply/text>
      \n**USAGE   ➥  **__Sends you the modi tweet sticker with given custom text__ 
      \n\n📌** CMD ➥** `.cmm` <reply/text>
      \n**USAGE   ➥  **__Sends you the  Change my mind banner with given custom text__ 
      \n\n📌** CMD ➥** `.kanna` <reply/text>
      \n**USAGE   ➥  **__Sends you the kanna chan sticker with given custom text__
      \n\n📌** CMD ➥** `.tweet reply/<username> ; <text>`
      \n**USAGE   ➥  **__Sends you the desired person tweet sticker with given custom text__ 
  """
    }
)
