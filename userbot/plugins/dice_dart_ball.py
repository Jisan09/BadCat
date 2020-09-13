# imported from uniborg credit goes to spechide
from telethon.tl.types import InputMediaDice

from .. import CMD_HELP
from ..utils import admin_cmd, sudo_cmd

# EMOJI CONSTANTS
DART_E_MOJI = "🎯"
DICE_E_MOJI = "🎲"
BALL_E_MOJI = "🏀"
FOOT_E_MOJI = "⚽️"
# EMOJI CONSTANTS


@borg.on(
    admin_cmd(
        pattern=f"({DART_E_MOJI}|{DICE_E_MOJI}|{BALL_E_MOJI}|{FOOT_E_MOJI}) ?(.*)"
    )
)
@bot.on(
    sudo_cmd(
        pattern=f"({DART_E_MOJI}|{DICE_E_MOJI}|{BALL_E_MOJI}|{FOOT_E_MOJI}) ?(.*)",
        allow_sudo=True,
    )
)
async def _(event):
    if event.fwd_from:
        return
    reply_message = event
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
    emoticon = event.pattern_match.group(1)
    input_str = event.pattern_match.group(2)
    await event.delete()
    r = await reply_message.reply(file=InputMediaDice(emoticon=emoticon))
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await reply_message.reply(file=InputMediaDice(emoticon=emoticon))
        except BaseException:
            pass


CMD_HELP.update(
    {
        "dice_dart_ball": "__**PLUGIN NAME :** dice_dart_ball__\
    \n\n📌** CMD ➥** `.🎯` [1-6]\
    \n**USAGE   ➥  **Each number shows different animation\
    \n\n📌** CMD ➥** `.🎲` [1-6]\
    \n**USAGE   ➥  **Each number shows different animation\
    \n\n📌** CMD ➥** `.🏀` [1-5]\
    \n**USAGE   ➥  **Each number shows different animation\
    \n\n📌** CMD ➥** `.⚽️` [1-5]\
    \n**USAGE   ➥  **Each number shows different animation\
    "
    }
)
