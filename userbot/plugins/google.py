# reverse search and google search  plugin for cat
import os
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from googlesearch import search

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import BOTLOG, BOTLOG_CHATID, CMD_HELP


@borg.on(admin_cmd(outgoing=True, pattern=r"gs(?: |$)(\d*)? ?(.*)"))
@borg.on(sudo_cmd(allow_sudo=True, pattern=r"gs(?: |$)(\d*)? ?(.*)"))
async def gsearch(event):
    if event.is_reply and not event.pattern_match.group(2):
        query = await event.get_reply_message()
        query = str(query.message)
    else:
        query = str(event.pattern_match.group(2))
    if not query:
        return await edit_or_reply(
            event, "Reply to a message or pass a query to search!"
        )
    catevent = await edit_or_reply(event, "`Processing...`")
    if event.pattern_match.group(1) != "":
        lim = int(event.pattern_match.group(1))
        if lim > 20:
            lim = int(20)
        if lim <= 0:
            lim = int(1)
    else:
        lim = int(10)
    catresult = ""
    for url in search(query, stop=lim):
        a = google_scrape(url)
        catresult += f"👉[{a}]({url})\n\n"
    await catevent.edit(
        "**Search Query:**\n`" + query + "`\n\n**Results:**\n" + catresult,
        link_preview=False,
    )
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "Google Search query `" + query + "` was executed successfully",
        )


"""@borg.on(admin_cmd(outgoing=True, pattern=r"gs (.*)"))
async def gsearch(q_event):
    match = q_event.pattern_match.group(1)
    page = findall(r"page=\d+", match)
    try:
        page = page[0]
        page = page.replace("page=", "")
        match = match.replace("page=" + page[0], "")
    except IndexError:
        page = 1
    search_args = (str(match), int(page))
    gsearch = GoogleSearch()
    gresults = await gsearch.async_search(*search_args)
    msg = ""
    for i in range(len(gresults["links"])):
        try:
            title = gresults["titles"][i]
            link = gresults["links"][i]
            desc = gresults["descriptions"][i]
            msg += f"👉[{title}]({link})\n`{desc}`\n\n"
        except IndexError:
            break
    await q_event.edit(
        "**Search Query:**\n`" + match + "`\n\n**Results:**\n" + msg, link_preview=False
    )
    if BOTLOG:
        await q_event.client.send_message(
            BOTLOG_CHATID,
            "Google Search query `" + match + "` was executed successfully",
        )"""


@borg.on(admin_cmd(pattern="grs$"))
@borg.on(sudo_cmd(pattern="grs$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    OUTPUT_STR = "Reply to an image to do Google Reverse Search"
    if event.reply_to_msg_id:
        catevent = await edit_or_reply(event, "Pre Processing Media")
        previous_message = await event.get_reply_message()
        previous_message_text = previous_message.message
        BASE_URL = "http://www.google.com"
        if previous_message.media:
            downloaded_file_name = await borg.download_media(
                previous_message, Config.TMP_DOWNLOAD_DIRECTORY
            )
            SEARCH_URL = "{}/searchbyimage/upload".format(BASE_URL)
            multipart = {
                "encoded_image": (
                    downloaded_file_name,
                    open(downloaded_file_name, "rb"),
                ),
                "image_content": "",
            }
            # https://stackoverflow.com/a/28792943/4723940
            google_rs_response = requests.post(
                SEARCH_URL, files=multipart, allow_redirects=False
            )
            the_location = google_rs_response.headers.get("Location")
            os.remove(downloaded_file_name)
        else:
            previous_message_text = previous_message.message
            SEARCH_URL = "{}/searchbyimage?image_url={}"
            request_url = SEARCH_URL.format(BASE_URL, previous_message_text)
            google_rs_response = requests.get(request_url, allow_redirects=False)
            the_location = google_rs_response.headers.get("Location")
        await catevent.edit("Found Google Result. Pouring some soup on it!")
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"
        }
        response = requests.get(the_location, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        # document.getElementsByClassName("r5a77d"): PRS
        prs_div = soup.find_all("div", {"class": "r5a77d"})[0]
        prs_anchor_element = prs_div.find("a")
        prs_url = BASE_URL + prs_anchor_element.get("href")
        prs_text = prs_anchor_element.text
        # document.getElementById("jHnbRc")
        img_size_div = soup.find(id="jHnbRc")
        img_size = img_size_div.find_all("div")
        end = datetime.now()
        ms = (end - start).seconds
        OUTPUT_STR = """{img_size}
<b>Possible Related Search : </b> <a href="{prs_url}">{prs_text}</a>
<b>More Info : </b> Open this <a href="{the_location}">Link</a> in {ms} seconds""".format(
            **locals()
        )
    await catevent.edit(OUTPUT_STR, parse_mode="HTML", link_preview=False)


def google_scrape(url):
    thepage = (requests.get(url)).text
    soup = BeautifulSoup(thepage, "html.parser")
    return soup.title.text


CMD_HELP.update(
    {
        "google": "__**PLUGIN NAME :** Google\
        \n\n📌** CMD ➥** `.gs` <limit> <query>` or `.gs <limit> (replied message)`\
        \n**USAGE   ➥  **Will google  search and sends you top 10 results links.\
        \n\n📌** CMD ➥** `.grs` reply to image\
        \n**USAGE   ➥  **Will google reverse search the image and shows you the result.\
        "
    }
)
