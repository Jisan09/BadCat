import asyncio

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import CMD_HELP

# ================= CONSTANT =================
A = (
    "`▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ `\n"
    "`████▌▄▌▄▐▐▌█████ `\n"
    "`████▌▄▌▄▐▐▌▀████ `\n"
    "`▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ `\n"
)


B = (
    "`\n(\_/)`"
    "`\n(•_•)`"
    "`\n >🌹 *`"
    "`\n                    `"
    "`\n(\_/)`"
    "`\n(•_•)`"
    "`\n🌹<\ *`"
)
# ===========================================


@bot.on(admin_cmd(outgoing=True, pattern="imp (.*)"))
@bot.on(sudo_cmd(pattern="imp (.*)", allow_sudo=True))
async def _(event):
    kakashi = event.pattern_match.group(1)
    event = await edit_or_reply(event, f"{kakashi} is ejected.......")
    await asyncio.sleep(2)
    await event.edit("ඞㅤㅤㅤㅤ ㅤㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await event.edit("ㅤඞㅤㅤㅤㅤ ㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await event.edit("ㅤㅤ ඞㅤㅤㅤㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await event.edit("ㅤㅤㅤ ඞㅤㅤㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await event.edit("ㅤㅤㅤㅤ ඞㅤㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await event.edit("ㅤㅤㅤㅤㅤ ඞㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await event.edit("ㅤㅤㅤㅤㅤㅤ ඞㅤㅤ")
    await asyncio.sleep(0.8)
    await event.edit("ㅤㅤㅤㅤㅤㅤㅤ ඞㅤ")
    await asyncio.sleep(0.8)
    await event.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ඞ")
    await asyncio.sleep(0.8)
    await event.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ㅤ")
    await asyncio.sleep(0.2)
    await event.edit(
        f""". 　　　。　　　　•　 　ﾟ　　。 　　.
 .　　　 　　.　　　　　。　　 。　. 　

  . 　　 。   　     ඞ         。 . 　　 • 　　　　•

  ﾟ     {kakashi} was an Impostor.      。　. 　 　       。　.                                        。　. 
                                   　.          。　  　. 
　'         0 Impostor remains    　 。　.  　　.                。　.        。 　     .          。 　            .               .         .    ,      。
　　ﾟ　　　.　　.    ,　 　。　 　. 　 .     。"""
    )


@bot.on(admin_cmd(outgoing=True, pattern="nimp (.*)"))
@bot.on(sudo_cmd(pattern="nimp (.*)", allow_sudo=True))
async def _(event):
    kakashi = event.pattern_match.group(1)
    event = await edit_or_reply(event, f"{kakashi} is ejected.......")
    await asyncio.sleep(2)
    await event.edit("ඞㅤㅤㅤㅤ ㅤㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await event.edit("ㅤඞㅤㅤㅤㅤ ㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await event.edit("ㅤㅤ ඞㅤㅤㅤㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await event.edit("ㅤㅤㅤ ඞㅤㅤㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await event.edit("ㅤㅤㅤㅤ ඞㅤㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await event.edit("ㅤㅤㅤㅤㅤ ඞㅤㅤㅤ")
    await asyncio.sleep(0.8)
    await event.edit("ㅤㅤㅤㅤㅤㅤ ඞㅤㅤ")
    await asyncio.sleep(0.8)
    await event.edit("ㅤㅤㅤㅤㅤㅤㅤ ඞㅤ")
    await asyncio.sleep(0.8)
    await event.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ඞ")
    await asyncio.sleep(0.8)
    await event.edit("ㅤㅤㅤㅤㅤㅤㅤㅤ ㅤ")
    await asyncio.sleep(0.2)
    await event.edit(
        f""". 　　　。　　　　•　 　ﾟ　　。 　　.
 .　　　 　　.　　　　　。　　 。　. 　

  . 　　 。   　     ඞ         。 . 　　 • 　　　　•

  ﾟ     {kakashi} was not an Impostor.      。　. 　 　       。　.                                        。　. 
                                   　.          。　  　. 
　'         1 Impostor remains    　 。　.  　　.                。　.        。 　     .          。 　            .               .         .    ,      。
　　ﾟ　　　.　　.    ,　 　。　 　. 　 .     。"""
    )


@bot.on(admin_cmd(pattern="ml (.*)"))
@bot.on(sudo_cmd(pattern="ml (.*)", allow_sudo=True))
async def kakashi(jisan):
    message = jisan.pattern_match.group(1)
    await edit_or_reply(
        jisan,
        "`\n█████████`"
        "`\n█▄█████▄█`"
        "`\n█▼▼▼▼▼`"
        f"`\n█  {message}`"
        "`\n█▲▲▲▲▲`"
        "`\n█████████`"
        "`\n ██   ██`",
    )


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


@borg.on(admin_cmd(pattern=r"join$"))
@borg.on(sudo_cmd(pattern="join$", allow_sudo=True))
async def kakashi(event):
    await edit_or_reply(
        event,
        "`━━━━━┓ \n┓┓┓┓┓┃\n┓┓┓┓┓┃　ヽ○ノ ⇦ Me When You Joined \n┓┓┓┓┓┃.     /　 \n┓┓┓┓┓┃ ノ) \n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃`",
    )


@borg.on(admin_cmd(pattern=r"climb$"))
@borg.on(sudo_cmd(pattern="climb$", allow_sudo=True))
async def kakashi(event):
    await edit_or_reply(
        event,
        "`😏/\n/▌ \n/ \\n████\n╬╬\n╬╬\n╬╬\n╬╬\n╬╬\n╬╬\n╬╬\😦\n╬╬/▌\n╬╬/\`",
    )


@borg.on(admin_cmd(pattern=r"aag$"))
@borg.on(sudo_cmd(pattern="aag$", allow_sudo=True))
async def kakashi(event):
    await edit_or_reply(
        event,
        "`😲💨  🔥\n/|\     🔥🔥\n/ \   🔥🔥🔥`",
    )


@borg.on(admin_cmd(pattern=r"push$"))
@borg.on(sudo_cmd(pattern="push$", allow_sudo=True))
async def kakashi(event):
    await edit_or_reply(
        event,
        "`.      😎\n          |\👐\n         / \\\n━━━━━┓ ＼＼ \n┓┓┓┓┓┃\n┓┓┓┓┓┃ ヽ😩ノ\n┓┓┓┓┓┃ 　 /　\n┓┓┓┓┓┃  ノ)　 \n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃`",
    )


@borg.on(admin_cmd(pattern=r"work$"))
@borg.on(sudo_cmd(pattern="work$", allow_sudo=True))
async def kakashi(event):
    await edit_or_reply(
        event,
        "`📔📚           📚\n📓📚📖  😫  📚📚📓\n📕📚📚  📝  📗💻📘\n📖⁣📖📖📖📖📖📖📖📖`",
    )


@bot.on(admin_cmd(pattern=r"ohh$"))
@bot.on(sudo_cmd(pattern="ohh$", allow_sudo=True))
async def kakashi(event):
    await edit_or_reply(
        event,
        "`´´´´´████████´´\n´´`´███▒▒▒▒███´´´´´\n´´´███▒●▒▒●▒██´´´\n´´´███▒▒👄▒▒██´´\n´´█████▒▒████´´´´´\n´█████▒▒▒▒███´´\n█████▒▒▒▒▒▒███´´´´\n´´▓▓▓▓▓▓▓▓▓▓▓▓▓▒´´\n´´▒▒▒▒▓▓▓▓▓▓▓▓▓▒´´´´´\n´.▒▒▒´´▓▓▓▓▓▓▓▓▒´´´´´\n´.▒▒´´´´▓▓▓▓▓▓▓▒\n..▒▒.´´´´▓▓▓▓▓▓▓▒\n´▒▒▒▒▒▒▒▒▒▒▒▒\n´´´´´´´´´███████´´´´\n´´´´´´´´████████´´´´´´\n´´´´´´´█████████´´´´´\n´´´´´´██████████´´´\n´´´´´´██████████´´\n´´´´´´´█████████´\n´´´´´´´█████████´\n´´´´´´´´████████´´´\n´´´´´´´´´´´▒▒▒▒▒´´´\n´´´´´´´´´´▒▒▒▒▒´´´\n´´´´´´´´´´▒▒▒▒▒´´´\n´´´´´´´´´´▒▒´▒▒´´´\n´´´´´´´´´▒▒´´▒▒´´´\n´´´´´´´´´´▒▒´´´▒▒´´´\n´´´´´´´´´▒▒´´´▒▒´´´\n´´´´´´´´▒▒´´´´´▒▒´´´\n´´´´´´´´▒▒´´´´´´▒▒´´´\n´´´´´´´´███´´´´███´´´\n´´´´´´´´████´´███´´´\n´´´´´´´´█´´███´´████´´´`",
    )


@bot.on(admin_cmd(pattern=r"fail$"))
@bot.on(sudo_cmd(pattern="fail$", allow_sudo=True))
async def kakashi(fail):
    await edit_or_reply(fail, A)


@bot.on(admin_cmd(pattern=r"nih$"))
@bot.on(sudo_cmd(pattern="nih$", allow_sudo=True))
async def kakashi(lol):
    await edit_or_reply(lol, B)


CMD_HELP.update(
    {
        "art": "__**PLUGIN NAME :** Art__\
\n\n📌** CMD ➥** `.imp` / `.nimp` <text>\
\n**USAGE   ➥  **Find imposter.\
\n\n📌** CMD ➥** `.ml` <text>\
\n**USAGE   ➥  **Monster send your text.\
\n\n📌** CMD ➥** `.g1` <text>\
\n**USAGE   ➥  **Send Long list of your text.\
\n\n📌** CMD ➥** `.ftext` <text>\
\n**USAGE   ➥  **Send Ftext text.\
\n\n📌** CMD ➥** `.join` | `.climb` | `.aag` | `.push` |`.work` | `.ohh` | `.fail` | `.nih`\
\n\n**USAGE   ➥  **These are arts,use & see"
    }
)
