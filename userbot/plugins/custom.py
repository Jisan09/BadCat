from userbot import catub
from userbot.core.logger import logging

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.globals import addgvar, delgvar, gvarstatus

plugin_category = "utils"
LOGS = logging.getLogger(__name__)
cmdhd = Config.COMMAND_HAND_LER
extractor = URLExtract()
vlist = [
    "ALIVE_PIC",
    "ALIVE_EMOJI",
    "ALIVE_TEXT",
    "IALIVE_TEXT",
    "IALIVE_PIC",
    "HELP_EMOJI",
    "HELP_TEXT",
    "PM_PIC",
]


@catub.cat_cmd(
    pattern="(set|get|del)dv(?: |$)(.*)",
    command=("dv", plugin_category),
    info={
        "header": "Set vars in database or Check or Delete",
        "description": "Set , Fetch or Delete values or vars directly in database without restart or heroku vars.\n\nYou can set multiple pics by giving space after links in alive, ialive, pm permit.",
        "flags": {
            "set": "To set new var in database or modify the old var",
            "get": "To show the already existing var value.",
            "del": "To delete the existing value",
        },
        "var name": {
            "ALIVE_PIC": "To set picture in alive",
            "ALIVE_EMOJI": "To set custom emoji in alive",
            "ALIVE_TEXT": "To set custom text in alive",
            "IALIVE_TEXT": "To set custom text in ialive",
            "IALIVE_PIC": "To set picture in alive",
            "HELP_EMOJI": "To set custom emoji in help",
            "HELP_TEXT": "To set custom text in help",
            "PM_PIC": "To customize pmpermit pic",
        },
        "usage": [
            "{tr}setdv <var name> <var value>",
            "{tr}getdv <var name>",
            "{tr}deldv <var name>",
        ],
        "examples": [
            "{tr}setdv ALIVE_PIC <pic link>",
            "{tr}setdv ALIVE_PIC <pic link 1> <pic link 2>",
            "{tr}getdv ALIVE_PIC",
            "{tr}deldv ALIVE_PIC",
        ],
    },
)
async def bad(event):
    "To manage vars in database"
    cmd = event.pattern_match.group(1).lower()
    vname = event.pattern_match.group(2)
    vnlist = ""
    for i, each in enumerate(vlist, start=1):
        vnlist += f"{i}. `{each}`\n"
    if not vname:
        return await edit_delete(
            event, f"**📑 Give correct var name from the list :\n\n**{vnlist}", time=60
        )
    if " " in vname:
        vname, vinfo = vname.split(" ", 1)
    if vname in vlist:
        if cmd == "set":
            if not vinfo:
                return await edit_delete(
                    event, f"Give some values which you want to save for **{vname}**"
                )
            if "PIC" in vname and "https://t" not in vinfo:
                await edit_delete(event, "**Give me a correct link...**")
            else:
                addgvar(vname, vinfo)
                await edit_delete(
                    event, f"📑 Value of **{vname}** is changed to :- `{vinfo}`", time=20
                )
        if cmd == "get":
            var_data = gvarstatus(vname)
            await edit_delete(
                event, f"📑 Value of **{vname}** is  `{var_data}`", time=20
            )
        elif cmd == "del":
            delgvar(vname)
            await edit_delete(
                event,
                f"📑 Value of **{vname}** is now deleted & set to default.",
                time=20,
            )
    else:
        await edit_delete(
            event, f"**📑 Give correct var name from the list :\n\n**{vnlist}", time=60
        )


@catub.cat_cmd(
    pattern="custom (pmpermit|pmblock)$",
    command=("custom", plugin_category),
    info={
        "header": "To customize your CatUserbot.",
        "options": {
            "pmpermit": "To customize pmpermit text. ",
            "pmblock": "To customize pmpermit block message.",
        },
        "custom": {
            "{mention}": "mention user",
            "{first}": "first name of user",
            "{last}": "last name of user",
            "{fullname}": "fullname of user",
            "{username}": "username of user",
            "{userid}": "userid of user",
            "{my_first}": "your first name",
            "{my_last}": "your last name ",
            "{my_fullname}": "your fullname",
            "{my_username}": "your username",
            "{my_mention}": "your mention",
            "{totalwarns}": "totalwarns",
            "{warns}": "warns",
            "{remwarns}": "remaining warns",
        },
        "usage": [
            "{tr}custom <option> reply",
        ],
    },
)
async def custom_catuserbot(event):
    "To customize your CatUserbot."
    reply = await event.get_reply_message()
    text = reply.text
    if not reply:
        return await edit_delete(event, "__Reply to custom text or url__")
    input_str = event.pattern_match.group(1)
    if input_str == "pmpermit":
        addgvar("pmpermit_txt", text)
    if input_str == "pmblock":
        addgvar("pmblock", text)
    await edit_or_reply(event, f"__Your custom {input_str} has been updated__")


@catub.cat_cmd(
    pattern="delcustom (pmpermit|pmblock)$",
    command=("delcustom", plugin_category),
    info={
        "header": "To delete costomization of your CatUserbot.",
        "options": {
            "pmpermit": "To delete custom pmpermit text",
            "pmblock": "To delete custom pmpermit block message",
        },
        "usage": [
            "{tr}delcustom <option>",
        ],
    },
)
async def custom_catuserbot(event):
    "To delete costomization of your CatUserbot."
    input_str = event.pattern_match.group(1)
    if input_str == "pmpermit":
        if gvarstatus("pmpermit_txt") is None:
            return await edit_delete(event, "__You haven't customzied your pmpermit.__")
        delgvar("pmpermit_txt")
    if input_str == "pmblock":
        if gvarstatus("pmblock") is None:
            return await edit_delete(event, "__You haven't customzied your pmblock.__")
        delgvar("pmblock")
    await edit_or_reply(
        event, f"__Succesfully deleted your customization of {input_str}.__"
    )
