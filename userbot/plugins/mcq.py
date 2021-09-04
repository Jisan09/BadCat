# By @deepaiims
import random

from userbot import catub

from ..core.managers import edit_delete
from ..helpers.utils import reply_id

plugin_category = "utils"


@catub.cat_cmd(
    pattern="mcq ?(.*)",
    command=("mcq", plugin_category),
    info={
        "header": "Chooses a random values in the given options, give a space to add multiple option",
        "usage": [
            "{tr}mcq <options>",
            "{tr}mcq a b c d",
            "{tr}mcq physics chemistry math biology",
        ],
    },
)
async def Gay(event):
    "Jai matadi"
    if event.fwd_from:
        return
    inp = event.pattern_match.group(1)
    await reply_id(event)
    if not inp:
        return await edit_delete(event, "What to choose from", 15)
    options = inp.split()
    await edit_delete(event, random.choice(options), 120)
