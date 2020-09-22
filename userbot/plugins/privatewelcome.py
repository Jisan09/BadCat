from telethon import events

from userbot.plugins.sql_helper.welcomesql import (
    addwelcome_setting,
    getcurrent_welcome_settings,
    rmwelcome_setting,
)

from .. import CMD_HELP, bot
from ..utils import admin_cmd, edit_or_reply, sudo_cmd

if Config.PRIVATE_GROUP_BOT_API_ID is None:
    BOTLOG = False
else:
    BOTLOG = True
    BOTLOG_CHATID = Config.PRIVATE_GROUP_BOT_API_ID


@bot.on(events.ChatAction)
async def _(event):
    cws = getcurrent_welcome_settings(event.chat_id)
    if (
        cws
        and (event.user_joined or event.user_added)
        and not (await event.get_user()).bot
    ):
        a_user = await event.get_user()
        chat = await event.get_chat()
        me = await bot.get_me()
        title = chat.title if chat.title else "this chat"
        participants = await bot.get_participants(chat)
        count = len(participants)
        mention = "<a href='tg://user?id={}'>{}</a>".format(
            a_user.id, a_user.first_name
        )
        my_mention = "<a href='tg://user?id={}'>{}</a>".format(me.id, me.first_name)
        first = a_user.first_name
        last = a_user.last_name
        fullname = f"{first} {last}" if last else first
        username = f"@{a_user.username}" if a_user.username else mention
        userid = a_user.id
        my_first = me.first_name
        my_last = me.last_name
        my_fullname = f"{my_first} {my_last}" if my_last else my_first
        my_username = f"@{me.username}" if me.username else my_mention
        file_media = None
        current_saved_welcome_message = None
        if cws:
            if cws.f_mesg_id:
                msg_o = await event.client.get_messages(
                    entity=BOTLOG_CHATID, ids=int(cws.f_mesg_id)
                )
                file_media = msg_o.media
                current_saved_welcome_message = msg_o.message
            elif cws.reply:
                current_saved_welcome_message = cws.reply
        current_message = await event.client.send_message(
            userid,
            current_saved_welcome_message.format(
                mention=mention,
                title=title,
                count=count,
                first=first,
                last=last,
                fullname=fullname,
                username=username,
                userid=userid,
                my_first=my_first,
                my_last=my_last,
                my_fullname=my_fullname,
                my_username=my_username,
                my_mention=my_mention,
            ),
            file=file_media,
            parse_mode="html",
        )


@borg.on(admin_cmd(pattern=r"savepwel ?(.*)"))
@borg.on(sudo_cmd(pattern=r"savepwel ?(.*)", allow_sudo=True))
async def save_welcome(event):
    msg = await event.get_reply_message()
    string = "".join(event.text.split(maxsplit=1)[1:])
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG_CHATID:
            await bot.send_message(
                BOTLOG_CHATID,
                f"#WELCOME_NOTE\
                \nCHAT ID: {event.chat_id}\
                \nThe following message is saved as the welcome note for the {event.chat.title}, Dont delete this message !!",
            )
            msg_o = await event.client.forward_messages(
                entity=BOTLOG_CHATID, messages=msg, from_peer=event.chat_id, silent=True
            )
            msg_id = msg_o.id
        else:
            await edit_or_reply(
                event,
                "`Saving media as part of the welcome note requires the BOTLOG_CHATID to be set.`",
            )
            return
    elif event.reply_to_msg_id and not string:
        rep_msg = await event.get_reply_message()
        string = rep_msg.text
    success = "`Welcome note {} for this chat.`"
    if addwelcome_setting(event.chat_id, 0, string, msg_id) is True:
        return await edit_or_reply(event, success.format("saved"))
    rmwelcome_setting(event.chat_id)
    if addwelcome_setting(event.chat_id, 0, string, msg_id) is True:
        return await edit_or_reply(event, success.format("updated"))
    await edit_or_reply("Error while setting welcome in this group")


@borg.on(admin_cmd(pattern="clearpwel$"))
@borg.on(sudo_cmd(pattern="clearpwel$", allow_sudo=True))
async def del_welcome(event):
    if rmwelcome_setting(event.chat_id) is True:
        await edit_or_reply(event, "`Welcome note deleted for this chat.`")
    else:
        await edit_or_reply(event, "`Do I have a welcome note here ?`")


@borg.on(admin_cmd(pattern="listpwel$"))
@borg.on(sudo_cmd(pattern="listpwel$", allow_sudo=True))
async def show_welcome(event):
    cws = getcurrent_welcome_settings(event.chat_id)
    if not cws:
        await edit_or_reply(event, "`No pwelcome message saved here.`")
        return
    elif cws.f_mesg_id:
        msg_o = await bot.get_messages(entity=BOTLOG_CHATID, ids=int(cws.f_mesg_id))
        await edit_or_reply(
            event, "`I am currently pwelcoming new users with this welcome note.`"
        )
        await event.reply(msg_o.message, file=msg_o.media)
    elif cws.reply:
        await edit_or_reply(
            event, "`I am currently pwelcoming new users with this welcome note.`"
        )
        await event.reply(cws.reply)


CMD_HELP.update(
    {
        "privatewelcome": "__**PLUGIN NAME :** Privatewelcome__\
\n\n📌** CMD ➥** `.savepwel` <welcome message> or reply to a message with .setwelcome\
\n**USAGE   ➥  **Saves the message as a welcome note in the chat.\
\n\nAvailable variables for formatting welcome messages :\
\n`{mention}`, `{title}`, `{count}`, `{first}`, `{last}`, `{fullname}`, `{userid}`, `{username}`, `{my_first}`, `{my_fullname}`, `{my_last}`, `{my_mention}`, `{my_username}`\
\n\n📌** CMD ➥** `.listpwel`\
\n**USAGE   ➥  **Check whether you have a welcome note in the chat.\
\n\n📌** CMD ➥** `.clearpwel`\
\n**USAGE   ➥  **Deletes the welcome note for the current chat.\
"
    }
)
