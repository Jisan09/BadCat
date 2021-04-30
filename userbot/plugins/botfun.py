import asyncio

game_code = ["ttt", "ttf", "cf", "rps", "rpsls", "rr", "c", "pc"]
button = ["0", "1", "2", "3", "4", "5", "6", "7"]
game_name = [
    "Tic-Tac-Toe",
    "Tic-Tac-Four",
    "Connect Four",
    "Rock-Paper-Scissors",
    "Rock-Paper-Scissors-Lizard-Spock",
    "Russian Roulette",
    "Checkers",
    "Pool Checkers",
]
game_list = "1.`ttt` :- Tic-Tac-Toe\n2.`ttf` :- Tic-Tac-Four\n3.`cf` :- Connect Four\n4.`rps` :- Rock-Paper-Scissors\n5.`rpsls` :- Rock-Paper-Scissors-Lizard-Spock\n6.`rr` :- Russian Roulette\n7.`c` :- Checkers\n8.`pc` :- Pool Checkers"


@bot.on(admin_cmd(pattern="game(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="game(?: |$)(.*)", allow_sudo=True))
async def igame(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    data = dict(zip(game_code, button))
    name = dict(zip(game_code, game_name))
    if not input_str:
        await edit_delete(
            event, f"**Available Game Codes & Names :-**\n\n{game_list}", time=60
        )
        return
    if input_str not in game_code:
        catevent = await edit_or_reply(event, "`Give me a correct game code...`")
        await asyncio.sleep(1)
        await edit_delete(
            catevent, f"**Available Game Codes & Names :-**\n\n{game_list}", time=60
        )
    else:
        game = data[input_str]
        gname = name[input_str]
        await edit_or_reply(
            event, f"**Game code `{input_str}` is selected for game:-** __{gname}__"
        )
        await asyncio.sleep(1)
        bot = "@inlinegamesbot"
        results = await event.client.inline_query(bot, gname)
        await results[int(game)].click(event.chat_id)
        await event.delete()


@bot.on(admin_cmd(pattern="honk(.*)"))
@bot.on(sudo_cmd(pattern="honk(.*)", allow_sudo=True))
async def pussycat(event):
    if event.fwd_from:
        return
    noob = event.pattern_match.group(1)
    if not noob:
        get = await event.get_reply_message()
        noob = get.text
    if not noob:
        await edit_delete(event, "What honk suppose to say?? ,Give text..", time=10)
        return
    bot = "@honka_says_bot"
    results = await event.client.inline_query(bot, f"{noob}.")
    await results[0].click(event.chat_id)
    await event.delete()


@bot.on(admin_cmd(pattern="twt(.*)"))
@bot.on(sudo_cmd(pattern="twt(.*)", allow_sudo=True))
async def pussycat(event):
    if event.fwd_from:
        return
    noob = event.pattern_match.group(1)
    if not noob:
        get = await event.get_reply_message()
        noob = get.text
    if not noob:
        await edit_delete(event, "What i suppose to Tweet?? ,Give text..", time=10)
        return
    bot = "@TwitterStatusBot"
    results = await event.client.inline_query(bot, noob)
    await results[0].click(event.chat_id)
    await event.delete()


CMD_HELP.update(
    {
        "botfun": "__**PLUGIN NAME :** Bot Fun__\
      \n\n📌** CMD ➥** `.game` <game code>\
      \n**USAGE   ➥  **Start an inline game by inlinegamebot. \
      \n\n📌** CMD ➥** `.honk` <type a text / reply to text>\
      \n**USAGE   ➥  **Honk will reply with your text.\
      \n\n📌** CMD ➥** `.twt` <type a text / reply to text>\
      \n**USAGE   ➥  **Tweet your text."
    }
)
