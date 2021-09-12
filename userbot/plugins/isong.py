#By @Feelded
from userbot import catub
from ..core.managers import edit_delete
from ..helpers.utils import reply_id
from . import deEmojify, hide_inlinebot

plugin_category = "useless"

@catub.cat_cmd(
    pattern="isong ?(.*)",
    command=("isong", plugin_category),
    info={
        "header": "Inline music downloader by @FeelDeD",
        "usage": [
            "{tr}isong <song name>",
        ],
    },
)
async def music(event):
    "Download song through @Deezermusicbot"
    if event.fwd_from:
        return
    bot = "@deezermusicbot"
    music = event.pattern_match.group(1)
    music = deEmojify(music)
    reply_to_id = await reply_id(event)
    if not music:
        return await edit_delete(
            event, "What should i search? Give a song name"
        )
    await event.delete()
    await hide_inlinebot(event.client, bot, music, event.chat_id, reply_to_id)


@catub.cat_cmd(
    pattern="ilyrics ?(.*)",
    command=("ilyrics", plugin_category),
    info={
        "header": "Search song lyrics inline by @FeelDeD",
        "usage": [
            "{tr}ilyrics <song name>",
        ],
    },
)
async def lyrics(event):
    "Search song lyrics through @ilyricsbot"
    if event.fwd_from:
        return
    bot = "@ilyricsbot"
    lyrics = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if not lyrics:
        return await edit_delete(
            event, "__What should i search? Give a song name__"
        )
    await event.delete()
    results = await event.client.inline_query(bot, lyrics)
    await results[0].click(event.chat_id, reply_to=reply_to_id)

@catub.cat_cmd(
    pattern="voice ?(.*)",
    command=("voice", plugin_category),
    info={
        "header": "Inline instant voice via Bot",
        "examples": "{tr}voice Hello motherfucker",
        "usage": [
            "{tr}voice <text>",
        ],
    },
)
async def app(event):
    await event.delete()
    bot = "MyInstantsBot"
    text = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if not text:
        return await edit_delete(
            event, "Give a me a text"
        )
    run = await event.client.inline_query(bot, text)
    result = await run[0].click(Config.OWNER_ID)
    await result.delete()
    await event.client.send_message(event.chat_id, result, reply_to=reply_to_id)
