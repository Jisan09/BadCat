"""DA.GD helpers in @UniBorg
Available Commands:
.dns google.com
.url <long url>
.unshort <short url>
.hl <link>
"""

import requests

from userbot import CMD_HELP

from ..utils import admin_cmd, edit_or_reply, sudo_cmd


@borg.on(admin_cmd(pattern="dns (.*)"))
@borg.on(sudo_cmd(pattern="dns (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/dns/{}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await edit_or_reply(
            event, "DNS records of {} are \n{}".format(input_str, response_api)
        )
    else:
        await edit_or_reply(
            event, "i can't seem to find {} on the internet".format(input_str)
        )


@borg.on(admin_cmd(pattern="url (.*)"))
@borg.on(sudo_cmd(pattern="url (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url={}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await edit_or_reply(
            event, "Generated {} for {}.".format(response_api, input_str)
        )
    else:
        await edit_or_reply(event, "something is wrong. please try again later.")


@borg.on(admin_cmd(pattern="unshort (.*)"))
@borg.on(sudo_cmd(pattern="unshort (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if not input_str.startswith("http"):
        input_str = "http://" + input_str
    r = requests.get(input_str, allow_redirects=False)
    if str(r.status_code).startswith("3"):
        await edit_or_reply(
            event,
            "Input URL: {}\nReDirected URL: {}".format(
                input_str, r.headers["Location"]
            ),
        )
    else:
        await edit_or_reply(
            event,
            "Input URL {} returned status_code {}".format(input_str, r.status_code),
        )


# By Priyam Kalra
@borg.on(admin_cmd(pattern="hl ?(.*)"))
@borg.on(sudo_cmd(pattern="hl ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input = event.pattern_match.group(1)
    await edit_or_reply(event, "[ㅤㅤㅤㅤㅤㅤㅤ](" + input + ")")
    await event.delete()


CMD_HELP.update(
    {
        "dagd": "__**PLUGIN NAME :** Dagd__\
    \n\n📌** CMD ➥** `.dns` <link>\
    \n**USAGE   ➥  **Shows you Domain Name System(dns) of the given link . example `.dns google.com` or `.dns github.cm`\
    \n\n📌** CMD ➥** `.url` <link>\
    \n**USAGE   ➥  **Shortens the given link\
    \n\n📌** CMD ➥** `.unshort` <link>\
    \n**USAGE   ➥  **Unshortens the given short link\
    \n\n📌** CMD ➥** `.hl` <link>\
    \n**USAGE   ➥  **Hide the given link\
    "
    }
)
