#    Copyright (C) 2020  sandeep.n(π.$)
# baning spmmers plugin for catuserbot by @sandy1709 and @mrconfused
# included both cas(combot antispam service) and spamwatch (need to add more feaututres)


from requests import get
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins

from ..utils import is_admin
from . import BOTLOG, BOTLOG_CHATID, LOGS, spamwatch
from .sql_helper.gban_sql_helper import get_gbanuser, is_gbanned

if Config.ANTISPAMBOT_BAN:

    @bot.on(events.ChatAction())
    async def anti_spambot(event):
        if not event.user_joined and not event.user_added:
            return
        chat = event.chat_id
        user = await event.get_user()
        catadmin = await is_admin(bot, chat, bot.uid)
        if not catadmin:
            return
        catbanned = None
        adder = None
        ignore = None
        if event.user_added:
            try:
                adder = event.action_message.from_id
            except AttributeError:
                return
        async for admin in event.client.iter_participants(
            event.chat_id, filter=ChannelParticipantsAdmins
        ):
            if admin.id == adder:
                ignore = True
                break
        if ignore:
            return
        if is_gbanned(user.id):
            catgban = get_gbanuser(user.id)
            if catgban.reason:
                hmm = await event.reply(
                    f"[{user.first_name}](tg://user?id={user.id}) was gbanned by you For the reason `{catgban.reason}`"
                )
            else:
                hmm = await event.reply(
                    f"[{user.first_name}](tg://user?id={user.id}) was gbanned by you"
                )
            try:
                await bot.edit_permissions(chat, user.id, view_messages=False)
                catbanned = True
            except Exception as e:
                LOGS.info(e)
        if spamwatch and not catbanned:
            ban = spamwatch.get_ban(user.id)
            if ban:
                hmm = await event.reply(
                    f"[{user.first_name}](tg://user?id={user.id}) was banned by spamwatch For the reason `{ban.reason}`"
                )
                try:
                    await bot.edit_permissions(chat, user.id, view_messages=False)
                    catbanned = True
                except Exception as e:
                    LOGS.info(e)
        if not catbanned:
            try:
                casurl = "https://api.cas.chat/check?user_id={}".format(user.id)
                data = get(casurl).json()
            except Exception as e:
                LOGS.info(e)
                data = None
            if data and data["ok"]:
                reason = (
                    f"[Banned by Combot Anti Spam](https://cas.chat/query?u={user.id})"
                )
                hmm = await event.reply(
                    f"[{user.first_name}](tg://user?id={user.id}) was banned by Combat anti-spam service(CAS) For the reason check {reason}"
                )
                try:
                    await bot.edit_permissions(chat, user.id, view_messages=False)
                    catbanned = True
                except Exception as e:
                    LOGS.info(e)
        if BOTLOG and catbanned:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#ANTISPAMBOT\n"
                f"**User :** [{user.first_name}](tg://user?id={user.id})\n"
                f"**Chat :** {event.chat.title} (`{event.chat_id}`)\n"
                f"**Reason :** {hmm.text}",
            )
