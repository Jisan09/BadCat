# Template by @Infinity20998
# Modified by @o_s_h_o_r_a_j
from userbot import catub

from ..core.managers import edit_delete
from ..helpers.utils import reply_id

plugin_category = "extra"


@catub.cat_cmd(
    pattern="hc ?(.*)",
    command=("hc", plugin_category),
    info={
        "header": "Hides the message via @hideitbot with █",
        "usage": [
            "{tr}hc <text>",
            "{tr}hc -p <text *hide*> "
        ],
        "flag":{"-p": "hides words inside **"},
    },
)
async def hideit01(event):
    "Hide your message through @HideitBot"
    if event.fwd_from:
        return
    bot = "@hideitbot"
    hidetxt = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if not hidetxt:
        return await edit_delete(
            event, "__What should I hide through bot? Give some text.__"
        )
    await event.delete()
    if "-p" in hidetxt:
        hidetxt = hidetxt.replace("-p", "")
        if not hidetxt:
            return await edit_delete(
            event, "__What should I hide through bot? Give some text.__"
        )
        else:
            results = await event.client.inline_query(bot, hidetxt)
            await results[1].click(event.chat_id, reply_to=reply_to_id)
    else:
        results = await event.client.inline_query(bot, hidetxt)
        await results[0].click(event.chat_id, reply_to=reply_to_id)


@catub.cat_cmd(
    pattern="hq ?(.*)",
    command=("hq", plugin_category),
    info={
        "header": "Hides the message via @hideitbot with ❓",
        "usage": [
            "{tr}hq <text>",
        ],
    },
)
async def hideit02(event):
    "Hide your message through @HideitBot"
    if event.fwd_from:
        return
    bot = "@hideitbot"
    hidetxt = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if not hidetxt:
        return await edit_delete(
            event, "__What should I hide through bot? Give some text.__"
        )
    await event.delete()
    results = await event.client.inline_query(bot, hidetxt)
    await results[1].click(event.chat_id, reply_to=reply_to_id)
