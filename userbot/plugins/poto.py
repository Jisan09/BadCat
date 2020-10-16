#    Friendly Telegram (telegram userbot)
#    Copyright (C) 2018-2019 The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
----------------------------------------------------------------
All Thenks goes to Emily ( The creater of This Plugin)
\nSome credits goes to me ( @kirito6969 ) for ported this plugin
\nand `SnapDragon for` Helping me.
----------------------------------------------------------------
Type `.poto` for get **All profile pics of that User**
\nOr type `.poto (number)` to get the **desired number of photo of a User** .
"""

import asyncio

from ..utils import admin_cmd, edit_or_reply, sudo_cmd

name = "Profile Photos"


@bot.on(admin_cmd(pattern="poto ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="poto ?(.*)", allow_sudo=True))
async def potocmd(event):
    """Gets the profile photos of replied users, channels or chats"""
    uid = "".join(event.raw_text.split(maxsplit=1)[1:])
    user = await event.get_reply_message()
    chat = event.input_chat
    if user:
        photos = await event.client.get_profile_photos(user.sender)
        u = True
    else:
        photos = await event.client.get_profile_photos(chat)
        u = False
    if uid.strip() == "":
        uid = 1
        if int(uid) <= (len(photos)):
            send_photos = await event.client.download_media(photos[uid - 1])
            await event.client.send_file(event.chat_id, send_photos)
        else:
            await edit_or_reply(
                event, "No photo found of this NIBBA / NIBBI. Now u Die!"
            )
            await asyncio.sleep(2)
            return
    elif uid.strip() == "all":
        if len(photos) > 0:
            await event.client.send_file(event.chat_id, photos)
        else:
            try:
                if u is True:
                    photo = await event.client.download_profile_photo(user.sender)
                else:
                    photo = await event.client.download_profile_photo(event.input_chat)
                await event.client.send_file(event.chat_id, photo)
            except a:
                await edit_or_reply(event, "**This user has no photos!**")
                return
    else:
        try:
            uid = int(uid)
            if uid <= 0:
                await edit_or_reply(
                    event, "```number Invalid!``` **Are you Comedy Me ?**"
                )
                return
        except BaseException:
            await edit_or_reply(event, "Are you comedy me ?")
            return
        if int(uid) <= (len(photos)):
            send_photos = await event.client.download_media(photos[uid - 1])
            await event.client.send_file(event.chat_id, send_photos)
        else:
            await edit_or_reply(
                event, "No photo found of this NIBBA / NIBBI. Now u Die!"
            )
            await asyncio.sleep(2)
            return
