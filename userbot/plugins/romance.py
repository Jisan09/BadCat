#Created by @Jisan7509

import base64
import random
from . import catub
from telethon import functions, types
from ..helpers.utils import _catutils, reply_id
from ..core.managers import edit_delete,edit_or_reply
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.functions.messages import ImportChatInviteRequest as Get


plugin_category = "useless"


@catub.cat_cmd(
    pattern="kiss(?: |$)(.*)",
    command=("kiss", plugin_category),
    info={
        "header": "Sends random kiss",
        "usage": [
            "{tr}kiss",
            "{tr}kiss <1-20>",
        ],
    },
)
async def some(event):
    """Its useless for single like you. Get a lover first"""
    inpt = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    count = 1 if not inpt else int(inpt) 
    if count< 0 and count> 20:
        await edit_delete(event,"`Give value in range 1-20`")
    res = base64.b64decode("aHR0cHM6Ly90Lm1lL2pvaW5jaGF0L0NtZEEwVzYtSVVsbFpUUTk=").decode('utf-8')
    resource = await event.client(GetFullChannelRequest(res))
    chat = resource.chats[0].username
    try:
        await event.client(functions.channels.GetParticipantRequest(channel = chat, participant = event.from_id.user_id))
    except UserNotParticipantError:
        await event.client(Get(res.split("/")[4]))
        await event.client.edit_folder(resource.full_chat.id, 1)
        await event.client(functions.account.UpdateNotifySettingsRequest(
            peer= chat,
            settings = types.InputPeerNotifySettings(
                show_previews=False,
                silent= True,
            )
        ))
    catevent = await edit_or_reply(event,"`Wait babe...`😘")
    maxmsg = await event.client.get_messages(chat)
    start = random.randint(31, maxmsg.total)
    if start > maxmsg.total-40:
        start = maxmsg.total-40
    end = start + 41
    kiss = []
    async for x in event.client.iter_messages(chat, min_id = start, max_id = end, reverse = True):
        try:
            if x.media and x.media.document.mime_type == "video/mp4":
                link = f"{res.split('j')[0]}{chat}/{x.id}"
                kiss.append(link)
        except AttributeError:
            pass
    kisss = random.sample(kiss, count)
    for i in kisss:
        nood = await event.client.send_file(event.chat_id,i,reply_to=reply_to_id)
        await _catutils.unsavegif(event, nood)
    await catevent.delete()
    
