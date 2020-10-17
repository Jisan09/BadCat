import asyncio

from telethon import events

from ..utils import admin_cmd, edit_or_reply, register, sudo_cmd
from . import ALIVE_NAME, CMD_HELP

DEF = str(ALIVE_NAME) if ALIVE_NAME else "cat"
USR = str(Config.LIVE_USERNAME) if Config.LIVE_USERNAME else "@Jisan7509"




@bot.on(admin_cmd(pattern="ftext (.*)"))
@bot.on(sudo_cmd(pattern="ftext (.*)", allow_sudo=True))
async def payf(event):
    paytext = event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 8,
        paytext * 8,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 6,
        paytext * 6,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
    )
    await edit_or_reply(event, pay)


@bot.on(admin_cmd(outgoing=True, pattern="g1 ?(.*)"))
@bot.on(sudo_cmd(pattern="g1 ?(.*)", allow_sudo=True))
async def payf(event):
    paytext = event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
        paytext * 1,
    )
    await edit_or_reply(event, pay)


# ================= CONSTANT =================



# ===========================================


A = (
    "`▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ `\n"
    "`████▌▄▌▄▐▐▌█████ `\n"
    "`████▌▄▌▄▐▐▌▀████ `\n"
    "`▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ `\n"
)





E = (
    "`\n(\_/)`"
    "`\n(•_•)`"
    "`\n >🌹 *`"
    "`\n                    `"
    "`\n(\_/)`"
    "`\n(•_•)`"
    "`\n🌹<\ *`"
)

@borg.on(admin_cmd(pattern="ml (.*)"))
async def kakashi(jisan):
    message = jisan.pattern_match.group(1)
    await jisan.edit(
        "`\n█████████`"
        "`\n█▄█████▄█`"
        "`\n█▼▼▼▼▼`"
        f"`\n█  {message}`"
        "`\n█▲▲▲▲▲`"
        "`\n█████████`"
        "`\n ██   ██`"
    )




@borg.on(admin_cmd(pattern=r"fail$"))
async def kakashi(fail):
    await fail.edit(A)



@borg.on(admin_cmd(pattern=r"nih$"))
async def kakashi(shit):
    await shit.edit(E)

CMD_HELP.update(
    {
        "art": "__**PLUGIN NAME :** Art__\
\n\n📌** CMD ➥** `.g1` <text>\
\n**USAGE   ➥  **Send Long list of your text.\
"
    }
)
