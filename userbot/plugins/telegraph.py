"""@telegraph Utilities
Available Commands:
.telegraph media as reply to a media
.telegraph text as reply to a large text"""
import os
from datetime import datetime

from PIL import Image
from telegraph import Telegraph, exceptions, upload_file

from userbot import ALIVE_NAME
from userbot.utils import admin_cmd, sudo_cmd

telegraph = Telegraph()
r = telegraph.create_account(short_name=Config.TELEGRAPH_SHORT_NAME)
auth_url = r["auth_url"]


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"
USERNAME = str(Config.LIVE_USERNAME) if Config.LIVE_USERNAME else "@Jisan7509"


@borg.on(admin_cmd(pattern="telegraph (media|text) ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if Config.PRIVATE_GROUP_BOT_API_ID is None:
        await event.edit(
            "Please set the required environment variable `PRIVATE_GROUP_BOT_API_ID` for this plugin to work"
        )
        return
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    await borg.send_message(
        Config.PRIVATE_GROUP_BOT_API_ID,
        "Created New Telegraph account {} for the current session. \n**Do not give this url to anyone, even if they say they are from Telegram!**".format(
            auth_url
        ),
    )
    optional_title = event.pattern_match.group(2)
    if event.reply_to_msg_id:
        start = datetime.now()
        r_message = await event.get_reply_message()
        input_str = event.pattern_match.group(1)
        if input_str == "media":
            downloaded_file_name = await borg.download_media(
                r_message, Config.TMP_DOWNLOAD_DIRECTORY
            )
            end = datetime.now()
            ms = (end - start).seconds
            await event.edit(
                "Downloaded to {} in {} seconds.".format(downloaded_file_name, ms)
            )
            if downloaded_file_name.endswith((".webp")):
                resize_image(downloaded_file_name)
            try:
                start = datetime.now()
                media_urls = upload_file(downloaded_file_name)
                jisan = "https://telegra.ph{}".format(media_urls[0])
            except exceptions.TelegraphException as exc:
                await event.edit("ERROR: " + str(exc))
                os.remove(downloaded_file_name)
            else:
                end = datetime.now()
                ms_two = (end - start).seconds
                os.remove(downloaded_file_name)
                await event.edit(
                    f"__**➥ Uploaded to :-**__ **[Telegraph]**({jisan})\n__**➥ Uploaded in {ms + ms_two} seconds .**__\n__**➥ Uploaded by :-**__ [{DEFAULTUSER}]({USERNAME})",
                    link_preview=True,
                )
        elif input_str == "text":
            user_object = await borg.get_entity(r_message.from_id)
            title_of_page = user_object.first_name  # + " " + user_object.last_name
            # apparently, all Users do not have last_name field
            if optional_title:
                title_of_page = optional_title
            page_content = r_message.message
            if r_message.media:
                if page_content != "":
                    title_of_page = page_content
                downloaded_file_name = await borg.download_media(
                    r_message, Config.TMP_DOWNLOAD_DIRECTORY
                )
                m_list = None
                with open(downloaded_file_name, "rb") as fd:
                    m_list = fd.readlines()
                for m in m_list:
                    page_content += m.decode("UTF-8") + "\n"
                os.remove(downloaded_file_name)
            page_content = page_content.replace("\n", "<br>")
            response = telegraph.create_page(title_of_page, html_content=page_content)
            kakashi = "https://telegra.ph/{}".format(response["path"])
            end = datetime.now()
            ms = (end - start).seconds
            await event.edit(
                f"__**➥ Pasted to :-**__ **[Telegraph]**({kakashi})\n__**➥ Pasted in {ms} seconds .**__",
                link_preview=True,
            )
    else:
        await event.edit(
            "Reply to a message to get a permanent telegra.ph link. (Inspired by @ControllerBot)"
        )


@borg.on(sudo_cmd(pattern="telegraph (media|text) ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if Config.PRIVATE_GROUP_BOT_API_ID is None:
        await event.edit(
            "Please set the required environment variable `PRIVATE_GROUP_BOT_API_ID` for this plugin to work"
        )
        return
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    await borg.send_message(
        Config.PRIVATE_GROUP_BOT_API_ID,
        "Created New Telegraph account {} for the current session. \n**Do not give this url to anyone, even if they say they are from Telegram!**".format(
            auth_url
        ),
    )
    optional_title = event.pattern_match.group(2)
    if event.reply_to_msg_id:
        start = datetime.now()
        r_message = await event.get_reply_message()
        input_str = event.pattern_match.group(1)
        if input_str == "media":
            downloaded_file_name = await borg.download_media(
                r_message, Config.TMP_DOWNLOAD_DIRECTORY
            )
            end = datetime.now()
            ms = (end - start).seconds
            await event.edit(
                "Downloaded to {} in {} seconds.".format(downloaded_file_name, ms)
            )
            if downloaded_file_name.endswith((".webp")):
                resize_image(downloaded_file_name)
            try:
                start = datetime.now()
                media_urls = upload_file(downloaded_file_name)
                jisan = "https://telegra.ph{}".format(media_urls[0])
            except exceptions.TelegraphException as exc:
                await event.edit("ERROR: " + str(exc))
                os.remove(downloaded_file_name)
            else:
                end = datetime.now()
                ms_two = (end - start).seconds
                os.remove(downloaded_file_name)
                await event.reply(
                    f"__**➥ Uploaded to :-**__ **[Telegraph]**({jisan})\n__**➥ Uploaded in {ms + ms_two} seconds .**__\n__**➥ Uploaded by :-**__ [{DEFAULTUSER}]({USERNAME})",
                    link_preview=True,
                )
        elif input_str == "text":
            user_object = await borg.get_entity(r_message.from_id)
            title_of_page = user_object.first_name  # + " " + user_object.last_name
            # apparently, all Users do not have last_name field
            if optional_title:
                title_of_page = optional_title
            page_content = r_message.message
            if r_message.media:
                if page_content != "":
                    title_of_page = page_content
                downloaded_file_name = await borg.download_media(
                    r_message, Config.TMP_DOWNLOAD_DIRECTORY
                )
                m_list = None
                with open(downloaded_file_name, "rb") as fd:
                    m_list = fd.readlines()
                for m in m_list:
                    page_content += m.decode("UTF-8") + "\n"
                os.remove(downloaded_file_name)
            page_content = page_content.replace("\n", "<br>")
            response = telegraph.create_page(title_of_page, html_content=page_content)
            kakashi = "https://telegra.ph/{}".format(response["path"])
            end = datetime.now()
            ms = (end - start).seconds
            await event.reply(
                f"__**➥ Pasted to :-**__ **[Telegraph]**({kakashi})\n__**➥ Pasted in {ms} seconds .**__",
                link_preview=True,
            )
    else:
        await event.reply(
            "Reply to a message to get a permanent telegra.ph link. (Inspired by @ControllerBot)"
        )


def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")
