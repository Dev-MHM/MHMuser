# MHMuser
# Copyright (C) 2021-2022 DevMHM
#
# This file is a part of < https://github.com/Dev-MHM/MHMuser/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/MHMuser/MHMuser/blob/main/LICENSE/>.

from pyMHMuser import *
from pyMHMuser import _ult_cache
from pyMHMuser._misc import owner_and_sudos
from pyMHMuser._misc._assistant import asst_cmd, callback, in_pattern
from pyMHMuser.functions.helper import *
from pyMHMuser.functions.tools import get_stored_file
from telethon import Button, custom

from plugins import ATRA_COL
from strings import get_languages, get_string, language

OWNER_NAME = MHMup_bot.full_name
OWNER_ID = MHMup_bot.uid

AST_PLUGINS = {}


async def setit(event, name, value):
    try:
        udB.set_key(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    return [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
