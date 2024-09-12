import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = 6092505
API_HASH = "98d119a0bebd325358589b62461e41a2"
SESSION = "BQBc9tkAcOZVG6fUS3ktpitZf1QmjI6cemtmMI_ccwTtAgS4kEhn5N7alxRZx-7Rs0RH_hr1Ax-4dgkh5SI8n9ibLfJiaoUAlrfti7Afr_Bj9iRTX2Fc9_eNbQr171N9inhdfWdg9vyrdsrOFGuSDuKwuqfSRYJoNTXB0pEj1JLqoZoRsDOwyfsMLvPTVLQtoG8iTkXt4QAwHgcl5ixvCbFI5q9hqXaDACwlJOJ8c14yJv9nysMWgiojZZzJLiqPq8qXVizul-J2SgOJsbH4TK79mMZOIodXkZIIUrs0mvwqcMZ8i5RtesljOz9iCG_oKumuJ7nPTJMbsMIrwd4C30Jm0O9QAAAAG8RaeeAA"
HNDLR = os.getenv("HNDLR", "/")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicAndVideo"))
call_py = PyTgCalls(bot)
