# Edit credit @Sur_vivor & @jisan7509
# Elove by @turquoise-giggle

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import CMD_HELP,ALIVE_NAME

DEF = str(ALIVE_NAME) if ALIVE_NAME else "cat"
USR = str(Config.LIVE_USERNAME) if Config.LIVE_USERNAME else "@Jisan7509"


@bot.on(admin_cmd(pattern="ded (.*)"))
@bot.on(sudo_cmd(pattern="ded (.*)", allow_sudo=True))
async def kakashi(ded):
    name = ded.pattern_match.group(1)
    await edit_or_reply(ded,
        f"[{DEF}]({USR}) --- {name}          \n　　　　　|"
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


@bot.on(admin_cmd(pattern="killer (.*)"))
@bot.on(sudo_cmd(pattern="killer (.*)", allow_sudo=True))
async def kakashi(killer):
    name = killer.pattern_match.group(1)
    await edit_or_reply(killer,
        f"__**Commando **__[{DEF}]({USR})          \n\n"
        "_/﹋\_\n"
        "(҂`_´)\n"
        f"<,︻╦╤─ ҉ - - - {name}\n"
        "_/﹋\_\n"
    )


@bot.on(admin_cmd(pattern=r"elove$"))
@bot.on(sudo_cmd(pattern="elove$", allow_sudo=True))
async def kakashi(event):
    await edit_or_reply(event,
        "░░▄███▄███▄\n░░█████████\n░░▒▀█████▀░\n░░▒░░▀█▀\n░░▒░░█░\n░░▒░█\n░░░█\n░░█░░░░███████\n░██░░░██▓▓███▓██▒\n██░░░█▓▓▓▓▓▓▓█▓████\n██░░██▓▓▓(◐)▓█▓█▓█\n███▓▓▓█▓▓▓▓▓█▓█▓▓▓▓█\n▀██▓▓█░██▓▓▓▓██▓▓▓▓▓█\n░▀██▀░░█▓▓▓▓▓▓▓▓▓▓▓▓▓█\n░░░░▒░░░█▓▓▓▓▓█▓▓▓▓▓▓█\n░░░░▒░░░█▓▓▓▓█▓█▓▓▓▓▓█\n░▒░░▒░░░█▓▓▓█▓▓▓█▓▓▓▓█\n░▒░░▒░░░█▓▓▓█░░░█▓▓▓█\n░▒░░▒░░██▓██░░░██▓▓██\n██████████████████████\n█─████─▄▄─██─█─██─▄▄─█\n█─██▀█─██─██─█─██─▄█▀█\n█▄▄▄▄▀▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▀"
    )


A = (
    "▄███████▄\n"
    "█▄█████▄█\n"
    "█▼▼▼▼▼█\n"
    "██________█▌\n"
    "█▲▲▲▲▲█\n"
    "█████████\n"
    "_████\n"
)

B = (
    "┈┈┏━╮╭━┓┈╭━━━━╮\n"
    "┈┈┃┏┗┛┓┃╭┫ⓞⓘⓝⓚ┃\n"
    "┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
    "┈╭━┻╮╲┗━━━━╮╭╮┈\n"
    "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
    "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
    "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
    "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n"
)

D = (
    "░▐█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄\n"
    "░███████████████████████ \n"
    "░▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓◤ \n"
    "░▀░▐▓▓▓▓▓▓▌▀█░░░█▀░\n"
    "░░░▓▓▓▓▓▓█▄▄▄▄▄█▀░░\n"
    "░░█▓▓▓▓▓▌░░░░░░░░░░\n"
    "░▐█▓▓▓▓▓░░░░░░░░░░░\n"
    "░▐██████▌░░░░░░░░░░\n"
)

E = (
    "╥━━━━━━━━╭━━╮━━┳\n"
    "╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
    "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
    "╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
    "╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
    "╨━━┗┛┗┛━━┗┛┗┛━━┻\n"
)
F = "╔┓┏╦━╦┓╔┓╔━━╗\n" "║┗┛║┗╣┃║┃║X X║\n" "║┏┓║┏╣┗╣┗╣╰╯║\n" "╚┛┗╩━╩━╩━╩━━╝\n"
G = (
    "▬▬▬.◙.▬▬▬ \n"
    "═▂▄▄▓▄▄▂ \n"
    "◢◤ █▀▀████▄▄▄▄◢◤ \n"
    "█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
    "◥█████◤ \n"
    "══╩══╩══ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ Hello, My Friend :D \n"
    "╬═╬☻/ \n"
    "╬═╬/▌ \n"
    "╬═╬/ \\n"
)

H = (
    "┳┻┳┻╭━━━━╮╱▔▔▔╲\n"
    "┻┳┻┳┃╯╯╭━┫▏╰╰╰▕\n"
    "┳┻┳┻┃╯╯┃▔╰┓▔▂▔▕╮\n"
    "┻┳┻┳╰╮╯┃┈╰┫╰━╯┏╯\n"
    "┳┻┳┻┏╯╯┃╭━╯┳━┳╯\n"
    "┻┳┻┳╰━┳╯▔╲╱▔╭╮▔╲\n"
    "┳┻┳┻┳┻┃┈╲┈╲╱╭╯╮▕\n"
    "┻┳┻┳┻┳┃┈▕╲▂╱┈╭╯╱\n"
    "┳┻┳┻┳┻┃'''┈┃┈┃┈'''╰╯\n"
    "┻┳┻┳┻┏╯▔'''╰┓┣━┳┫\n"
    "┳┻┳┻┳╰┳┳┳'''╯┃┈┃┃\n"
    "┻┳┻┳┻┳┃┃┃┈'''┃┈┃┃\n"
    "┳┻┳┻┳┻┃┃┃'''┊┃┈┃┃\n"
    "┻┳┻┳┻┳┃┃┃┈'''┃┈┃┃.\n"
    "┳┻┳┻┳┻┣╋┫'''┊┣━╋┫\n"
    "┻┳┻┳┻╭╯╰╰-╭╯━╯.''╰╮\n"
    "Love You Forever,,,,\n"
)

I = (
    "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡿⠋⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⠀⣠⣾⣿⡿⠋⠀⠀⠉⠻⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⠃⠀⠀⣀⡀⠀⢹⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡄⠀⠙⠻⠋⠀⠀⣸⣿⣿⠀⠀⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⣰⣿⣿⠟⠀⢠⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡿⠛⠛⠒⠶⠾⢿⣿⣿⣷⣄⣾⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⢰⣿⣿⣷⣶⣦⣼⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡀⠀⠙⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⢿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⠀⠀⠀⠉⠉⠛⠛⠛⠶⢶⣤⣼⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣦⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠁⠀⣾⣿⣷⡄⠀⢼⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⠀⢿⣿⣿⡿⠀⠈⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣇⠀⠀⠉⠋⠁⠀⢠⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠿⢷⣤⣀⣀⣀⣠⣾⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⠀⠀⠈⠉⠉⠛⢻⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣶⣦⣤⣤⣀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠹⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⠙⠻⣀⣀⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠁⠀⣀⡀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⢸⣿⡇⠀⣷⡀⠘⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡄⠈⢻⡇⠀⡿⠃⠀⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣷⣄⢸⡇⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⠉⠉⠑⠒⠲⠿⢿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣤⣄⣀⡀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⢺⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⠀⠉⠉⠙⠋⠀⠀⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣤⣤⣀⣀⡀⠀⠀⣰⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣷⠀⢹⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⠉⠉⠀⠀⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣶⣤⣤⣀⣀⣀⣀⣰⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡟⠉⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⢀⣤⡄⠀⡀⠀⢹⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⢸⣿⡇⠀⣿⡄⠈⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡆⠀⢹⡇⠀⠟⠁⢀⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⣦⣸⡇⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
)

J = (
    "⣿⣿⣿⣿⣿⣍⠀⠉⠻⠟⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠓⠀⠀⢒⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿\n"
    "⣿⡿⠋⠋⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⢿⣿⣿⡿⣿⣿⡟⠋⠀⢀⣩\n"
    "⣿⣿⡄⠀⠀⠀⠀⠀⠁⡀⠀⠀⠀⠀⠈⠉⠛⢷⣭⠉⠁⠀⠀⣿⣿\n"
    "⣇⣀. INDIA🇮🇳INDIA🇮🇳⠆⠠..⠘⢷⣿⣿⣛⠐⣶⣿⣿\n"
    "⣿⣄⠀⣰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢀⣠⣿⣿⣿⣾⣿⣿⣿\n"
    "⣿⣿⣿⣿⠀⠀⠀⠀⡠⠀⠀⠀⠀⠀⢀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠄⠀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⣠⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⠀⠀⠂⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣇⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡆⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
)

K = (
    "───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───\n"
    "───█▒▒░░░░░░░░░▒▒█───\n"
    "────█░░█░░░░░█░░█────\n"
    "─▄▄──█░░░▀█▀░░░█──▄▄─\n"
    "█░░█─▀▄░░░░░░░▄▀─█░░█\n"
    "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
    "█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n"
    "█░░║║║╠─║─║─║║║║║╠─░░█\n"
    "█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n"
    "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n"
)

L = (
    "░░░░▓\n"
    "░░░▓▓\n"
    "░░█▓▓█\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░░██▓▓██\n"
    "░░██▓▓██\n"
    "░░██▓▓██\n"
    "░░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓███\n"
    "░░░░██▓▓████\n"
    "░░░░░██▓▓█████\n"
    "░░░░░░██▓▓██████\n"
    "░░░░░░███▓▓███████\n"
    "░░░░░████▓▓████████\n"
    "░░░░█████▓▓█████████\n"
    "░░░█████░░░█████●███\n"
    "░░████░░░░░░░███████\n"
    "░░███░░░░░░░░░██████\n"
    "░░██░░░░░░░░░░░████\n"
    "░░░░░░░░░░░░░░░░███\n"
    "░░░░░░░░░░░░░░░░░░░\n"
)


O = (
    "────██──────▀▀▀██\n"
    "──▄▀█▄▄▄─────▄▀█▄▄▄\n"
    "▄▀──█▄▄──────█─█▄▄\n"
    "─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n"
    "─▀───────▀▀─▀───────▀▀\n🚶🏻‍♂️🚶🏻‍♂️ɮʏɛ ʄʀɨɛռɖֆ.."
)

P = (
    "╭━━━┳╮╱╱╭╮╱╭━━━┳━━━╮\n"
    "┃╭━╮┃┃╱╭╯╰╮┃╭━╮┃╭━╮┃\n"
    "┃╰━━┫╰━╋╮╭╯┃┃╱┃┃╰━━╮\n"
    "╰━━╮┃╭╮┣┫┃╱┃┃╱┃┣━━╮┃\n"
    "┃╰━╯┃┃┃┃┃╰╮┃╰━╯┃╰━╯┃\n"
    "╰━━━┻╯╰┻┻━╯╰━━━┻━━━╯\n"
)


R = (
    "███████▄▄███████████▄\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓███░░░░░░░░░░░░█\n"
    "██████▀░░█░░░░██████▀\n"
    "░░░░░░░░░█░░░░█\n"
    "░░░░░░░░░░█░░░█\n"
    "░░░░░░░░░░░█░░█\n"
    "░░░░░░░░░░░█░░█\n"
    "░░░░░░░░░░░░▀▀\n"
)


@bot.on(admin_cmd(pattern=r"monster$"))
@bot.on(sudo_cmd(pattern="monster$", allow_sudo=True))
async def bluedevilmonster(monster):
    await edit_or_reply(monster, A)


@bot.on(admin_cmd(pattern=r"pig$"))
@bot.on(sudo_cmd(pattern="pig$", allow_sudo=True))
async def bluedevilpig(pig):
    await edit_or_reply(pig, B)


@bot.on(admin_cmd(pattern=r"gun$"))
@bot.on(sudo_cmd(pattern="gun$", allow_sudo=True))
async def bluedevilgun(gun):
    await edit_or_reply(gun, D)


@bot.on(admin_cmd(pattern=r"dog$"))
@bot.on(sudo_cmd(pattern="dog$", allow_sudo=True))
async def bluedevildog(dog):
    await edit_or_reply(dog, E)


@bot.on(admin_cmd(pattern=r"hello$"))
@bot.on(sudo_cmd(pattern="hello$", allow_sudo=True))
async def bluedevilhello(hello):
    await edit_or_reply(hello, F)


@bot.on(admin_cmd(pattern=r"hmf$"))
@bot.on(sudo_cmd(pattern="hmf$", allow_sudo=True))
async def bluedevilhmf(hmf):
    await edit_or_reply(hmf, G)


@bot.on(admin_cmd(pattern=r"couple$"))
@bot.on(sudo_cmd(pattern="couple$", allow_sudo=True))
async def bluedevilcouple(couple):
    await edit_or_reply(couple, H)


@bot.on(admin_cmd(pattern=r"sup$"))
@bot.on(sudo_cmd(pattern="sup$", allow_sudo=True))
async def bluedevilsupreme(supreme):
    await edit_or_reply(supreme, I)


@bot.on(admin_cmd(pattern=r"india$"))
@bot.on(sudo_cmd(pattern="india$", allow_sudo=True))
async def bluedevilindia(india):
    await edit_or_reply(india, J)


@bot.on(admin_cmd(pattern=r"wc$"))
@bot.on(sudo_cmd(pattern="wc$", allow_sudo=True))
async def bluedevilwelcome(welcome):
    await edit_or_reply(welcome, K)


@bot.on(admin_cmd(pattern=r"snk$"))
@bot.on(sudo_cmd(pattern="snk$", allow_sudo=True))
async def bluedevilsnake(snake):
    await edit_or_reply(snake, L)


@bot.on(admin_cmd(pattern=r"bye$"))
@bot.on(sudo_cmd(pattern="bye$", allow_sudo=True))
async def bluedevilbye(bye):
    await edit_or_reply(bye, O)


@bot.on(admin_cmd(pattern=r"shitos$"))
@bot.on(sudo_cmd(pattern="shitos$", allow_sudo=True))
async def bluedevilshitos(shitos):
    await edit_or_reply(shitos, P)


@bot.on(admin_cmd(pattern=r"dislike$"))
@bot.on(sudo_cmd(pattern="dislike$", allow_sudo=True))
async def bluedevildislike(dislike):
    await edit_or_reply(dislike, R)
    
    
CMD_HELP.update(
    {
        "art": "__**PLUGIN NAME :** Art__\
\n\n📌** CMD ➥** `.killer` <text>\
\n**USAGE   ➥  **Be a warrior & kill enimes.\
\n\n📌** CMD ➥** `.ded` <text>\
\n**USAGE   ➥  **Hang yourself.\
\n\n📌** CMD ➥** `.elove` | `.monster` | `.pig` | `.gun` | `.dog` | `.hello` | `.hmf` | `.couple` | `.sup` | `.india` | `.wc` | `.snk` | `.bye` | `.shitos` | `.dislike`\
\n\n**USAGE   ➥  **These are arts,use & see"
    }
)
