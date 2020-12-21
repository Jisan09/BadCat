# CC- @refundisillegal\nSyntax:-\n.get var NAME\n.del var NAME\n.set var NAME

# Copyright (C) 2020 Adek Maulana.
# All rights reserved.

import asyncio
import math
import os

import heroku3
import requests
import urllib3

from .. import CMD_HELP

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# =================

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY


@bot.on(admin_cmd(pattern=r"(set|get|del) var (.*)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"(set|get|del) var (.*)", allow_sudo=True))
async def variable(var):
    """
    Manage most of ConfigVars setting, set new var, get current var,
    or delete var...
    """
    if Config.HEROKU_API_KEY is None:
        return await edit_delete(
            var,
            "Set the required var in heroku to function this normally `HEROKU_API_KEY`.",
        )
    if Config.HEROKU_APP_NAME is not None:
        app = Heroku.app(Config.HEROKU_APP_NAME)
    else:
        return await edit_delete(
            var,
            "Set the required var in heroku to function this normally `HEROKU_APP_NAME`.",
        )
    exe = var.pattern_match.group(1)
    heroku_var = app.config()
    if exe == "get":
        cat = await edit_or_reply(var, "`Getting information...`")
        await asyncio.sleep(1.0)
        try:
            variable = var.pattern_match.group(2).split()[0]
            if variable in heroku_var:
                return await cat.edit(
                    "**ConfigVars**:" f"\n\n`{variable} = {heroku_var[variable]}`\n"
                )
            return await cat.edit(
                "**ConfigVars**:" f"\n\n`Error:\n-> {variable} don't exists`"
            )
        except IndexError:
            configs = prettyjson(heroku_var.to_dict(), indent=2)
            with open("configs.json", "w") as fp:
                fp.write(configs)
            with open("configs.json", "r") as fp:
                result = fp.read()
                if len(result) >= 4096:
                    await bot.send_file(
                        var.chat_id,
                        "configs.json",
                        reply_to=var.id,
                        caption="`Output too large, sending it as a file`",
                    )
                else:
                    await cat.edit(
                        "`[HEROKU]` ConfigVars:\n\n"
                        "================================"
                        f"\n```{result}```\n"
                        "================================"
                    )
            os.remove("configs.json")
            return
    elif exe == "set":
        variable = "".join(var.text.split(maxsplit=2)[2:])
        cat = await edit_or_reply(var, "`Setting information...`")
        if not variable:
            return await cat.edit("`.set var <ConfigVars-name> <value>`")
        value = "".join(variable.split(maxsplit=1)[1:])
        variable = "".join(variable.split(maxsplit=1)[0])
        if not value:
            return await cat.edit("`.set var <ConfigVars-name> <value>`")
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await cat.edit(f"`{variable}` **successfully changed to  ->  **`{value}`")
        else:
            await cat.edit(
                f"`{variable}`**  successfully added with value`  ->  **{value}`"
            )
        heroku_var[variable] = value
    elif exe == "del":
        cat = await edit_or_reply(var, "`Getting information to deleting variable...`")
        try:
            variable = var.pattern_match.group(2).split()[0]
        except IndexError:
            return await cat.edit("`Please specify ConfigVars you want to delete`")
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
            return await cat.edit(f"`{variable}`**  is not exists**")

        await cat.edit(f"`{variable}`  **successfully deleted**")
        del heroku_var[variable]


@bot.on(admin_cmd(pattern="usage$", outgoing=True))
@bot.on(sudo_cmd(pattern="usage$", allow_sudo=True))
async def dyno_usage(dyno):
    """
    Get your account Dyno Usage
    """
    if HEROKU_APP_NAME is None:
        return await edit_delete(
            dyno,
            "Set the required var in heroku to function this normally `HEROKU_APP_NAME`.",
        )
    if HEROKU_API_KEY is None:
        return await edit_delete(
            dyno,
            "Set the required var in heroku to function this normally `HEROKU_API_KEY`.",
        )
    dyno = await edit_or_reply(dyno, "`Processing...`")
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    user_id = Heroku.account().id
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {Config.HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + user_id + "/actions/get-quota"
    r = requests.get(heroku_api + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit(
            "`Error: something bad happened`\n\n" f">.`{r.reason}`\n"
        )
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]

    # - Used -
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    # - Current -
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)
    await asyncio.sleep(1.5)
    return await dyno.edit(
        "**Dyno Usage**:\n\n"
        f" -> `Dyno usage for`  **{Config.HEROKU_APP_NAME}**:\n"
        f"     •  `{AppHours}`**h**  `{AppMinutes}`**m**  "
        f"**|**  [`{AppPercentage}`**%**]"
        "\n\n"
        " -> `Dyno hours quota remaining this month`:\n"
        f"     •  `{hours}`**h**  `{minutes}`**m**  "
        f"**|**  [`{percentage}`**%**]"
    )


@bot.on(admin_cmd(pattern="herokulogs$", outgoing=True))
@bot.on(sudo_cmd(pattern="herokulogs$", allow_sudo=True))
async def _(dyno):
    if HEROKU_APP_NAME is None:
        return await edit_delete(
            dyno,
            "Set the required var in heroku to function this normally `HEROKU_APP_NAME`.",
        )
    if HEROKU_API_KEY is None:
        return await edit_delete(
            dyno,
            "Set the required var in heroku to function this normally `HEROKU_API_KEY`.",
        )
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        app = Heroku.app(HEROKU_APP_NAME)
    except BaseException:
        return await dyno.reply(
            " Please make sure your Heroku API Key, Your App name are configured correctly in the heroku"
        )
    data = app.get_log()
    key = (
        requests.post("https://nekobin.com/api/documents", json={"content": data})
        .json()
        .get("result")
        .get("key")
    )
    url = f"https://nekobin.com/{key}"
    reply_text = f"Recent 100 lines of heroku logs: [here]({url})"
    await edit_or_reply(dyno, reply_text)


def prettyjson(obj, indent=2, maxlinelength=80):
    """Renders JSON content with indentation and line splits/concatenations to fit maxlinelength.
    Only dicts, lists and basic types are supported"""
    items, _ = getsubitems(
        obj,
        itemkey="",
        islast=True,
        maxlinelength=maxlinelength - indent,
        indent=indent,
    )
    return indentitems(items, indent, level=0)


CMD_HELP.update(
    {
        "heroku": "__**PLUGIN NAME :** Heroku__\
  \n\n📌** CMD ➥** `.usage`\
  \n**USAGE   ➥  **Check your heroku dyno hours status.\
  \n\n📌** CMD ➥** `.set var` <NEW VAR> <VALUE>\
  \n**USAGE   ➥  **Add new variable or update existing value variable\
  \n\n📌** CMD ➥** `.get var` or `.get var <VAR>`\
  \n**USAGE   ➥  **Get your existing varibles & valus of that\
  \n\n📌** CMD ➥** `.del var` <VAR>\
  \n**USAGE   ➥  **Delete existing variable\
  \n\n📌** CMD ➥** `.herokulogs`\
  \n**USAGE   ➥  **Sends you recent 100 lines of logs in heroku\
  \n\n\n**!!! WARNING !!!, After adding or deleting variable the bot will restarted**\
  \n**Don't use .get var in public groups.This returns all of your private information, please be cautious...**"
    }
)
