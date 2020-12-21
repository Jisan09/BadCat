from telethon.tl.types import ChannelParticipantsAdmins

from . import reply_id


@bot.on(admin_cmd(pattern="tagall$"))
@bot.on(sudo_cmd(pattern="tagall$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    mentions = "@all"
    chat = await event.get_input_chat()
    async for x in event.client.iter_participants(chat, 100):
        mentions += f"[\u2063](tg://user?id={x.id})"
    await reply_to_id.reply(mentions)
    await event.delete()


@bot.on(admin_cmd(pattern="all( (.*)|$)"))
@bot.on(sudo_cmd(pattern="all( (.*)|$)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    input_str = event.pattern_match.group(1)
    mentions = input_str or "@all"
    chat = await event.get_input_chat()
    async for x in event.client.iter_participants(chat, 100):
        mentions += f"[\u2063](tg://user?id={x.id})"
    await event.client.send_message(event.chat_id, mentions, reply_to=reply_to_id)
    await event.delete()


@bot.on(admin_cmd(pattern="report$"))
@bot.on(sudo_cmd(pattern="report$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "@admin: **Spam Spotted**"
    chat = await event.get_input_chat()
    reply_to_id = await reply_id(event)
    async for x in event.client.iter_participants(
        chat, filter=ChannelParticipantsAdmins
    ):
        mentions += f"[\u2063](tg://user?id={x.id})"
    await event.client.send_message(event.chat_id, mentions, reply_to=reply_to_id)
    await event.delete()


@bot.on(admin_cmd(pattern="men (.*)"))
@bot.on(sudo_cmd(pattern="men (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id:
        reply_msg = await event.get_reply_message()
        u = reply_msg.sender_id
        str = input_str
    else:
        user, str = input_str.split(" ", 1)
        try:
            u = int(user)
        except ValueError:
            try:
                u = await event.client.get_entity(user)
            except ValueError:
                await event.delete()
                return
            u = int(u.id)
        except:
            await event.delete()
            return
    await event.delete()
    await event.client.send_message(
        event.chat_id,
        f"<a href='tg://user?id={u}'>{str}</a>",
        parse_mode="HTML",
        reply_to=reply_to_id,
    )


CMD_HELP.update(
    {
        "mention": """__**PLUGIN NAME :** Mention__
\n\n📌** CMD ➥** `.all`
\n**USAGE   ➥  **__Tags recent 100 persons in the group may not work for all__  
\n\n📌** CMD ➥** `.tagall`
\n**USAGE   ➥  **__Tags recent 100 persons in the group may not work for all__ 
\n\n📌** CMD ➥** `.report`
\n**USAGE   ➥  **__Tags admins in group__  
\n\n📌** CMD ➥** `.men` <username/userid text>
\n**USAGE   ➥  **__Tags that person with the given custom text other way for this is __
\n\n📌** CMD ➥** `Hi @username[custom text]`
"""
    }
)
