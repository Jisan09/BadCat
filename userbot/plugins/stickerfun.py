# Random RGB Sticklet by @PhycoNinja13b
# modified by @UniBorg
# imported from ppe-remix by @heyworld & @DeletedUser420
# modified by @mrconfused

import io
import os
import random
import textwrap

from PIL import Image, ImageDraw, ImageFont
from telethon.tl.types import InputMessagesFilterDocument

from .. import CMD_HELP, bot
from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import deEmojify, waifutxt

# RegEx by https://t.me/c/1220993104/500653 ( @SnapDragon7410 )


@borg.on(admin_cmd(outgoing=True, pattern="st(?: |$)(.*)"))
@borg.on(sudo_cmd(allow_sudo=True, pattern="st(?: |$)(.*)"))
async def waifu(animu):
    text = animu.pattern_match.group(1)
    reply_to_id = animu.message
    if animu.reply_to_msg_id:
        reply_to_id = await animu.get_reply_message()
    if not text:
        if animu.is_reply:
            text = (await animu.get_reply_message()).message
        else:
            await edit_or_reply(
                animu, "`You haven't written any article, Waifu is going away.`"
            )
            return
    text = deEmojify(text)
    await animu.delete()
    await waifutxt(text, animu.chat_id, reply_to_id, bot, borg)


# 12 21 28 30


@borg.on(admin_cmd(pattern=r"stcr ?(?:(.*?) \| )?(.*)", outgoing=True))
@borg.on(sudo_cmd(pattern=r"stcr ?(?:(.*?) \| )?(.*)", allow_sudo=True))
async def sticklet(event):
    R = random.randint(0, 256)
    G = random.randint(0, 256)
    B = random.randint(0, 256)
    reply_message = event.message
    # get the input text
    # the text on which we would like to do the magic on
    font_file_name = event.pattern_match.group(1)
    if not font_file_name:
        font_file_name = ""
    sticktext = event.pattern_match.group(2)
    if not sticktext and event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        sticktext = reply_message.message
    elif not sticktext:
        await edit_or_reply(event, "need something, hmm")
        return
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
    # delete the userbot command,
    # i don't know why this is required
    await event.delete()
    sticktext = deEmojify(sticktext)
    # https://docs.python.org/3/library/textwrap.html#textwrap.wrap
    sticktext = textwrap.wrap(sticktext, width=10)
    # converts back the list to a string
    sticktext = "\n".join(sticktext)
    image = Image.new("RGBA", (512, 512), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    fontsize = 230
    FONT_FILE = await get_font_file(event.client, "@catfonts", font_file_name)
    font = ImageFont.truetype(FONT_FILE, size=fontsize)
    while draw.multiline_textsize(sticktext, font=font) > (512, 512):
        fontsize -= 3
        font = ImageFont.truetype(FONT_FILE, size=fontsize)
    width, height = draw.multiline_textsize(sticktext, font=font)
    draw.multiline_text(
        ((512 - width) / 2, (512 - height) / 2), sticktext, font=font, fill=(R, G, B)
    )
    image_stream = io.BytesIO()
    image_stream.name = "@catuserbot17.webp"
    image.save(image_stream, "WebP")
    image_stream.seek(0)
    # finally, reply the sticker
    await event.client.send_file(
        event.chat_id,
        image_stream,
        caption="cat's Sticklet",
        reply_to=event.message.reply_to_msg_id,
    )
    # cleanup
    try:
        os.remove(FONT_FILE)
    except BaseException:
        pass


async def get_font_file(client, channel_id, search_kw=""):
    # first get the font messages
    font_file_message_s = await client.get_messages(
        entity=channel_id,
        filter=InputMessagesFilterDocument,
        # this might cause FLOOD WAIT,
        # if used too many times
        limit=None,
        search=search_kw,
    )
    # get a random font from the list of fonts
    # https://docs.python.org/3/library/random.html#random.choice
    font_file_message = random.choice(font_file_message_s)
    # download and return the file path
    return await client.download_media(font_file_message)


CMD_HELP.update(
    {
        "stickerfun": "__**PLUGIN NAME :** Stickerfun__\
    \n\n📌** CMD ➥** `.st` <your txt>\
    \n**USAGE   ➥  **Anime that makes your writing fun.\
    \n\n📌** CMD ➥** `.stcr` <your txt>\
    \n**USAGE   ➥  **Your text as sticker\
    "
    }
)
