"""
By:- @Mrconfused & @sandy1709
idea from userage
"""
import io
import os
import os.path
import time
from os.path import exists, isdir

from userbot import CMD_HELP

from ..utils import admin_cmd, edit_or_reply, humanbytes, sudo_cmd
from . import runcmd


@borg.on(admin_cmd(pattern="ls ?(.*)"))
@borg.on(sudo_cmd(pattern="ls ?(.*)", allow_sudo=True))
async def lst(event):
    cat = event.pattern_match.group(1)
    if cat:
        path = cat
    else:
        path = os.getcwd()
    if not exists(path):
        await edit_or_reply(
            event,
            f"there is no such directory or file with the name `{cat}` check again",
        )
        return
    if isdir(path):
        if cat:
            msg = "Folders and Files in `{}` :\n".format(path)
            lists = os.listdir(path)
        else:
            msg = "Folders and Files in Current Directory :\n"
            lists = os.listdir(path)
        files = ""
        folders = ""
        for contents in sorted(lists):
            catpath = path + "/" + contents
            if not isdir(catpath):
                size = os.stat(catpath).st_size
                if contents.endswith((".mp3", ".flac", ".wav", ".m4a")):
                    files += "🎵" + f"`{contents}`\n"
                if contents.endswith((".opus")):
                    files += "🎙" + f"`{contents}`\n"
                elif contents.endswith(
                    (".mkv", ".mp4", ".webm", ".avi", ".mov", ".flv")
                ):
                    files += "🎞" + f"`{contents}`\n"
                elif contents.endswith((".zip", ".tar", ".tar.gz", ".rar")):
                    files += "🗜" + f"`{contents}`\n"
                elif contents.endswith(
                    (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".ico")
                ):
                    files += "🖼" + f"`{contents}`\n"
                else:
                    files += "📄" + f"`{contents}`\n"
            else:
                folders += f"📁`{contents}`\n"
        if files or folders:
            msg = msg + folders + files
        else:
            msg = msg + "__empty path__"
    else:
        size = os.stat(path).st_size
        msg = f"The details of given file :\n"
        if path.endswith((".mp3", ".flac", ".wav", ".m4a")):
            mode = "🎵"
        if path.endswith((".opus")):
            mode = "🎙"
        elif path.endswith((".mkv", ".mp4", ".webm", ".avi", ".mov", ".flv")):
            mode = "🎞"
        elif path.endswith((".zip", ".tar", ".tar.gz", ".rar")):
            mode = "🗜"
        elif path.endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp", ".ico")):
            mode = "🖼"
        else:
            mode = "📄"
        time.ctime(os.path.getctime(path))
        time2 = time.ctime(os.path.getmtime(path))
        time3 = time.ctime(os.path.getatime(path))
        msg += f"**Location :** `{path}`\n"
        msg += f"**icon :** `{mode}`\n"
        msg += f"**Size :** `{humanbytes(size)}`\n"
        msg += f"**Last Modified Time:** `{time2}`\n"
        msg += f"**Last Accessed Time:** `{time3}`"
    if len(msg) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(msg)) as out_file:
            out_file.name = "ls.txt"
            await borg.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=path,
            )
            await event.delete()
    else:
        await edit_or_reply(event, msg)


@borg.on(admin_cmd(pattern="rem ?(.*)"))
@borg.on(sudo_cmd(pattern="rem ?(.*)", allow_sudo=True))
async def lst(event):
    cat = event.pattern_match.group(1)
    if cat:
        path = cat
    else:
        await edit_or_reply(event, "what should i delete")
        return
    if not exists(path):
        await edit_or_reply(
            event,
            f"there is no such directory or file with the name `{cat}` check again",
        )
        return
    catcmd = f"rm -rf {path}"
    if isdir(path):
        await runcmd(catcmd)
        await edit_or_reply(event, f"Succesfully removed `{path}` directory")
    else:
        await runcmd(catcmd)
        await edit_or_reply(event, f"Succesfully removed `{path}` file")


CMD_HELP.update(
    {
        "filemanager": "__**PLUGIN NAME :** File Manager__\
     \n\n📌** CMD ➥** `.ls`\
     \n**USAGE   ➥  **Will return files from current working directory\
     \n\n📌** CMD ➥** `.ls` path\
     \n**USAGE   ➥  **Will return output according to path  \
     \n\n📌** CMD ➥** `.ls` file path\
     \n**USAGE   ➥  **Will return file details\
     \n\n📌** CMD ➥** `.rem` path\
     \n**USAGE   ➥  **To delete the required item from the bot server\
     \n\nSimple Module for people who dont wanna use shell executor for listing files."
    }
)
