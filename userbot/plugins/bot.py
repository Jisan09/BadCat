# plugin by @Infinity20998 for Catuserbot

from ..helpers.utils import reply_id
from . import catub, edit_delete, reply_id

plugin_category = "bot"


@catub.cat_cmd(
    pattern="bot(?: |$)(.*)",
    command=("bot", plugin_category),
    info={
        "header": "Send any text through your bot if the bot is in the chat",
        "usage": "{tr}bot <text>",
        "examples": "{tr}bot Hello everyone",
    },
)
async def botmsg(event):
    "Send your text through your bot."
    text = event.pattern_match.group(1)
    chat = event.chat_id
    reply_to_id = await reply_id(event)
    if not text:
        return await edit_delete(
            event, "__What should I send through bot? Give some text.__"
        )
    await event.client.tgbot.send_message(chat, text, reply_to=reply_to_id)
    await event.delete()


@catub.cat_cmd(
    pattern="mbot(?: |$)(.*)",
    command=("mbot", plugin_category),
    info={
        "header": "Send any media through your bot if the bot is in the chat",
        "usage": "{tr}mbot <reply to a media>",
        "examples": "{tr}mbot",
    },
)
async def botmsg(event):
    "Send media through your bot."
    reply_message = await event.get_reply_message()
    if not event.reply_to_msg_id or not reply_message.media:
        return await edit_delete(event, "Reply to a media file...")
    media = await reply_message.download_media()
    chat = event.chat_id
    await event.client.tgbot.send_file(chat, media)
    await event.delete()
