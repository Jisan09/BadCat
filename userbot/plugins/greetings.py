from ..utils import admin_cmd, edit_or_reply, sudo_cmd

R = (
    "██╗░░██╗██╗\n"
    "██║░░██║██║\n"
    "███████║██║\n"
    "██╔══██║██║\n"
    "██║░░██║██║\n"
    "╚═╝░░╚═╝╚═╝\n"
)

S = (
    "..... (¯`v´¯)♥️\n"
    ".......•.¸.•´\n"
    "....¸.•´  🅷🅸\n"
    "... (   BABYy\n"
    "☻/ \n"
    "/▌✿🌷✿\n"
    "/ \     \|/\n"
)


U = (
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

V = (
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

W = (
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

X = (
    ".......🦋🦋........🦋🦋\n"
    "...🦋.........🦋🦋.......🦋\n"
    "...🦋............💙..........🦋\n"
    ".....🦋🅣🅗🅐🅝🅚🅢 🦋\n"
    "....... 🦋.................🦋\n"
    "..............🦋......🦋\n"
    "...................💙\n"
)


@bot.on(admin_cmd(pattern=r"hy$"))
@bot.on(sudo_cmd(pattern="hy$", allow_sudo=True))
async def bluedevilhy(hy):
    await edit_or_reply(hy, R)


@bot.on(admin_cmd(pattern=r"baby$"))
@bot.on(sudo_cmd(pattern="baby$", allow_sudo=True))
async def bluedevilbaby(baby):
    await edit_or_reply(baby, S)


@bot.on(admin_cmd(pattern=r"hbd$"))
@bot.on(sudo_cmd(pattern="hbd$", allow_sudo=True))
async def bluedevilhbd(hbd):
    await edit_or_reply(hbd, V)


@bot.on(admin_cmd(pattern=r"thanks$"))
@bot.on(sudo_cmd(pattern="thanks$", allow_sudo=True))
async def bluedeviltnk(tnk):
    await edit_or_reply(tnk, X)


@bot.on(admin_cmd(pattern="gmg$"))
@bot.on(sudo_cmd(pattern="gmg$", allow_sudo=True))
async def gm(event):
    await edit_or_reply(
        event,
        "｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･｡♥｡･ﾟ♡ﾟ･\n╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╭╮\n╭━┳━┳━┳╯┃╭━━┳━┳┳┳━┳╋╋━┳┳━╮\n┃╋┃╋┃╋┃╋┃┃┃┃┃╋┃╭┫┃┃┃┃┃┃┃╋┃\n┣╮┣━┻━┻━╯╰┻┻┻━┻╯╰┻━┻┻┻━╋╮┃\n╰━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯\n｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･｡♥｡･ﾟ♡ﾟ･",
    )


@bot.on(admin_cmd(pattern="gnt$"))
@bot.on(sudo_cmd(pattern="gnt$", allow_sudo=True))
async def gn(event):
    await edit_or_reply(
        event,
        "｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･\n╱╱╱╱╱╱╱╭╮╱╱╱╭╮╱╭╮╭╮\n╭━┳━┳━┳╯┃╭━┳╋╋━┫╰┫╰╮\n┃╋┃╋┃╋┃╋┃┃┃┃┃┃╋┃┃┃╭┫\n┣╮┣━┻━┻━╯╰┻━┻╋╮┣┻┻━╯\n╰━╯╱╱╱╱╱╱╱╱╱╱╰━╯\n｡♥｡･ﾟ♡ﾟ･｡♥° ♥｡･ﾟ♡ﾟ･",
    )


# by @turquoise-giggle
@bot.on(admin_cmd(pattern="gmg2$"))
@bot.on(sudo_cmd(pattern="gmg2$", allow_sudo=True))
async def gm(event):
    await edit_or_reply(
        event,
        "♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n╔══╗────╔╗──────────╔╗\n║╔═╬═╦═╦╝║╔══╦═╦╦╦═╦╬╬═╦╦═╗\n║╚╗║╬║╬║╬║║║║║╬║╔╣║║║║║║║╬║\n╚══╩═╩═╩═╝╚╩╩╩═╩╝╚╩═╩╩╩═╬╗║\n────────────────────────╚═╝\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛･",
    )


# by @turquoise-giggle
@bot.on(admin_cmd(pattern="gnt2$"))
@bot.on(sudo_cmd(pattern="gnt2$", allow_sudo=True))
async def gn(event):
    await edit_or_reply(
        event,
        "♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n╔══╗────╔╗╔═╦╦╗─╔╗╔╗\n║╔═╬═╦═╦╝║║║║╠╬═╣╚╣╚╗\n║╚╗║╬║╬║╬║║║║║║╬║║║╔╣\n╚══╩═╩═╩═╝╚╩═╩╬╗╠╩╩═╝\n──────────────╚═╝\n╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨╱╱✨\n♛┈⛧┈┈•༶🦋⋇⋆✦⋆⋇🦋༶•┈┈⛧┈♛･",
    )


@bot.on(admin_cmd(pattern=r"gmg3$"))
@bot.on(sudo_cmd(pattern="gmg3$", allow_sudo=True))
async def bluedevilgoodm(goodm):
    await edit_or_reply(goodm, W)


@bot.on(admin_cmd(pattern=r"gnt3$"))
@bot.on(sudo_cmd(pattern="gnt3$", allow_sudo=True))
async def bluedevilgoodn(goodn):
    await edit_or_reply(goodn, U)


# by  @Halto_Tha
@bot.on(admin_cmd(pattern=r"lmoon$"))
@bot.on(sudo_cmd(pattern="lmoon$", allow_sudo=True))
async def test(event):
    if event.fwd_from:
        return
    await edit_or_reply(
        event,
        "🌕🌕🌕🌕🌕🌕🌕🌕\n🌕🌕🌖🌔🌖🌔🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌗🌔🌖🌓🌕🌕\n🌕🌕🌖🌓🌗🌔🌕🌕\n🌕🌕🌗🌑🌑🌓🌕🌕\n🌕🌕🌗👀🌑🌓🌕🌕\n🌕🌕🌘👄🌑🌓🌕🌕\n🌕🌕🌗🌑🌑🌒🌕🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌕🌘🌑🌑🌑🌑🌒🌕\n🌖🌑🌑🌑🌑🌑🌑🌔\n🌕🤜🏻🌑🌑🌑🌑🤛🏻🌕\n🌕🌖🌑🌑🌑🌑🌔🌕\n🌘🌑🌑🌑🌑🌑🌑🌒\n🌕🌕🌕🌕🌕🌕🌕🌕",
    )


@bot.on(admin_cmd(pattern=r"city$"))
@bot.on(sudo_cmd(pattern="city$", allow_sudo=True))
async def test(event):
    if event.fwd_from:
        return
    await edit_or_reply(
        event,
        """☁☁🌞      ☁           ☁
       ☁  ✈         ☁    🚁    ☁    ☁        ☁          ☁     ☁   ☁
🏬🏨🏫🏢🏤🏥🏦🏪🏫
              🌲/     l🚍\🌳👭
           🌳/  🚘 l  🏃 \🌴 👬                        👬     🌴/            l  🚔    \🌲
      🌲/   🚖     l        \
          🌳/🚶           |   🚍         \ 🌴🚴🚴
🌴/                    |                     \🌲""",
    )


# @PhycoNinja13b 's Part begin from here


@bot.on(admin_cmd(pattern=r"hi ?(.*)"))
@bot.on(sudo_cmd(pattern=r"hi ?(.*)", allow_sudo=True))
async def hi(event):
    giveVar = event.text
    cat = giveVar[4:5]
    if not cat:
        cat = "🌺"
    await edit_or_reply(
        event,
        f"{cat}✨✨{cat}✨{cat}{cat}{cat}\n{cat}✨✨{cat}✨✨{cat}✨\n{cat}{cat}{cat}{cat}✨✨{cat}✨\n{cat}✨✨{cat}✨✨{cat}✨\n{cat}✨✨{cat}✨{cat}{cat}{cat}\n☁☁☁☁☁☁☁☁",
    )


@bot.on(admin_cmd(pattern=r"cheer$"))
@bot.on(sudo_cmd(pattern="cheer$", allow_sudo=True))
async def cheer(event):
    if event.fwd_from:
        return
    await edit_or_reply(
        event,
        "💐💐😉😊💐💐\n☕ Cheer Up  🍵\n🍂 ✨ )) ✨  🍂\n🍂┃ (( * ┣┓ 🍂\n🍂┃*💗 ┣┛ 🍂 \n🍂┗━━┛  🍂🎂 For YOU  🍰\n💐💐😌😚💐💐",
    )


@bot.on(admin_cmd(pattern=r"getwell$"))
@bot.on(sudo_cmd(pattern="getwell$", allow_sudo=True))
async def getwell(event):
    if event.fwd_from:
        return
    await edit_or_reply(
        event, "🌹🌹🌹🌹🌹🌹🌹🌹 \n🌹😷😢😓😷😢💨🌹\n🌹💝💉🍵💊💐💝🌹\n🌹 GetBetter Soon! 🌹\n🌹🌹🌹🌹🌹🌹🌹🌹"
    )


@bot.on(admin_cmd(pattern=r"luck$"))
@bot.on(sudo_cmd(pattern="luck$", allow_sudo=True))
async def luck(event):
    if event.fwd_from:
        return
    await edit_or_reply(
        event, "💚~🍀🍀🍀🍀🍀\n🍀╔╗╔╗╔╗╦╗✨🍀\n🍀║╦║║║║║║👍🍀\n🍀╚╝╚╝╚╝╩╝。 🍀\n🍀・・ⓁⓊⒸⓀ🍀\n🍀🍀🍀 to you💚"
    )


@bot.on(admin_cmd(pattern=r"sprinkle$"))
@bot.on(sudo_cmd(pattern="sprinkle$", allow_sudo=True))
async def sprinkle(event):
    if event.fwd_from:
        return
    await edit_or_reply(
        event,
        "✨.•*¨*.¸.•*¨*.¸¸.•*¨*• ƸӜƷ\n🌸🌺🌸🌺🌸🌺🌸🌺\n Sprinkled with love❤\n🌷🌻🌷🌻🌷🌻🌷🌻\n ¨*.¸.•*¨*. ¸.•*¨*.¸¸.•*¨`*•.✨\n🌹🍀🌹🍀🌹🍀🌹🍀",
    )
