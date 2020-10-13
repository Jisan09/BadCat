import requests
from telethon import functions

from userbot import ALIVE_NAME

from .. import CMD_HELP, CMD_LIST, SUDO_LIST
from ..utils import admin_cmd, edit_or_reply, sudo_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"
USERNAME = str(Config.LIVE_USERNAME) if Config.LIVE_USERNAME else "@Jisan7509"


@bot.on(admin_cmd(pattern="help ?(.*)"))
async def cmd_list(event):
    reply_to_id = None
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    input_str = event.pattern_match.group(1)
    if input_str == "text":
        string = (
            "Total {count} commands found in {plugincount} plugins of catuserbot\n\n"
        )
        catcount = 0
        plugincount = 0
        for i in sorted(CMD_LIST):
            plugincount += 1
            string += f"{plugincount}) Command found in Plugin " + i + " are \n"
            for iter_list in CMD_LIST[i]:
                string += "    " + str(iter_list)
                string += "\n"
                catcount += 1
            string += "\n"
        if len(string) > 4095:
            data = string.format(count=catcount, plugincount=plugincount)
            key = (
                requests.post(
                    "https://nekobin.com/api/documents", json={"content": data}
                )
                .json()
                .get("result")
                .get("key")
            )
            url = f"https://nekobin.com/{key}"
            reply_text = f"All commands of the catuserbot are [here]({url})"
            await event.edit(reply_text)
            return
        await event.edit(string.format(count=catcount, plugincount=plugincount))
        return
    if input_str:
        if input_str in CMD_LIST:
            string = "**{count} Commands found in plugin {input_str}:**\n\n"
            catcount = 0
            for i in CMD_LIST[input_str]:
                string += f"  •  `{i}`"
                string += "\n"
                catcount += 1
            await event.edit(string.format(count=catcount, input_str=input_str))
        else:
            await event.edit(input_str + " is not a valid plugin!")
    else:
        if Config.HELP_INLINETYPE is None:
            help_string = f"Userbot Helper.. Provided by [{DEFAULTUSER}]({USERNAME})\
                          \nUserbot Helper to reveal all the plugin names\
                          \n__Do__ `.help` __plugin_name for commands, in case popup doesn't appear.__\
                          \nDo `.info` plugin_name for usage"
            tgbotusername = Var.TG_BOT_USER_NAME_BF_HER
            results = await bot.inline_query(  # pylint:disable=E0602
                tgbotusername, help_string
            )
            await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
            await event.delete()
        else:
            string = f"**Userbot Helper.. Provided by {DEFAULTUSER}\nUserbot Helper to reveal all the plugin names\n\n**Do `.help` plugin_name for commands\nDo `.info` plugin_name for usage\n\n"
            for i in sorted(CMD_LIST):
                string += "◆```" + str(i)
                string += "```   "
            await event.edit(string)


@bot.on(admin_cmd(outgoing=True, pattern="info ?(.*)"))
@bot.on(sudo_cmd(pattern="info ?(.*)", allow_sudo=True))
async def info(event):
    """ For .info command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await edit_or_reply(event, str(CMD_HELP[args]))
        else:
            await edit_or_reply(event, "Please specify a valid plugin name.")
    else:
        string = "**Please specify which plugin do you want help for !!**\
            \n**Number of plugins : **`{count}`\
            \n**Usage:** `.info` <plugin name>\n\n"
        catcount = 0
        for i in sorted(CMD_HELP):
            string += "◆" + f"`{str(i)}`"
            string += "   "
            catcount += 1
        await edit_or_reply(event, string.format(count=catcount))


@bot.on(admin_cmd(pattern="dc"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    result = await bot(functions.help.GetNearestDcRequest())
    result = (
        result.stringify()
        + "\n\nList Of Telegram Data Centres:\
                                    \nDC1 : Miami FL, USA\
                                    \nDC2 : Amsterdam, NL\
                                    \nDC3 : Miami FL, USA\
                                    \nDC4 : Amsterdam, NL\
                                    \nDC5 : Singapore, SG\
                                    "
    )
    await event.edit(result)


@bot.on(sudo_cmd(allow_sudo=True, pattern="help(?: |$)(.*)"))
async def info(event):
    input_str = event.pattern_match.group(1)
    if input_str == "text":
        string = "Total {count} commands found in {plugincount} sudo plugins of catuserbot\n\n"
        catcount = 0
        plugincount = 0
        for i in sorted(SUDO_LIST):
            plugincount += 1
            string += f"{plugincount}) Command found in Plugin " + i + " are \n"
            for iter_list in SUDO_LIST[i]:
                string += "    " + str(iter_list)
                string += "\n"
                catcount += 1
            string += "\n"
        if len(string) > 4095:
            data = string.format(count=catcount, plugincount=plugincount)
            key = (
                requests.post(
                    "https://nekobin.com/api/documents", json={"content": data}
                )
                .json()
                .get("result")
                .get("key")
            )
            url = f"https://nekobin.com/{key}"
            reply_text = f"All commands of the catuserbot are [here]({url})"
            await event.reply(reply_text)
            return
        await event.reply(string.format(count=catcount, plugincount=plugincount))
        return
    if input_str:
        if input_str in SUDO_LIST:
            string = "**{count} Commands found in plugin {input_str}:**\n\n"
            catcount = 0
            for i in SUDO_LIST[input_str]:
                string += f"  •  `{i}`"
                string += "\n"
                catcount += 1
            await event.reply(string.format(count=catcount, input_str=input_str))
        else:
            await event.reply(input_str + " is not a valid plugin!")
    else:
        string = "**Please specify which plugin do you want help for !!**\
            \n**Number of plugins : **`{count}`\
            \n**Usage:** `.help` <plugin name>\n\n"
        catcount = 0
        for i in sorted(SUDO_LIST):
            string += "◆" + f"`{str(i)}`"
            string += "   "
            catcount += 1
        await event.reply(string.format(count=catcount))
