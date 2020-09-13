# New arts added by @Sur_vivor
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

n = str(ALIVE_NAME) if ALIVE_NAME else "Sur_vivor"

emojis = {
    "yee": "ツ",
    "happy": "(ʘ‿ʘ)",
    "veryhappy": "=͟͟͞͞٩(๑☉ᴗ☉)੭ु⁾⁾",
    "amazed": "ヾ(o✪‿✪o)ｼ",
    "crying": "༎ຶ︵༎ຶ",
    "dicc": "╰U╯☜(◉ɷ◉ )",
    "fek": "╰U╯\n(‿ˠ‿)",
    "ded": "✖‿✖",
    "sad": "⊙︿⊙",
    "lenny": "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)",
    "idc": r"¯\_(ツ)_/¯",
    "f": "😂😂😂😂😂😂😂😂\n😂😂😂😂😂😂😂😂😂\n😂😂\n😂😂\n😂😂😂😂😂😂\n😂😂😂😂😂😂\n😂😂\n😂😂\n😂😂\n😂😂\n😂😂",
}

unpacked_emojis = ""

for emoji in emojis:
    unpacked_emojis += f"`{emoji}`\n"

ascii = {
    "mf": r"'                            / ¯͡  ) \n                           /...../ \n                         /´¯´/ \n                       /¯..../ \n                    /....  / \n             /´¯/'...' /´¯¯·¸ \n          / '/.../..../..../.. /¨¯\ \n        ('(...´...´.... ¯~'/...')  /\n         \.................'..... /´ \n          \................ _.·´\n            \..............( \n'             \.............\ ",
    "dislike": "███████▄▄███████████▄\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓███░░░░░░░░░░░░█\n██████▀░░█░░░░██████▀\n░░░░░░░░░█░░░░█\n░░░░░░░░░░█░░░█\n░░░░░░░░░░░█░░█\n░░░░░░░░░░░█░░█\n░░░░░░░░░░░░▀▀ ",
    "music": "╔══╗ \n║██║ \n║(O)║♫ ♪ ♫ ♪\n╚══╝\n▄ █ ▄ █ ▄ ▄ █ ▄ █ ▄ █\n\nVol- --------------------------● Vol+ ",
    "chess": "♜♞♝♚♛♝♞♜\n♟♟♟♟♟♟♟♟\n▓░▓░▓░▓░\n░▓░▓░▓░▓\n▓░▓░▓░▓░\n░▓░▓░▓░▓\n♙♙♙♙♙♙♙♙\n♖♘♗♔♕♗♘♖ ",
    "shitos": "╭━━━┳╮╱╱╭╮╱╭━━━┳━━━╮\n┃╭━╮┃┃╱╭╯╰╮┃╭━╮┃╭━╮┃\n┃╰━━┫╰━╋╮╭╯┃┃╱┃┃╰━━╮\n╰━━╮┃╭╮┣┫┃╱┃┃╱┃┣━━╮┃\n┃╰━╯┃┃┃┃┃╰╮┃╰━╯┃╰━╯┃\n╰━━━┻╯╰┻┻━╯╰━━━┻━━━╯ ",
    "qrcode": "█▀▀▀▀▀█░▀▀░░░█░░░░█▀▀▀▀▀█\n█░███░█░█▄░█▀▀░▄▄░█░███░█\n█░▀▀▀░█░▀█▀▀▄▀█▀▀░█░▀▀▀░█\n▀▀▀▀▀▀▀░▀▄▀▄▀▄█▄▀░▀▀▀▀▀▀▀\n█▀█▀▄▄▀░█▄░░░▀▀░▄█░▄▀█▀░▀\n░█▄▀░▄▀▀░░░▄▄▄█░▀▄▄▄▀▄▄▀▄\n░░▀█░▀▀▀▀▀▄█░▄░████ ██▀█▄\n▄▀█░░▄▀█▀█▀░█▄▀░▀█▄██▀░█▄\n░░▀▀▀░▀░█▄▀▀▄▄░▄█▀▀▀█░█▀▀\n█▀▀▀▀▀█░░██▀█░░▄█░▀░█▄░██\n█░███░█░▄▀█▀██▄▄▀▀█▀█▄░▄▄\n█░▀▀▀░█░█░░▀▀▀░█░▀▀▀▀▄█▀░\n▀▀▀▀▀▀▀░▀▀░░▀░▀░░░▀▀░▀▀▀▀` ",
    "youjoined": "━━━━━┓ \n┓┓┓┓┓┃\n┓┓┓┓┓┃　ヽ○ノ ⇦ Me When \n┓┓┓┓┓┃.      /　        You Joined\n┓┓┓┓┓┃  ノ) \n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃\n┓┓┓┓┓┃ ",
}

unpacked_ascii = ""

for art in ascii:
    unpacked_ascii += f"{art}\n"


@borg.on(admin_cmd(pattern="hek ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    for _ in range(5):
        await event.edit(";_;")
        await event.edit("_;;")
        await event.edit(";;_")
    await event.edit(";_;")


@borg.on(admin_cmd(pattern="sed ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    for _ in range(4):
        await event.edit(":/")
        await event.edit(":|")
        await event.edit(":\\")
        await event.edit(":|")
    await event.edit(":/")


@borg.on(admin_cmd(pattern="emoji ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    try:
        req_emoji = emojis[str(input_str)]
        await event.edit(req_emoji)
    except KeyError:
        await event.edit("Emoji not found!")


@borg.on(admin_cmd(pattern="ascii ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    try:
        req_ascii = ascii[str(input_str)]
        await event.edit(req_ascii)
    except KeyError:
        await event.edit("ASCII art not found!")


@borg.on(admin_cmd(pattern=r"ded"))
async def bluedevilded(ded):
    await ded.edit(
        n + " ==             |\n　　　　　|"
        "\n　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　／￣￣＼| \n"
        "＜ ´･ 　　 |＼ \n"
        "　|　３　 | 丶＼ \n"
        "＜ 、･　　|　　＼ \n"
        "　＼＿＿／∪ _ ∪) \n"
        "　　　　　 Ｕ Ｕ\n"
    )


M = (
    "$…………………GO…...………..….....$\n"
    "$$……………….TO....................$$\n"
    "..$$…………....HELL…............$$\n"
    "….$$s…………………………….…s$$\n"
    "..…$$$$……………………...….$$$$\n"
    "……³$$$$..¶¶¶¶¶¶¶¶..$$$$³\n"
    "...…….³$$$$..¶¶¶¶¶¶..$$$$³\n"
    "……¶..$$$$$..¶¶¶¶..$$$$$..¶\n"
    "…¶¶¶..$$$..¶¶¶¶¶¶..$$$..¶¶\n"
    "..¶¶¶….¶¶¶¶¶¶¶¶¶¶….¶¶¶¶\n"
    "¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n"
    "..¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶…\n"
    "….¶¶……..¶¶¶¶……….¶……………\n"
    "….¶¶……..¶¶¶¶……….¶¶…………\n"
    "….¶¶¶¶¶¶¶¶..¶¶¶¶¶¶¶¶\n"
    "……¶¶¶¶¶¶……¶¶¶¶¶¶¶\n"
    "………….¶¶¶¶¶¶¶¶¶…………\n"
    "…………...¶..¶..¶..¶..¶……\n"
    "…..…¶......¶……….…..¶…........¶\n"
    "…….¶¶.......DON'T MESS ....¶\n"
    "…….¶¶……....WITH ME........¶\n"
    "……¶¶………..¶¶…......….……..¶\n"
    "…¶¶..¶¶..¶¶..¶……...….¶..¶..¶\n"
    "¶..¶¶..¶¶..¶¶..¶……....¶...¶¶..\n"
    "¶¶..¶¶..¶..¶¶..¶……..¶..¶¶...¶\n"
    "…¶¶¶¶..¶..¶¶……....….¶¶..¶..¶\n"
)


P = (
    "██╗░░██╗██╗\n"
    "██║░░██║██║\n"
    "███████║██║\n"
    "██╔══██║██║\n"
    "██║░░██║██║\n"
    "╚═╝░░╚═╝╚═╝\n"
)

K = (
    "..... (¯`v´¯)♥️\n"
    ".......•.¸.•´\n"
    "....¸.•´  🅷🅸\n"
    "... (   BABYy\n"
    "☻/ \n"
    "/▌✿🌷✿\n"
    "/ \     \|/\n"
)

G = (
    "╔══╗        🎧\n"
    "║██║  Nice ya ! (•  ̮ •) \n"
    r"║ (O) ║..'...........    /█\  \n"
    "╚══╝                  . .Π.\n"
    "▄ █ ▄ █ ▄ ▄ █ ▄ █ ▄ █\n"
    "Min- - - - - - - - - - - -●Max\n"
)

D = (
    "🌙.     *       ☄️      \n"
    "🌟   .  *       .         \n"
    "                       *   .      🛰     .        ✨      *\n"
    "  .     *   SLEEP WELL        🚀     \n"
    "      .              . . SWEET DREAMS 🌙\n"
    ". *       🌏 GOOD NIGHT         *\n"
    "                     🌙.     *       ☄️      \n"
    "🌟   .  *       .         \n"
    "                       *   .      🛰     .        ✨      *\n"
)

E = (
    "▃▃▃▃▃▃▃▃▃▃▃\n"
    "┊ ┊ ┊ ┊ ┊ ┊\n"
    "┊ ┊ ┊ ┊ ˚✩ ⋆｡˚ ✩\n"
    "┊ ┊ ┊ ✫\n"
    "┊ ┊ ✧🎂🍰🍫🍭\n"
    "┊ ┊ ✯\n"
    "┊ . ˚ ˚✩\n"
    "........♥️♥️..........♥️♥️_\n"
    ".....♥️........♥️..♥️........♥️_\n"
    "...♥️.............♥️............♥️\n"
    "......♥️.....Happy.......♥️__\n"
    "...........♥️..............♥️__\n"
    "................♥️.....♥️__\n"
    "......................♥️__\n"
    "...............♥️........♥️__\n"
    "..........♥️...............♥️__\n"
    ".......♥️..Birthday....♥️_\n"
    ".....♥️..........♥️...........♥️__\n"
    ".....♥️.......♥️_♥️.....♥️__\n"
    ".........♥️♥️........♥️♥️.....\n"
    ".............................................\n"
    "..... (¯`v´¯)♥️\n"
    ".......•.¸.•´STAY BLESSED\n"
    "....¸.•´      LOVE&FUN\n"
    "... (   YOU DESERVE\n"
    "☻/ THEM A LOT\n"
    "/▌✿🌷✿\n"
    r"/ \     \|/\n"
    "▃▃▃▃▃▃▃▃▃▃▃\n"
)

C = (
    "G🌷o🍃o🌷D\n"
    "M🍃o🌷r🍃N🌷i🍃N🌷g\n"
    "            \n"
    "No matter how good or \n"
    "bad your life is,\n"
    "wake up each morning\n"
    "and be thankful.\n"
    "You still have a new day.\n"
    "        \n"
    "🌞   \n"
    "         \n"
    "╱◥████◣\n"
    "│田│▓ ∩ │◥███◣\n"
    "╱◥◣ ◥████◣田∩田│\n"
    "│╱◥█◣║∩∩∩ 田∩田│\n"
    "║◥███◣∩田∩ 田∩田│\n"
    "│∩│ ▓ ║∩田│║▓田▓\n"
    "🌹🌷🌹🌷🌹🍃🌷🌹🌷🌹\n"
)

S = (
    ".......🦋🦋........🦋🦋\n"
    "...🦋.........🦋🦋.......🦋\n"
    "...🦋............💙..........🦋\n"
    ".....🦋🅣🅗🅐🅝🅚🅢 🦋\n"
    "....... 🦋.................🦋\n"
    "..............🦋......🦋\n"
    "...................💙\n"
)

W = (
    ".                       /¯ )\n"
    "                      /¯  /\n"
    "                    /    /\n"
    "              /´¯/'   '/´¯¯`•¸\n"
    r"          /'/   /    /       /¨¯\ \n"
    "        ('(   (   (   (  ¯~/'  ')\n"
    r"         \                        /\n"
    r"          \                _.•´\n"
    r"            \              (\n"
    r"              \  \n"
    "Roses are RED\n"
    "Violets are BLUE\n"
    "My middle finger for U🖕😂\n"
)

Z = (
    ".Me  😎  rest in peace\n"
    r"          |\👐           mf...\n"
    r"        / \         \n"
    "━━━━━┒＼＼ \n"
    "┓┏┓┏┓┃\n"
    "┛┗┛┗┛┃＼😫／\n"
    "┓┏┓┏┓┃   / \n"
    "┛┗┛┗┛┃ノ)\n"
    "┓┏┓┏┓┃ \n"
    "┛┗┛┗┛┃  👆you \n"
    "┓┏┓┏┓┃ \n"
    "┛┗┛┗┛┃ \n"
    "┓┏┓┏┓┃ \n"
    "┛┗┛┗┛┃ \n"
    "┓┏┓┏┓┃ \n"
    "┛┗┛┗┛┃ \n"
    "┓┏┓┏┓┃\n"
    "┃┃┃┃┃┃\n"
    "┻┻┻┻┻┻\n"
)


B = (
    "😍🔊Noice to Hear🎧😍\n"
    "0:35 ━❍──────── -5:32\n"
    "           ⇆  ◁ㅤ❚❚ㅤ▷  ↻\n"
    "VOLUME: ▁▂▃▄▅▆▇ 100%\n"
)


@borg.on(admin_cmd(pattern=r"demon"))
async def bluedevilmonster(demon):
    await demon.edit(M)


@borg.on(admin_cmd(pattern=r"hy"))
async def bluedevilhy(hy):
    await hy.edit(P)


@borg.on(admin_cmd(pattern=r"baby"))
async def bluedevilbaby(baby):
    await baby.edit(K)


@borg.on(admin_cmd(pattern=r"muusic"))
async def bluedevilgun(muusic):
    await gun.edit(G)


@borg.on(admin_cmd(pattern=r"goodn"))
async def bluedevilgoodn(goodn):
    await goodn.edit(D)


@borg.on(admin_cmd(pattern=r"hello"))
async def bluedevilhello(hello):
    await hello.edit(H)


@borg.on(admin_cmd(pattern=r"hbd"))
async def bluedevilhmf(hmf):
    await hmf.edit(E)


@borg.on(admin_cmd(pattern=r"goodm"))
async def bluedevilgoodm(goodm):
    await goodm.edit(C)


@borg.on(admin_cmd(pattern=r"tnk"))
async def bluedeviltnk(tnk):
    await tnk.edit(S)


@borg.on(admin_cmd(pattern=r"fooku"))
async def bluedevilfooku(fooku):
    await fooku.edit(W)


@borg.on(admin_cmd(pattern=r"ripp"))
async def bluedevilripp(ripp):
    await ripp.edit(Z)


@borg.on(admin_cmd(pattern=r"noice"))
async def bluedevilnoice(noice):
    await noice.edit(B)
