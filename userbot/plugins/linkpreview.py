from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import CMD_HELP


@bot.on(admin_cmd(pattern="ctg$", outgoing=True))
@bot.on(sudo_cmd(pattern="ctg$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    if not reply_message:
        await edit_or_reply(event, "```Reply to a Link.```")
        return
    if not reply_message.text:
        await edit_or_reply(event, "```Reply to a Link```")
        return
    chat = "@chotamreaderbot"
    catevent = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=272572121)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit(
                "`RIP Check Your Blacklist Boss and unblock @chotamreaderbot`"
            )
            return
        if response.text.startswith(""):
            await catevent.edit("Am I Dumb Or Am I Dumb?")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)


CMD_HELP.update(
    {
        "linkpreview": "__**PLUGIN NAME :** Linkpreview__\
    \n\n📌** CMD ➥** `.ctg` reply to link\
    \n\n**USAGE   ➥  **Converts the given link to link preview"
    }
)
