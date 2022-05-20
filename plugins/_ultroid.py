# MHMuser
# Copyright (C) 2021-2022 DevMHM
#
# This file is a part of < https://github.com/Dev-MHM/MHMuser/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/MHMuser/MHMuser/blob/main/LICENSE/>.

from telethon.errors import (
    BotMethodInvalidError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
)

from . import LOG_CHANNEL, LOGS, Button, asst, eor, get_string, MHMup_cmd

REPOMSG = """
• **MHMuser USERBOT** •\n
• Repo - [Click Here](https://github.com/Dev-MHM/MHMuser)
• Addons - [Click Here](https://github.com/Dev-MHM/MHMuserAddons)
• Support - @MHMuser
"""

RP_BUTTONS = [
    [
        Button.url(get_string("bot_3"), "https://github.com/Dev-MHM/MHMuser"),
        Button.url("Addons", "https://github.com/Dev-MHM/MHMuserAddons"),
    ],
    [Button.url("Support Group", "t.me/MHMuser")],
]

ULTSTRING = """🎇 **Thanks for Deploying MHMuser Userbot!**

• Here, are the Some Basic stuff from, where you can Know, about its Usage."""


@MHMup_cmd(
    pattern="repo$",
    manager=True,
)
async def repify(e):
    try:
        q = await e.client.inline_query(asst.me.username, "")
        await q[0].click(e.chat_id)
        return await e.delete()
    except (
        ChatSendInlineForbiddenError,
        ChatSendMediaForbiddenError,
        BotMethodInvalidError,
    ):
        pass
    except Exception as er:
        LOGS.info("Error while repo command : " + str(er))
    await e.eor(REPOMSG)


@MHMup_cmd(pattern="MHMuser$")
async def useMHMuser(rs):
    button = Button.inline("Start >>", "initft_2")
    msg = await asst.send_message(
        LOG_CHANNEL,
        ULTSTRING,
        file="https://telegra.ph/file/54a917cc9dbb94733ea5f.jpg",
        buttons=button,
    )
    if not (rs.chat_id == LOG_CHANNEL and rs.client._bot):
        await eor(rs, f"**[Click Here]({msg.message_link})**")
