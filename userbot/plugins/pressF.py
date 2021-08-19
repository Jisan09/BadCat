# Made by @o_s_h_o_r_a_j
# Change credit and you gay.
from userbot import catub

from ..core.managers import edit_delete
from ..helpers.utils import reply_id

plugin_category = "extra"


@catub.cat_cmd(
    pattern="pf ?(.*)",
    command=("pf", plugin_category),
    info={
        "header": "Pay tribute to victim by pressing F(s)",
        "usage": [
            "{tr}pf <text>",
        ],
    },
)
async def GayIfUChangeCredit(event):
    "Bullies the victim"
    await event.delete()
    if event.fwd_from:
        return
    bot = "@FsInChatBot"
    hidetxt = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if not hidetxt:
        return await edit_delete(
            event, "__How should I bulli without text.__"
        )
    results = await event.client.inline_query(bot, hidetxt)
    await results[0].click(event.chat_id, reply_to=reply_to_id)
