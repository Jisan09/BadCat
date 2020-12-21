"""Transfer Ownership of Channels
Available Commands:
.otransfer @username"""

import telethon.password as pwd_mod

# https://t.me/TelethonChat/140200
from telethon.tl import functions


@bot.on(admin_cmd(pattern="otransfer (.*)"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    user_name = event.pattern_match.group(1)
    current_channel = event.chat_id
    # not doing any validations, here FN
    # MBL
    try:
        pwd = await event.client(functions.account.GetPasswordRequest())
        my_srp_password = pwd_mod.compute_check(pwd, Config.TELE_GRAM_2FA_CODE)
        await event.client(
            functions.channels.EditCreatorRequest(
                channel=current_channel, user_id=user_name, password=my_srp_password
            )
        )
    except Exception as e:
        await event.edit(str(e))
    else:
        await event.edit("Transferred 🌚")


CMD_HELP.update(
    {
        "transfer_channel": "__**PLUGIN NAME :** Transfer_channel__\
        \n\n📌** CMD ➥** `.otransfer` [username to whom you want to transfer]\
        \n**USAGE   ➥  **Transfers ownership to the given username for this set this var `TELE_GRAM_2FA_CODE` in heroku with your 2-step verification code \
        "
    }
)
