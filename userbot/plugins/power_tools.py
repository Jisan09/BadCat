"""Restart or Terminate the bot from any chat
Available Commands:
.restart
.shutdown"""
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html
import os
import sys
from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern="restart"))
async def _(event):
    if event.fwd_from:
        return
    # await asyncio.sleep(2)
    # await event.edit("Restarting [██░] ...\n`.ping` me or `.help` to check if I am online after a lil bit.")
    # await asyncio.sleep(2)
    # await event.edit("Restarting [███]...\n`.ping` me or `.help` to check if I am online after a lil bit.")
    # await asyncio.sleep(2)
    await event.edit("Restarted. `.ping` me or `.help` to check if I am online, actually it takes 1-2 min for restarting")
    await borg.disconnect()
    # https://archive.is/im3rt
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()


@borg.on(admin_cmd(pattern="shutdown"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Turning off ...Manually turn me on later")
    await borg.disconnect()
