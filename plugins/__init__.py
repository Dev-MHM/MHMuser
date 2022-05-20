# MHMuser
# Copyright (C) 2021-2022 DevMHM
#
# This file is a part of < https://github.com/Dev-MHM/MHMuser/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/MHMuser/MHMuser/blob/main/LICENSE/>.


import asyncio
import os
import time
from random import choice

import requests
from pyMHMuser import *
from pyMHMuser._misc._assistant import asst_cmd, callback, in_pattern
from pyMHMuser._misc._decorators import MHMup_cmd
from pyMHMuser._misc._wrappers import eod, eor
from pyMHMuser.dB import DEVLIST, MHMup_IMAGES
from pyMHMuser.functions.helper import *
from pyMHMuser.functions.info import *
from pyMHMuser.functions.misc import *
from pyMHMuser.functions.tools import *
from pyMHMuser.version import __version__, MHMup_version
from telethon import Button, events
from telethon.tl import functions, types

from strings import get_string

Redis = udB.get_key
con = TgConverter
quotly = Quotly()
OWNER_NAME = MHMup_bot.full_name
OWNER_ID = MHMup_bot.uid

LOG_CHANNEL = udB.get_key("LOG_CHANNEL")

INLINE_PIC = udB.get_key("INLINE_PIC")

if INLINE_PIC is None:
    INLINE_PIC = choice(MHMup_IMAGES)
elif INLINE_PIC == False:
    INLINE_PIC = None

Telegraph = telegraph_client()

List = []
Dict = {}
N = 0

STUFF = {}

# Chats, which needs to be ignore for some cases
# Considerably, there can be many
# Feel Free to Add Any other...

NOSPAM_CHAT = [
    -1001327032795,  # MHMuser
    -1001387666944,  # PyrogramChat
    -1001109500936,  # TelethonChat
    -1001050982793,  # Python
    -1001256902287,  # DurovsChat
    -1001473548283,  # SharingUserbot
]

KANGING_STR = [
    "Using Witchery to kang this sticker...",
    "Plagiarising hehe...",
    "Inviting this sticker over to my pack...",
    "Kanging this sticker...",
    "Hey that's a nice sticker!\nMind if I kang?!..",
    "Hehe me stel ur stiker...",
    "Ay look over there (☉｡☉)!→\nWhile I kang this...",
    "Roses are red violets are blue, kanging this sticker so my pack looks cool",
    "Imprisoning this sticker...",
    "Mr.Steal-Your-Sticker is stealing this sticker... ",
]

ATRA_COL = [
    "DarkCyan",
    "DeepSkyBlue",
    "DarkTurquoise",
    "Cyan",
    "LightSkyBlue",
    "Turquoise",
    "MediumVioletRed",
    "Aquamarine",
    "Lightcyan",
    "Azure",
    "Moccasin",
    "PowderBlue",
]