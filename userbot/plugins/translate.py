from googletrans import LANGUAGES

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import getTranslate
from ..sql_helper.globals import addgvar, gvarstatus
from . import BOTLOG, BOTLOG_CHATID, catub, deEmojify

plugin_category = "utils"


@catub.cat_cmd(
    pattern="tl ([\s\S]*)",
    command=("tl", plugin_category),
    info={
        "header": "To translate the text to required language.",
        "note": "For langugage codes check [this link](https://bit.ly/2SRQ6WU)",
        "usage": [
            "{tr}tl <language code> ; <text>",
            "{tr}tl <language codes>",
        ],
        "examples": "{tr}tl te ; Catuserbot is one of the popular bot",
    },
)
async def _(event):
    "To translate the text."
    input_str = event.pattern_match.group(1)
    text = None
    if ";" in input_str:
        lan, text = input_str.split(";")
    elif event.reply_to_msg_id and not text:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "en"
    else:
        return await edit_delete(
            event, "`.tl LanguageCode` as reply to a message", time=5
        )
    text = deEmojify(text.strip())
    lan = lan.strip()
    try:
        translated = await getTranslate(text, dest=lan)
        after_tr_text = translated.text
        output_str = f"**TRANSLATED from {LANGUAGES[translated.src].title()} to {LANGUAGES[lan].title()}**\
                \n`{after_tr_text}`"
        await edit_or_reply(event, output_str)
    except Exception as exc:
        await edit_delete(event, f"**Error:**\n`{exc}`", time=5)


@catub.cat_cmd(
    pattern="trt(?: |$)([\s\S]*)",
    command=("trt", plugin_category),
    info={
        "header": "To translate the text to required language.",
        "note": "for this command set lanuage by `.lang trt` command.",
        "usage": [
            "{tr}trt",
            "{tr}trt <text>",
        ],
    },
)
async def translateme(trans):
    "To translate the text to required language."
    textx = await trans.get_reply_message()
    message = trans.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await edit_or_reply(
            trans, "`Give a text or reply to a message to translate!`"
        )
    TRT_LANG = gvarstatus("TRT_LANG") or "en"
    try:
        reply_text = await getTranslate(deEmojify(message), dest=TRT_LANG)
    except ValueError:
        return await edit_delete(trans, "`Invalid destination language.`", time=5)
    source_lan = LANGUAGES[f"{reply_text.src.lower()}"]
    transl_lan = LANGUAGES[f"{reply_text.dest.lower()}"]
    reply_text = f"**From {source_lan.title()}({reply_text.src.lower()}) to {transl_lan.title()}({reply_text.dest.lower()}) :**\n`{reply_text.text}`"

    await edit_or_reply(trans, reply_text)
    if BOTLOG:
        await trans.client.send_message(
            BOTLOG_CHATID,
            f"`Translated some {source_lan.title()} stuff to {transl_lan.title()} just now.`",
        )


@catub.cat_cmd(
    pattern="lang (ai|trt|tocr) ([\s\S]*)",
    command=("lang", plugin_category),
    info={
        "header": "To set language for trt/ai command.",
        "description": "Check here [Language codes](https://bit.ly/2SRQ6WU)",
        "options": {
            "trt": "default language for trt command",
            "tocr": "default language for tocr command",
            "ai": "default language for chatbot(ai)",
        },
        "usage": "{tr}lang option <language codes>",
        "examples": [
            "{tr}lang trt te",
            "{tr}lang tocr bn",
            "{tr}lang ai hi",
        ],
    },
)
async def lang(value):
    "To set language for trt comamnd."
    arg = value.pattern_match.group(2).lower()
    input_str = value.pattern_match.group(1)
    if arg not in LANGUAGES:
        return await edit_or_reply(
            value,
            f"`Invalid Language code !!`\n`Available language codes for TRT`:\n\n`{LANGUAGES}`",
        )
    LANG = LANGUAGES[arg]
    if input_str == "trt":
        addgvar("TRT_LANG", arg)
        await edit_or_reply(
            value, f"`Language for Translator changed to {LANG.title()}.`"
        )
    elif input_str == "tocr":
        addgvar("TOCR_LANG", arg)
        await edit_or_reply(
            value, f"`Language for Translated Ocr changed to {LANG.title()}.`"
        )
    else:
        addgvar("AI_LANG", arg)
        await edit_or_reply(
            value, f"`Language for chatbot is changed to {LANG.title()}.`"
        )
    LANG = LANGUAGES[arg]

    if BOTLOG and input_str == "trt":
        await value.client.send_message(
            BOTLOG_CHATID, f"`Language for Translator changed to {LANG.title()}.`"
        )
    if BOTLOG:
        if input_str == "tocr":
            await value.client.send_message(
                BOTLOG_CHATID,
                f"`Language for Translated Ocr changed to {LANG.title()}.`",
            )
        if input_str == "ai":
            await value.client.send_message(
                BOTLOG_CHATID, f"`Language for chatbot is changed to {LANG.title()}.`"
            )
