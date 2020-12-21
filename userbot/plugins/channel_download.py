"""
Telegram Channel Media Downloader Plugin for userbot.
usage: .geta channel_username [will  get all media from channel, tho there is limit of 3000 there to prevent API limits.]
       .getc number_of_messsages channel_username
By: @Zero_cool7870
"""
import os
import subprocess

location = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "temp")


@bot.on(admin_cmd(pattern=r"getc(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="getc(?: |$)(.*)", allow_sudo=True))
async def get_media(event):
    if event.fwd_from:
        return
    tempdir = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "temp")
    try:
        os.makedirs(tempdir)
    except BaseException:
        pass
    catty = event.pattern_match.group(1)
    limit = int(catty.split(" ")[0])
    channel_username = str(catty.split(" ")[1])
    event = await edit_or_reply(event, "Downloading Media From this Channel.")
    msgs = await event.client.get_messages(channel_username, limit=int(limit))
    with open("log.txt", "w") as f:
        f.write(str(msgs))
    i = 0
    for msg in msgs:
        if msg.media is not None:
            await event.client.download_media(msg, tempdir)
            i += 1
            await event.edit(
                f"Downloading Media From this Channel.\n **DOWNLOADED : **`{i}`"
            )
    ps = subprocess.Popen(("ls", tempdir), stdout=subprocess.PIPE)
    output = subprocess.check_output(("wc", "-l"), stdin=ps.stdout)
    ps.wait()
    output = str(output)
    output = output.replace("b'", " ")
    output = output.replace("\\n'", " ")
    await event.edit(f"Successfully downloaded {output} number of media files")


@bot.on(admin_cmd(pattern="geta(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="geta(?: |$)(.*)", allow_sudo=True))
async def get_media(event):
    if event.fwd_from:
        return
    tempdir = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "temp")
    try:
        os.makedirs(tempdir)
    except BaseException:
        pass
    channel_username = event.pattern_match.group(1)
    event = await edit_or_reply(event, "Downloading All Media From this Channel.")
    msgs = await event.client.get_messages(channel_username, limit=3000)
    with open("log.txt", "w") as f:
        f.write(str(msgs))
    i = 0
    for msg in msgs:
        if msg.media is not None:
            await event.client.download_media(msg, tempdir)
            i += 1
            await event.edit(
                f"Downloading Media From this Channel.\n **DOWNLOADED : **`{i}`"
            )
    ps = subprocess.Popen(("ls", tempdir), stdout=subprocess.PIPE)
    output = subprocess.check_output(("wc", "-l"), stdin=ps.stdout)
    ps.wait()
    output = str(output)
    output = output.replace("b'", "")
    output = output.replace("\\n'", "")
    await event.edit(f"Successfully downloaded {output} number of media files")


CMD_HELP.update(
    {
        "channel_download": "__**PLUGIN NAME :** Channel Download__\
\n\n📌** CMD ➥** `.geta` <channel_username>\
\n**USAGE   ➥  **Will  get all media from channel, though there is limit of 3000 there to prevent API limits.\
\n\n📌** CMD ➥** `.getc` <number_of_messsages channel_username>\
\n**USAGE   ➥  **Will  get that number of media from channel"
    }
)
