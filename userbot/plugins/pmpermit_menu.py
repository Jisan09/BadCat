"""
Support chatbox for pmpermit.
Used by incoming messages with trigger as /start
Will not work for already approved people.
Credits: written by ༺αиυвιѕ༻ {@A_Dark_Princ3}
"""
import asyncio
import io 
import telethon.sync
from telethon.tl.functions.users import GetFullUserRequest
import userbot.plugins.sql_helper.pmpermit_sql as pmpermit_sql
from telethon import events, errors, functions, types
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"
PREV_REPLY_MESSAGE = {}

@command(pattern=r"\/start", incoming=True)
async def _(event):
    chat_id = event.from_id
    userid = event.sender_id
    if not pmpermit_sql.is_approved(chat_id):
        chat = await event.get_chat()
        if event.fwd_from:
            return
        if not event.is_private:
            return
        PM = ("`Ciao. Stai per accedere al menu di,`"
               f"{DEFAULTUSER}.\n"
               "__Muoviti a dire perché sei qui 🤔...__\n"
               "*Scegli uno dei seguenti motivi:**\n\n"
               "`a`. Per parlare con me. 💬\n"
               "`b`. Per essere aiutato. 🌺\n"
               "`c`. Per chiedere qualcosa. 🌸\n"
               "`d`. Per richiedere qualcosa. 🌻\n")
        ONE = ("__Okay, la tua richiesta è stata registrata, non spammare in chat. Aspetta la mia risposta minimo tra 24 anni luce.Forse è impegnata a differenza di te.__\n\n"
                "**🥳 Verrai bloccato se continuerai ad inviare messaggi. 🥳**\n\n"
                "__Use__ `/start` __Per tornare al menu principale. 🤍__")
        TWO = (" `███████▄▄███████████▄  \n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓███░░░░░░░░░░░░█\n██████▀▀▀█░░░░██████▀  \n░░░░░░░░░█░░░░█  \n░░░░░░░░░░█░░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░░▀▀ `\n\n**So uncool, this is not your home. Go bother someone else. You have been blocked and reported until further notice.**")
        FOUR = ("__Okay. My master has not seen your message yet.He usually responds to people,though idk about retarted ones.__\n __He'll respond when he comes back, if he wants to.There's already a lot of pending messages😶__\n **Please do not spam unless you wish to be blocked and reported.**")
        FIVE = ("`Okay. please have the basic manners as to not bother my master too much. If he wishes to help you, he will respond to you soon.`\n**Do not ask repeatdly else you will be blocked and reported.**")
        LWARN = ("**This is your last warning. DO NOT send another message else you will be blocked and reported. Keep patience. My master will respond you ASAP.**\n__Use__ `/start` __to go back to the main menu.__")
     
        async with borg.conversation(chat) as conv:
         if pmpermit_sql.is_approved(chat_id):
            return
         await borg.send_message(chat, PM)
         chat_id = event.from_id
         response = await conv.get_response(chat)
         y = response.text
         if y == "a":
             if pmpermit_sql.is_approved(chat_id):
                return
             await borg.send_message(chat, ONE)
             response = await conv.get_response(chat)
             await event.delete()
             if not response.text == "/start":
                 await response.delete()
                 if pmpermit_sql.is_approved(chat_id):
                    return
                 await borg.send_message(chat, LWARN)
                 response = await conv.get_response(chat)
                 await event.delete()
                 await response.delete()
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     if pmpermit_sql.is_approved(chat_id):
                            return
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         elif y == "b":
             if pmpermit_sql.is_approved(chat_id):
                    return
             await borg.send_message(chat, LWARN)
             response = await conv.get_response(chat)
             if not response.text == "/start":
                 if pmpermit_sql.is_approved(chat_id):
                        return
                 await borg.send_message(chat, TWO)
                 await asyncio.sleep(3)
                 await event.client(functions.contacts.BlockRequest(chat_id))
         elif y == "c":
             if pmpermit_sql.is_approved(chat_id):
                    return
             await borg.send_message(chat, FOUR)
             response = await conv.get_response(chat)
             await event.delete()
             await response.delete()
             if not response.text == "/start":
                 if pmpermit_sql.is_approved(chat_id):
                    return
                 await borg.send_message(chat, LWARN)
                 await event.delete()
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     if pmpermit_sql.is_approved(chat_id):
                            return
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         elif y == "d":
             if pmpermit_sql.is_approved(chat_id):
                    return
             await borg.send_message(chat,FIVE)
             response = await conv.get_response(chat)
             if not response.text == "/start":
                 if pmpermit_sql.is_approved(chat_id):
                        return
                 await borg.send_message(chat, LWARN)
                 response = await conv.get_response(chat)
                 if not response.text == "/start":
                     if pmpermit_sql.is_approved(chat_id):
                            return
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
         else:
             if pmpermit_sql.is_approved(chat_id):
                    return
             await borg.send_message(chat, "`You have entered an invalid command. Please send /start again or do not send another message if you do not wish to be blocked and reported.`")
             response = await conv.get_response(chat)
             z = response.text
             if not z == "/start":
                 if pmpermit_sql.is_approved(chat_id):
                    return
                 await borg.send_message(chat, LWARN)
                 await conv.get_response(chat)
                 if not response.text == "/start":
                     if pmpermit_sql.is_approved(chat_id):
                        return
                     await borg.send_message(chat, TWO)
                     await asyncio.sleep(3)
                     await event.client(functions.contacts.BlockRequest(chat_id))
