"""
`Credits` @amnd33p
Modified by @mrconfused
"""
import io
import traceback
from datetime import datetime

import requests
from selenium import webdriver
from validators.url import url

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import CMD_HELP


@borg.on(admin_cmd(pattern="ss (.*)"))
@borg.on(sudo_cmd(pattern="ss (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if Config.CHROME_BIN is None:
        await edit_or_reply(event, "Need to install Google Chrome. Module Stopping.")
        return
    catevent = await edit_or_reply(event, "`Processing ...`")
    start = datetime.now()
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--test-type")
        chrome_options.add_argument("--headless")
        # https://stackoverflow.com/a/53073789/4723940
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.binary_location = Config.CHROME_BIN
        await event.edit("Starting Google Chrome BIN")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        input_str = event.pattern_match.group(1)
        caturl = url(input_str)
        if not caturl:
            await catevent.edit(
                "the url must be in the format `https://www.google.com`"
            )
            return
        driver.get(input_str)
        await catevent.edit("Calculating Page Dimensions")
        height = driver.execute_script(
            "return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);"
        )
        width = driver.execute_script(
            "return Math.max(document.body.scrollWidth, document.body.offsetWidth, document.documentElement.clientWidth, document.documentElement.scrollWidth, document.documentElement.offsetWidth);"
        )
        driver.set_window_size(width + 100, height + 100)
        # Add some pixels on top of the calculated dimensions
        # for good measure to make the scroll bars disappear
        im_png = driver.get_screenshot_as_png()
        # saves screenshot of entire page
        await catevent.edit("Stoppping Chrome Bin")
        driver.close()
        message_id = None
        if event.reply_to_msg_id:
            message_id = event.reply_to_msg_id
        end = datetime.now()
        ms = (end - start).seconds
        hmm = f"**url : **{input_str} \n**Time :** `{ms} seconds`"
        await catevent.delete()
        with io.BytesIO(im_png) as out_file:
            out_file.name = input_str + ".PNG"
            await event.client.send_file(
                event.chat_id,
                out_file,
                caption=hmm,
                force_document=True,
                reply_to=message_id,
                allow_cache=False,
                silent=True,
            )
    except Exception:
        await catevent.edit(traceback.format_exc())


@borg.on(admin_cmd(pattern="scapture (.*)"))
@borg.on(sudo_cmd(pattern="scapture (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    if Config.SCREEN_SHOT_LAYER_ACCESS_KEY is None:
        await edit_or_reply(
            event,
            "Need to get an API key from https://screenshotlayer.com/product \nModule stopping!",
        )
        return
    catevent = await edit_or_reply(event, "Processing ...")
    sample_url = "https://api.screenshotlayer.com/api/capture?access_key={}&url={}&fullpage={}&viewport={}&format={}&force={}"
    input_str = event.pattern_match.group(1)
    caturl = url(input_str)
    if not caturl:
        await catevent.edit("the url must be in the format `https://www.google.com`")
        return
    response_api = requests.get(
        sample_url.format(
            Config.SCREEN_SHOT_LAYER_ACCESS_KEY, input_str, "1", "2560x1440", "PNG", "1"
        )
    )
    # https://stackoverflow.com/a/23718458/4723940
    contentType = response_api.headers["content-type"]
    end = datetime.now()
    ms = (end - start).seconds
    hmm = f"**url : **{input_str} \n**Time :** `{ms} seconds`"
    if "image" in contentType:
        with io.BytesIO(response_api.content) as screenshot_image:
            screenshot_image.name = "screencapture.png"
            try:
                await event.client.send_file(
                    event.chat_id,
                    screenshot_image,
                    caption=hmm,
                    force_document=True,
                    reply_to=event.message.reply_to_msg_id,
                )
                await catevent.delete()
            except Exception as e:
                await catevent.edit(str(e))
    else:
        await catevent.edit(response_api.text)


CMD_HELP.update(
    {
        "screenshot": "__**PLUGIN NAME :** Screenshot__\
    \n\n📌** CMD ➥** `.ss` <url>\
    \n**USAGE   ➥  **Takes a screenshot of a website and sends the screenshot.\
    \n\n📌** CMD ➥** `.scapture` <url>\
    \n**USAGE   ➥  **Takes a screenshot of a website and sends the screenshot need to set config var for this.\
    \n\n**Example of a valid URL :** `https://www.google.com`"
    }
)
