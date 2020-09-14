import time
from platform import python_version

import nekos
import requests
from PIL import Image
from telethon import version

from userbot import ALIVE_NAME, CMD_HELP, StartTime, catdef, catversion
from . import catalive
from ..uniborgConfig import Config
from ..utils import admin_cmd, edit_or_reply, sudo_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"
CAT_IMG = Config.ALIVE_PIC
JISAN = Config.CUSTOM_ALIVE_TEXT
EMOJI = str(Config.CUSTOM_ALIVE_EMOJI) if Config.CUSTOM_ALIVE_EMOJI else "✧✧"


@borg.on(admin_cmd(outgoing=True, pattern="alive$"))
@borg.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = alive.message
    hmm = bot.uid
    if alive.reply_to_msg_id:
        reply_to_id = await alive.get_reply_message()
    if JISAN:
        if CAT_IMG:
            cat_caption = f"**{JISAN}**\n\n"
            cat_caption += f"**{EMOJI} Master:** [{DEFAULTUSER}](tg://user?id={hmm})\n"
            cat_caption += f"**{EMOJI} Uptime :** `{uptime}\n`"
            cat_caption += f"**{EMOJI} Python Version :** `{python_version()}\n`"
            cat_caption += f"**{EMOJI} Telethon version :** `{version.__version__}\n`"
            cat_caption += f"**{EMOJI} Catuserbot Version :** `{catversion}`\n"
            cat_caption += f"**{EMOJI} Database :** `{check_sgnirts}`\n\n"
            cat_caption += "   **[GoodCat]**(https://github.com/sandy1709/catuserbot) | **[BadCat]**(https://github.com/Jisan09/catuserbot) | **[Support]**(https://t.me/catuserbot_support) "
            await borg.send_file(
                alive.chat_id,
                CAT_IMG,
                caption=cat_caption,
                reply_to=reply_to_id,
            )
            await alive.delete()
        else:
            await edit_or_reply(
                alive,
                f"** {JISAN}**\n\n"
                f"**{EMOJI} Master:** [{DEFAULTUSER}](tg://user?id={hmm})\n"
                f"**{EMOJI} Uptime :** `{uptime}\n`"
                f"**{EMOJI} Python Version :** `{python_version()}\n`"
                f"**{EMOJI} Telethon Version :** `{version.__version__}\n`"
                f"**{EMOJI} Catuserbot Version :** `{catversion}`\n"
                f"**{EMOJI} Database :** `{check_sgnirts}`\n"
                "   **[GoodCat]**(https://github.com/sandy1709/catuserbot) | **[BadCat]**(https://github.com/Jisan09/catuserbot) | **[Support]**(https://t.me/catuserbot_support) ",
            )
    elif CAT_IMG:
        cat_caption = "__**✮ MY BOT IS RUNNING SUCCESFULLY ✮**__\n\n"
        cat_caption += f"**{EMOJI} Database :** `{check_sgnirts}`\n"
        cat_caption += f"**{EMOJI} Telethon version :** `{version.__version__}\n`"
        cat_caption += f"**{EMOJI} Catuserbot Version :** `{catversion}`\n"
        cat_caption += f"**{EMOJI} Python Version :** `{python_version()}\n`"
        cat_caption += f"**{EMOJI} Uptime :** `{uptime}\n`"
        cat_caption += (
            f"**{EMOJI} My peru Master:** [{DEFAULTUSER}](tg://user?id={hmm})\n"
        )
        await borg.send_file(
            alive.chat_id, CAT_IMG, caption=cat_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            "__**✮ MY BOT IS RUNNING SUCCESFULLY ✮**__\n\n"
            f"**{EMOJI} Database :** `{check_sgnirts}`\n"
            f"**{EMOJI} Telethon Version :** `{version.__version__}\n`"
            f"**{EMOJI} Catuserbot Version :** `{catversion}`\n"
            f"**{EMOJI} Python Version :** `{python_version()}\n`"
            f"**{EMOJI} Uptime :** `{uptime}\n`"
            f"**{EMOJI} My Peru Master:** [{DEFAULTUSER}](tg://user?id={hmm})\n",
        )


@borg.on(admin_cmd(outgoing=True, pattern="live$"))
@borg.on(sudo_cmd(pattern="live$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    tgbotusername = Var.TG_BOT_USER_NAME_BF_HER
    reply_to_id = alive.message
    if alive.reply_to_msg_id:
        reply_to_id = await alive.get_reply_message()
    hmm = bot.uid
    cat_caption = f"__**Catuserbot is Up and Running**__\n"
    cat_caption += f"**  -Telethon version :** `{version.__version__}\n`"
    cat_caption += f"**  -Catuserbot Version :** `{catversion}`\n"
    cat_caption += f"**  -Python Version :** `{python_version()}\n`"
    cat_caption += f"**  -My peru Master:** [{DEFAULTUSER}](tg://user?id={hmm})\n"
    results = await bot.inline_query(tgbotusername, cat_caption)  # pylint:disable=E0602
    await results[0].click(alive.chat_id, reply_to=reply_to_id, hide_via=True)
    await alive.delete()


@borg.on(admin_cmd(pattern="cat$"))
@borg.on(sudo_cmd(pattern="cat$", allow_sudo=True))
async def _(event):
    try:
        await event.delete()
    except BaseException:
        pass
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.cat()).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    img.seek(0)
    await bot.send_file(event.chat_id, open("temp.webp", "rb"), reply_to=reply_to_id)

CMD_HELP.update(
    {
        "alive": "__**PLUGIN NAME :** Alive__\
      \n\n📌** CMD ➥** `.alive`\
      \n**USAGE   ➥  **To see wether your bot is working or not.\
      \n\n📌** CMD ➥** `.live`\
      \n**USAGE   ➥**  status of bot.\
      \n\n📌** CMD ➥** `.cat`\
      \n**USAGE   ➥**  Random cat stickers"
    }
)
