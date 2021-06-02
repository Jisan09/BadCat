import re
from collections import defaultdict, deque

import regex
from telethon import events
from telethon.tl import functions, types

from userbot import catub

from ..Config import Config

plugin_category = "tools"

HEADER = "「sed」\n"
KNOWN_RE_BOTS = re.compile(Config.GROUP_REG_SED_EX_BOT_S, flags=re.IGNORECASE)

# Heavily based on
# https://github.com/SijmenSchoon/regexbot/blob/master/regexbot.py

last_msgs = defaultdict(lambda: deque(maxlen=10))


def doit(chat_id, match, original):
    fr = match.group(1)
    to = match.group(2)
    to = to.replace("\\/", "/")
    try:
        fl = match.group(3)
        if fl is None:
            fl = ""
        fl = fl[1:]
    except IndexError:
        fl = ""

    # Build Python regex flags
    count = 1
    flags = 0
    for f in fl:
        if f == "i":
            flags |= regex.IGNORECASE
        elif f == "g":
            count = 0
        else:
            return None, f"Unknown flag: {f}"

    def actually_doit(original):
        try:
            s = original.message
            if s.startswith(HEADER):
                s = s[len(HEADER) :]
            s, i = regex.subn(fr, to, s, count=count, flags=flags)
            if i > 0:
                return original, s
        except Exception as e:
            return None, f"u dun goofed m8: {str(e)}"
        return None, None

    if original is not None:
        return actually_doit(original)
    # Try matching the last few messages
    for org in last_msgs[chat_id]:
        m, s = actually_doit(org)
        if s is not None:
            return m, s
    return None, None


async def group_has_sedbot(group):
    if isinstance(group, types.InputPeerChannel):
        full = await catub(functions.channels.GetFullChannelRequest(group))
    elif isinstance(group, types.InputPeerChat):
        full = await catub(functions.messages.GetFullChatRequest(group.chat_id))
    else:
        return False

    return any(KNOWN_RE_BOTS.match(x.username or "") for x in full.users)


@catub.on(events.NewMessage)
async def on_message(event):
    last_msgs[event.chat_id].appendleft(event.message)


@catub.on(events.MessageEdited)
async def on_edit(event):
    for m in last_msgs[event.chat_id]:
        if m.id == event.id:
            m.raw_text = event.raw_text
            break


@catub.cat_cmd(
    pattern="^s/((?:\\/|[^/])+)/((?:\\/|[^/])*)(/.*)?",
    command=("sed", plugin_category),
    info={
        "header": "Replaces a word or words with other words.",
        "description": "Tag any sentence and type s/a/b. where is required word to replace and b is correct word.",
        "usage": "s<delimiter><old word(s)><delimiter><new word(s)>",
        "delimiters": ["/", ":", "|", "_"],
        "examples": "s/delimiter/symbol - replace this command to this message",
    },
)
async def on_regex(event):
    "To replace words in sentences"
    if not event.is_private and await group_has_sedbot(await event.get_input_chat()):
        await edit_delete(event, "This group has a sed bot. Ignoring this message!")
        return
    m, s = doit(event.chat_id, event.pattern_match, await event.get_reply_message())
    if m is not None:
        s = f"{HEADER}{s}"
        out = await event.client.send_message(
            await event.get_input_chat(), s, reply_to=m.id
        )
        last_msgs[event.chat_id].appendleft(out)
    elif s is not None:
        await edit_or_reply(event, s)
    raise events.StopPropagation
