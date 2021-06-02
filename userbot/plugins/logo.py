"""
Created & modified by @Jisan7509

Base idea DevsExpo

"""
import asyncio
import os
import re
import urllib

import PIL
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont

from userbot import catub

from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import convert_toimage, reply_id

# ======================================================================================================================================================================================

vars_list = {
    "bg": "LOGO_BACKGROUND",
    "lfc": "LOGO_FONT_COLOR",
    "lfs": "LOGO_FONT_SIZE",
    "lfh": "LOGO_FONT_HEIGHT",
    "lfw": "LOGO_FONT_WIDTH",
    "lf": "LOGO_FONT",
}

# ======================================================================================================================================================================================

plugin_category = "useless"


@catub.cat_cmd(
    pattern="(|s)logo(?: |$)(.*)",
    command=("logo", plugin_category),
    info={
        "header": "Make a logo in image or sticker",
        "description": "Just a fun purpose plugin to create logo in image or in sticker.",
        "flags": {
            "s": "To create a logo in sticker instade of image.",
        },
        "usage": [
            "{tr}logo <text>",
            "{tr}slogo <text>",
        ],
        "examples": [
            "{tr}logo Cat",
            "{tr}slogo Cat",
        ],
    },
)
async def very(event):
    "To create a logo"
    cmd = event.pattern_match.group(1).lower()
    text = event.pattern_match.group(2)
    if not text:
        return await edit_delete(event, "```Give some text to make the logo...```")
    reply_to_id = await reply_id(event)
    catevent = await edit_or_reply(event, "`Processing.....`")
    LOGO_FONT_SIZE = gvarstatus("LOGO_FONT_SIZE") or 220
    LOGO_FONT_WIDTH = gvarstatus("LOGO_FONT_WIDTH") or 2
    LOGO_FONT_HEIGHT = gvarstatus("LOGO_FONT_HEIGHT") or 2
    LOGO_FONT_COLOR = gvarstatus("LOGO_FONT_COLOR") or "red"
    if not os.path.exists("temp/bg_img.jpg"):
        if gvarstatus("LOGO_BACKGROUND") is None:
            urllib.request.urlretrieve(
                "https://telegra.ph/file/47fce894d66ae67e3665f.jpg", "temp/bg_img.jpg"
            )
        else:
            LOGO_BACKGROUND = gvarstatus("LOGO_BACKGROUND")
            urllib.request.urlretrieve(LOGO_BACKGROUND, "temp/bg_img.jpg")
    img = Image.open("./temp/bg_img.jpg")
    draw = ImageDraw.Draw(img)
    if not os.path.exists("temp/logo.ttf"):
        if gvarstatus("LOGO_FONT") is None:
            urllib.request.urlretrieve(
                "https://github.com/Jisan09/Files/blob/main/fonts/Streamster.ttf?raw=true",
                "temp/logo.ttf",
            )
        else:
            LOGO_FONT = gvarstatus("LOGO_FONT")
            urllib.request.urlretrieve(LOGO_FONT, "temp/logo.ttf")
    font = ImageFont.truetype("temp/logo.ttf", int(LOGO_FONT_SIZE))
    image_widthz, image_heightz = img.size
    w, h = draw.textsize(text, font=font)
    h += int(h * 0.21)
    draw.text(
        (
            (image_widthz - w) / float(LOGO_FONT_WIDTH),
            (image_heightz - h) / float(LOGO_FONT_HEIGHT),
        ),
        text,
        font=font,
        fill=LOGO_FONT_COLOR,
    )
    file_name = "LogoBy@MeisNub.png"
    img.save(file_name, "png")
    if cmd == "":
        await event.client.send_file(
            event.chat_id,
            file_name,
            reply_to=reply_to_id,
        )
    elif cmd == "s":
        await clippy(event.client, file_name, event.chat_id, reply_to_id)
    await catevent.delete()
    if os.path.exists(file_name):
        os.remove(file_name)


@catub.cat_cmd(
    pattern="(|c)lbg(?: |$)(.*)",
    command=("bg", plugin_category),
    info={
        "header": "Change the background of logo",
        "description": "To change the background on which logo will created, in **bg** there few built-in backgrounds.",
        "flags": {
            "c": "Custom background for logo, can set by giving a telegraph link or reply to media.",
        },
        "usage": [
            "{tr}lbg <background color code>",
            "{tr}clbg <telegraph link / reply to media>",
        ],
        "examples": [
            "{tr}lbg red",
            "{tr}clbg https://telegra.ph/blablabla.jpg",
        ],
    },
)
async def bad(event):
    "To change background of logo"
    cmd = event.pattern_match.group(1).lower()
    input_str = event.pattern_match.group(2)
    source = requests.get("https://github.com/Jisan09/Files/tree/main/backgroud")
    soup = BeautifulSoup(source.text, features="html.parser")
    links = soup.find_all("a", class_="js-navigation-open Link--primary")
    bg_name = []
    for i in links:
        bg_name.append(i.text)
    lbg = ""
    for i, each in enumerate(bg_name, start=1):
        lbg += f"**{i}.**  `{each}`\n"
    if os.path.exists("./temp/bg_img.jpg"):
        os.remove("./temp/bg_img.jpg")
    if cmd == "c":
        reply_message = await event.get_reply_message()
        if not input_str and event.reply_to_msg_id and reply_message.media:
            if not os.path.isdir("./temp"):
                os.mkdir("./temp")
            os.path.join("./temp", "bg_img.jpg")
            output = await _cattools.media_to_pic(event, reply_message)
            convert_toimage(output[1], filename="./temp/bg_img.jpg")
            return await edit_delete(
                event, "This media is successfully set as background."
            )
        if input_str.startswith("https://t"):
            addgvar("LOGO_BACKGROUND", input_str)
            return await edit_delete(
                event, f"**Background for logo changed to :-** `{input_str}`"
            )
        else:
            return await edit_delete(
                event, "Give a valid Telegraph picture link, Or reply to a media."
            )
    if not input_str:
        await edit_delete(
            event, f"**Available background names are here:-**\n\n{lbg}", time=40
        )
        return
    if input_str not in bg_name:
        catevent = await edit_or_reply(event, "`Give me a correct background name...`")
        await asyncio.sleep(1)
        await edit_delete(
            catevent, f"**Available background names are here:-**\n\n{lbg}", time=40
        )
    else:
        string = f"https://raw.githubusercontent.com/Jisan09/Files/main/backgroud/{input_str}"
        addgvar("LOGO_BACKGROUND", string)
        await edit_delete(
            event, f"**Background for logo changed to :-** `{input_str}`", time=10
        )


@catub.cat_cmd(
    pattern="lf(|c|s|h|w)(?: |$)(.*)",
    command=("lf", plugin_category),
    info={
        "header": "Change text style for logo.",
        "description": "Customise logo font, font size, font position like text hight or width.",
        "flags": {
            "c": "To change color of logo font.",
            "s": "To change size of logo font.",
            "h": "To change hight of logo font.",
            "w": "To change width of logo font.",
        },
        "usage": [
            "{tr}lf <font name>",
            "{tr}lfc <logo font color>",
            "{tr}lfs <1-100>",
            "{tr}lfh <10-1000>",
            "{tr}lfw <10-1000>",
        ],
        "examples": [
            "{tr}lf genau-font.ttf",
            "{tr}lfc white",
            "{tr}lfs 120",
            "{tr}lfh 1",
            "{tr}lfw 8",
        ],
    },
)
async def pussy(event):
    "To customise logo font"
    cmd = event.pattern_match.group(1).lower()
    input_str = event.pattern_match.group(2)
    if cmd == "":
        source = requests.get("https://github.com/Jisan09/Files/tree/main/fonts")
        soup = BeautifulSoup(source.text, features="html.parser")
        links = soup.find_all("a", class_="js-navigation-open Link--primary")
        logo_font = []
        for i in links:
            logo_font.append(i.text)
            font_name = ""
            for i, each in enumerate(logo_font, start=1):
                font_name += f"**{i}.**  `{each}`\n"
        if not input_str:
            return await edit_delete(
                event, f"**Available font names are here:-**\n\n{font_name}", time=60
            )
        if input_str not in logo_font:
            catevent = await edit_or_reply(event, "`Give me a correct font name...`")
            await asyncio.sleep(1)
            await edit_delete(
                catevent, f"**Available font names are here:-**\n\n{font_name}", time=60
            )
        else:
            if " " in input_str:
                input_str = str(input_str).replace(" ", "%20")
            string = (
                f"https://github.com/Jisan09/Files/blob/main/fonts/{input_str}?raw=true"
            )
            if os.path.exists("temp/logo.ttf"):
                os.remove("temp/logo.ttf")
                urllib.request.urlretrieve(
                    string,
                    "temp/logo.ttf",
                )
            addgvar("LOGO_FONT", string)
            await edit_delete(
                event, f"**Font for logo changed to :-** `{input_str}`", time=10
            )
    elif cmd == "c":
        fg_name = []
        for name, code in PIL.ImageColor.colormap.items():
            fg_name.append(name)
            fg_list = str(fg_name).replace("'", "`")
        if not input_str:
            return await edit_delete(
                event,
                f"**Available foreground color names are here:-**\n\n{fg_list}",
                time=60,
            )
        if input_str not in fg_name:
            catevent = await edit_or_reply(
                event, "`Give me a correct foreground color name...`"
            )
            await asyncio.sleep(1)
            await edit_delete(
                catevent,
                f"**Available foreground color names are here:-**\n\n{fg_list}",
                time=60,
            )
        else:
            addgvar("LOGO_FONT_COLOR", input_str)
            await edit_delete(
                event,
                f"**Foreground color for logo changed to :-** `{input_str}`",
                time=10,
            )
    else:
        cat = re.compile(r"^\-?[1-9][0-9]*\.?[0-9]*")
        isint = re.match(cat, input_str)
        if not input_str or not isint:
            return await edit_delete(
                event, f"**Give an integer value to set**", time=10
            )
        else:
            if cmd == "s":
                input_str = int(input_str)
                if input_str > 0 and input_str <= 1000:
                    addgvar("LOGO_FONT_SIZE", input_str)
                    await edit_delete(
                        event, f"**Font size is changed to :-** `{input_str}`"
                    )
                else:
                    await edit_delete(
                        event,
                        f"**Font size is between 20 - 1000, You can't set limit to :** `{input_str}`",
                    )
            elif cmd == "w":
                input_str = float(input_str)
                if input_str > 0 and input_str <= 100:
                    addgvar("LOGO_FONT_WIDTH", input_str)
                    await edit_delete(
                        event, f"**Font width is changed to :-** `{input_str}`"
                    )
                else:
                    await edit_delete(
                        event,
                        f"**Font width is between 0 - 30, You can't set limit to {input_str}",
                    )
            elif cmd == "h":
                input_str = float(input_str)
                if input_str > 0 and input_str <= 100:
                    addgvar("LOGO_FONT_HEIGHT", input_str)
                    await edit_delete(
                        event, f"**Font hight is changed to :-** `{input_str}`"
                    )
                else:
                    await edit_delete(
                        event,
                        f"**Font hight is between 0 - 30, You can't set limit to {input_str}",
                    )


@catub.cat_cmd(
    pattern="(g|d|r)lvar(?: |$)(.*)",
    command=("lvar", plugin_category),
    info={
        "header": "Manage values which set for logo",
        "description": "To see which value have been set, or to delete a value , or to reset all values.",
        "flags": {
            "g": "Gets the value of the var which you set manually for logo.",
            "d": "Delete the value of the var which you set manually for logo.",
            "r": "Delete all the values of the vars which you set manually for logo & reset all changes.",
        },
        "usage": [
            "{tr}glvar <var code>",
            "{tr}dlvar <var code>",
            "{tr}rlvar",
        ],
        "examples": [
            "{tr}glvar bg",
            "{tr}dlvar lfc",
        ],
    },
)
async def cat(event):
    "Manage all values of logo"
    cmd = event.pattern_match.group(1).lower()
    input_str = event.pattern_match.group(2)
    if input_str in vars_list.keys():
        var = vars_list[input_str]
        if cmd == "g":
            var_data = gvarstatus(var)
            await edit_delete(event, f"📑 Value of **{var}** is  `{var_data}`", time=60)
        elif cmd == "d":
            if input_str == "bg":
                if os.path.exists("./temp/bg_img.jpg"):
                    os.remove("./temp/bg_img.jpg")
            if input_str == "lf":
                if os.path.exists("./temp/logo.ttf"):
                    os.remove("./temp/logo.ttf")
            delgvar(var)
            await edit_delete(
                event, f"📑 Value of **{var}** is now deleted & set to default.", time=60
            )
    elif not input_str and cmd == "r":
        delgvar("LOGO_BACKGROUND")
        delgvar("LOGO_FONT_COLOR")
        delgvar("LOGO_FONT")
        delgvar("LOGO_FONT_SIZE")
        delgvar("LOGO_FONT_HEIGHT")
        delgvar("LOGO_FONT_WIDTH")
        if os.path.exists("./temp/bg_img.jpg"):
            os.remove("./temp/bg_img.jpg")
        if os.path.exists("./temp/logo.ttf"):
            os.remove("./temp/logo.ttf")
        await edit_delete(
            event,
            "📑 Values for all vars deleted successfully & all settings reset.",
            time=20,
        )
    else:
        await edit_delete(
            event,
            f"**📑 Give correct vars name :**\n__Correct Vars code list is :__\n\n1. `bg` : **LOGO_BACKGROUND**\n2. `lfc` : **LOGO_FONT_COLOR**\n3. `lf` : **LOGO_FONT**\n4. `lfs` : **LOGO_FONT_SIZE**\n5. `lfh` : **LOGO_FONT_HEIGHT**\n6. `lfw` : **LOGO_FONT_WIDTH**",
            time=60,
        )
