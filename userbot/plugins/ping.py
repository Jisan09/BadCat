import asyncio
from datetime import datetime

from ..core.managers import edit_or_reply
from . import catub, hmention

plugin_category = "tools"


@catub.cat_cmd(
    pattern="(p|ping)( -a|$)",
    command=("p", plugin_category),
    info={
        "header": "check how long it takes to ping your userbot",
        "flags": {"-a": "average ping"},
        "usage": ["{tr}p", "{tr}p -a"],
    },
)
async def _(event):
    "To check ping"
    flag = event.pattern_match.group(2)
    start = datetime.now()
    if flag == " -a":
        catevent = await edit_or_reply(event, "__**Hmm, Pinging...**__")
        await catevent.edit("`!....`")
        await asyncio.sleep(0.1)
        await catevent.edit("`..!..`")
        await asyncio.sleep(0.1)
        await catevent.edit("`....!`")
        end = datetime.now()
        tms = (end - start).microseconds / 1000
        ms = round((tms - 0.2) / 3, 3)
        await catevent.edit(
        f"┏━━━━━━━━━━━┓\n┃ ⁭⁫⁭<b><i>〣 Average Pong!</b></i>\n┃⁭⁫⁭<b><i> ⁭⁫⁭⁭〣 {ms}</b></i>\n┃⁭⁫⁭<b><i> ⁭〣 {hmention}</b></i>\n┗━━━━━━━━━━━┛"
        , parse_mode="html")
    else:
        catevent = await edit_or_reply(event, "__**Hmm, Pinging...**__")
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await catevent.edit(f"<b><i>〣 Ping: {ms} ms\n〣 Owner: {hmention}</b></i>", parse_mode="html")
