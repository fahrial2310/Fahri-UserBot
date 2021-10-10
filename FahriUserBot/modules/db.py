""" Userbot module for getting information about the server. """

from platform import uname


from FahriUserBot import ALIVE_NAME, BOT_VER, is_mongo_alive, is_redis_alive
from FahriUserBot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^;db$")
async def amireallydbs(dbs):
    if not is_mongo_alive() and not is_redis_alive():
        db = "Both Mongo and Redis Database seems to be failing!"
    elif not is_mongo_alive():
        db = "Mongo DB seems to be failing!"
    elif not is_redis_alive():
        db = "Redis Cache seems to be failing!"
    else:
        db = "Databases functioning normally!"
    await dbs.edit(""
                   f"**User:** `{DEFAULTUSER}` \n"
                   f"**Status Database:** `{db}`\n"
                   f"**Alvin-Userbot:** `{BOT_VER}`"
                   "")
