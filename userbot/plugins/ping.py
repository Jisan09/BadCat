import asyncio
from datetime import datetime

from ..core.managers import edit_or_reply
from . import catub, hmention

plugin_category = "tools"


@catub.cat_cmd(
    pattern="p( -a|$)",
    command=("p", plugin_category),
    info={
        "header": "check how long it takes to ping your userbot",
        "flags": {"-a": "average ping"},
        "usage": ["{tr}p", "{tr}p -a"],
    },
)
async def _(event):
    "To check ping"
    catevent = await edit_or_reply(event, "<b><i>Hmm, Pinging....</b></i>", "html")
    flag = event.pattern_match.group(1)
    start = datetime.now()
    if flag == " -a":
        await catevent.edit("`!....`")
        await asyncio.sleep(0.3)
        await catevent.edit("`..!..`")
        await asyncio.sleep(0.3)
        await catevent.edit("`....!`")
        end = datetime.now()
        tms = (end - start).microseconds / 1000
        ms = round((tms - 0.6) / 3, 3)
        await catevent.edit(f"**⌘ Average Ping**\n :- {ms} ms")
    else:
        await catevent.edit("<b><i>Hmm, Pinging....</b></i>", "html")
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await catevent.edit(
            f"<b><i>〣 Ping: </b></i> : {ms} <b><i>ms\n〣 Owner: {hmention}</b></i>",
            parse_mode="html",
        )
