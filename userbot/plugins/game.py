import asyncio

from userbot import catub

from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id

plugin_category = "fun"

game_code = ["ttt", "ttf", "ex", "cf", "rps", "rpsls", "rr", "c", "pc"]
game_name = [
    "Tic-Tac-Toe",
    "Tic-Tac-Four",
    "Elephant XO",
    "Connect Four",
    "Rock-Paper-Scissors",
    "Rock-Paper-Scissors-Lizard-Spock",
    "Russian Roulette",
    "Checkers",
    "Pool Checkers",
]

game = dict(zip(game_code, game_name))


@catub.cat_cmd(
    pattern="game(?:\s|$)([\s\S]*)",
    command=("game", plugin_category),
    info={
        "header": "Play inline games",
        "description": "Start an inline game by inlinegamebot",
        "Game code & Name": game,
        "usage": "{tr}game <game code>",
        "examples": "{tr}game ttt ",
    },
)
async def igame(event):
    "Fun game by inline"
    reply_to_id = await reply_id(event)
    input_str = event.pattern_match.group(1)
    game_list = "".join(f"**{i}.** `{item}` :- __{game[item]}__\n" for i, item in enumerate(game, start=1))
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
        await edit_or_reply(
            event, f"**Game code `{input_str}` is selected for game:-** __{game[input_str]}__"
        )
        await asyncio.sleep(1)
        bot = "@inlinegamesbot"
        results = await event.client.inline_query(bot, input_str)
        await results[game_code.index(input_str)].click(event.chat_id, reply_to=reply_to_id)
        await event.delete()
