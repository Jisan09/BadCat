from telethon.utils import pack_bot_file_id

from .. import CMD_HELP
from ..utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd(pattern="get_id"))
@bot.on(sudo_cmd(pattern="get_id", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await edit_or_reply(
                event,
                "Current Chat ID: `{}`\nFrom User ID: `{}`\nBot API File ID: `{}`".format(
                    str(event.chat_id), str(r_msg.sender_id), bot_api_file_id
                ),
            )
        else:
            await edit_or_reply(
                event,
                "Current Chat ID: `{}`\nFrom User ID: `{}`".format(
                    str(event.chat_id), str(r_msg.sender_id)
                ),
            )
    else:
        await edit_or_reply(event, "Current Chat ID: `{}`".format(str(event.chat_id)))


CMD_HELP.update(
    {
        "Get_id": "__**PLUGIN NAME :** Get_id__\
    \n\n📌** CMD ➥** `.get_id`\
\n**USAGE   ➥  **To get id of certain chat,channel or user."
    }
)
