# this plugin is created by @deeoaiims

import os

import asyncio

from telethon.errors.rpcerrorlist import YouBlockedUserError, UserAlreadyParticipantError

from telethon.tl.functions.messages import ImportChatInviteRequest

from telethon import events

from userbot import catub

from . import mention

from ..core.managers import edit_delete, edit_or_reply

from ..helpers.utils import _format

plugin_category = "extra"

@catub.cat_cmd(

    pattern="(d|i)()logo?(?:\s|$)([\s\S]*)",

    command=("advancelogo", plugin_category),

    info={

        "header": "To make logo of given text with random beautiful background and random fonts.",

        "flag": {

            "d": "To make logo of given text document format",

            "i": "To make logo of given text compressed image format",

        },

        "usage": [

            "{tr}dlogo <text>",

            "{tr}ilogo <text>",

        ],

        "examples":[ 

            "{tr}dlogo Venom",

            "{tr}ilogo Venom",

        ],

    },

)

async def _(event):

    "To make logo of given text."

    cmd = event.pattern_match.group(1).lower()

    chat = "@BHLogoBot"

    tr = os.environ.get("COMMAND_HAND_LER")

    if cmd == "d" :

        input_str = "".join(event.text.split(maxsplit=1)[1:])

        if not input_str :

            await edit_delete(

            event,

            "Please give some text.",

            )

        else :

            async with event.client.conversation(chat) as conv:

                try:

                    try:

                        await event.client(ImportChatInviteRequest('RvT1YQvgl_8D9Hbd'))

                    except UserAlreadyParticipantError:

                        await asyncio.sleep(0.00000069420)

                    await conv.send_message(f"/gen {input_str}")

                    await event.delete()

                    Venom = await conv.get_response(1)

                    cat = await event.client.send_message(event.chat_id, Venom)

                    Peter = await conv.get_response(1)

                    Mine = input_str

                    Zarox = str(Peter.file.ext)

                    Parker = Mine + Zarox

                    file = await event.client.download_media(Peter, Parker)

                except YouBlockedUserError:

                    return await edit_or_reply(event,f"`{tr}unblock @BHLogoBot` and then try",)

                await event.client.send_file(event.chat_id,  file, force_document=True, caption=f"➥ Genrated by :- {mention}")

                await event.client.delete_messages(event.chat_id, cat)

    if cmd == "i" :

        input_str = "".join(event.text.split(maxsplit=1)[1:])

        if not input_str:

            await edit_delete(

            event,

            "Please give some text.",

            )

        else :

            async with event.client.conversation(chat) as conv:

                try:

                    try:

                        await event.client(ImportChatInviteRequest('RvT1YQvgl_8D9Hbd'))

                    except UserAlreadyParticipantError:

                        await asyncio.sleep(0.00000069420)

                    await conv.send_message(f"/gen {input_str}")

                    await event.delete()

                    Venom = await conv.get_response(1)

                    cat = await event.client.send_message(event.chat_id, Venom)

                    Peter = await conv.get_response(1)

                    Mine = input_str

                    Zarox = str(Peter.file.ext)

                    Parker = Mine + Zarox

                    file = await event.client.download_media(Peter, Parker)

                except YouBlockedUserError:

                    await edit_or_reply(event,f"`{tr}unblock @BHLogoBot` and then try",)

                await event.client.send_file(event.chat_id,  file, force_document=False, caption=f"➥ Genrated by :- {mention}")

                await event.client.delete_messages(event.chat_id, cat)

                if os.path.exists(file):    os.remove(file)
