import random
import re
import time
from platform import python_version

from telethon import version
from telethon.events import CallbackQuery

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import catalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import StartTime, catub, catversion, hmention, mention

plugin_category = "utils"


@catub.cat_cmd(
    pattern="alive$",
    command=("alive", plugin_category),
    info={
        "header": "To check bot's alive status",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}alive",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    ##############################NUB########################################
    EMOJI = "✧✧" if gvarstatus("ALIVE_EMOJI") is None else EMOJI = gvarstatus("ALIVE_EMOJI")
    CUSTOM_ALIVE_TEXT = "✮ MY BOT IS RUNNING SUCCESSFULLY ✮" if gvarstatus("ALIVE_TEXT") is None else CUSTOM_ALIVE_TEXT = gvarstatus("ALIVE_TEXT")
    if gvarstatus("ALIVE_PIC") is not None: CAT = [x for x in gvarstatus("ALIVE_PIC").split()]
    CAT_IMG = list(CAT)
    ##############################END#########################################
    if CAT_IMG:
        PIC = random.choice(CAT_IMG)
        cat_caption = f"<b>{CUSTOM_ALIVE_TEXT}</b>\n\n"
        cat_caption += f"<b>{EMOJI} Master : {hmention}</b>\n"
        cat_caption += f"<b>{EMOJI} Uptime :</b> <code>{uptime}</code>\n"
        cat_caption += (f"<b>{EMOJI} Python Version :</b> <code>{python_version()}</code>\n")
        cat_caption += (f"<b>{EMOJI} Telethon version :</b> <code>{version.__version__}</code>\n")
        cat_caption += (f"<b>{EMOJI} Catuserbot Version :</b> <code>{catversion}</code>\n")
        cat_caption += f"<b>{EMOJI} Database :</b> <code>{check_sgnirts}</code>\n\n"
        cat_caption += "    <a href = https://github.com/sandy1709/catuserbot><b>GoodCat</b></a> | <a href = https://github.com/Jisan09/catuserbot><b>BadCat</b></a> | <a href = https://t.me/catuserbot_support><b>Support</b></a>"
        await event.client.send_file(
            event.chat_id,
            PIC,
            caption=cat_caption,
            parse_mode="html",
            reply_to=reply_to_id,
            allow_cache=True,
        )
        await event.delete()
    else:
        await edit_or_reply(
            event,
            f"<b>{CUSTOM_ALIVE_TEXT}</b>\n\n"
            f"<b>{EMOJI} Master : {hmention}</b>\n"
            f"<b>{EMOJI} Uptime :</b> <code>{uptime}</code>\n"
            f"<b>{EMOJI} Python Version :</b> <code>{python_version()}</code>\n"
            f"<b>{EMOJI} Telethon version :</b> <code>{version.__version__}</code>\n"
            f"<b>{EMOJI} Catuserbot Version :</b> <code>{catversion}</code>\n"
            f"<b>{EMOJI} Database :</b> <code>{check_sgnirts}</code>\n\n"
            "    <a href = https://github.com/sandy1709/catuserbot><b>GoodCat</b></a> | <a href = https://github.com/Jisan09/catuserbot><b>BadCat</b></a> | <a href = https://t.me/catuserbot_support><b>Support</b></a>",
            parse_mode="html",
        )


@catub.cat_cmd(
    pattern="ialive$",
    command=("ialive", plugin_category),
    info={
        "header": "To check bot's alive status via inline mode",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}alive",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details by your inline bot"
    reply_to_id = await reply_id(event)
    EMOJI = "✧✧" if gvarstatus("ALIVE_EMOJI") is None else EMOJI = gvarstatus("ALIVE_EMOJI")
    cat_caption = f"**Catuserbot is Up and Running**\n"
    cat_caption += f"**{EMOJI} Telethon version :** `{version.__version__}\n`"
    cat_caption += f"**{EMOJI} Catuserbot Version :** `{catversion}`\n"
    cat_caption += f"**{EMOJI} Python Version :** `{python_version()}\n`"
    cat_caption += f"**{EMOJI} Master:** {mention}\n"
    results = await event.client.inline_query(Config.TG_BOT_USERNAME, cat_caption)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


@catub.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await catalive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)
