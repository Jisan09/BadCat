"""
Created by @Jisan7509
Peru helper @mrconfused
Userbot plugin for CatUserbot
"""
from userbot import CMD_HELP
from userbot.utils import admin_cmd

from . import *


@borg.on(admin_cmd(pattern="emoji(?: |$)(.*)"))
async def itachi(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`What I am Supposed to do nibba `")
        return
    string = "  ".join(args).lower()
    for chutiya in string:
        if chutiya in emojify.kakashitext:
            bsdk = emojify.kakashiemoji[emojify.kakashitext.index(chutiya)]
            string = string.replace(chutiya, bsdk)
    await event.edit(string)


@borg.on(admin_cmd(pattern="cmoji(?: |$)(.*)"))
async def itachi(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("`What I am Supposed to do nibba `")
        return
    emoji, args = args.split(" ", 1)
    string = "  ".join(args).lower()
    for chutiya in string:
        if chutiya in emojify.itachitext:
            bsdk = emojify.itachiemoji[emojify.itachitext.index(chutiya)].format(
                cj=emoji
            )
            string = string.replace(chutiya, bsdk)
    await event.edit(string)


CMD_HELP.update(
    {
        "emojitxt": "__**PLUGIN NAME :** Emojitxt__\
      \n\n📌** CMD ➥** `.emoji` <text>\
      \n**USAGE   ➥  **Converts your text to big emoji text, with default emoji. \
      \n\n📌** CMD ➥** `.cmoji` <emoji> <text>\
      \n**USAGE   ➥  **Converts your text to big emoji text, with your custom emoji.\
      \n\n**☞ NOTE :** For giving sapce between two words use **@** symbol.\
      \n**EXAMPLE :**  `.emoji Bad@cat`\
      \n         `.cmoji 😋 Good@cat`"
    }
)
