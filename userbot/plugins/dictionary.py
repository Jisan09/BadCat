# Urban Dictionary for catuserbot by @mrconfused
from PyDictionary import PyDictionary

from ..helpers.utils import _format
from . import AioHttp, catub, edit_delete, edit_or_reply

plugin_category = "utils"


@catub.cat_cmd(
    pattern="ud (.*)",
    command=("ud", plugin_category),
    info={
        "header": "To fetch meaning of the given word from urban dictionary.",
        "usage": "{tr}ud <word>",
    },
)
async def _(event):
    "To fetch meaning of the given word from urban dictionary."
    word = event.pattern_match.group(1)
    try:
        response = await AioHttp().get_json(
            f"http://api.urbandictionary.com/v0/define?term={word}",
        )
        word = response["list"][0]["word"]
        definition = response["list"][0]["definition"]
        example = response["list"][0]["example"]
        result = "**Text: {}**\n**Meaning:**\n`{}`\n\n**Example:**\n`{}`".format(
            _format.replacetext(word),
            _format.replacetext(definition),
            _format.replacetext(example),
        )
        await edit_or_reply(event, result)
    except Exception as e:
        await edit_delete(
            event,
            text="`The Unban Dictionary API could not be reached`",
        )
        print(e)


@catub.cat_cmd(
    pattern="meaning (.*)",
    command=("meaning", plugin_category),
    info={
        "header": "To fetch meaning of the given word from dictionary.",
        "usage": "{tr}meaning <word>",
    },
)
async def _(event):
    "To fetch meaning of the given word from dictionary."
    word = event.pattern_match.group(1)
    dictionary = PyDictionary()
    cat = dictionary.meaning(word)
    output = f"**Word :** __{word}__\n\n"
    try:
        for a, b in cat.items():
            output += f"**{a}**\n"
            for i in b:
                output += f"☞__{i}__\n"
        await edit_or_reply(event, output)
    except Exception:
        await edit_or_reply(event, f"Couldn't fetch meaning of {word}")
