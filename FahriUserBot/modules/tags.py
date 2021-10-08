import asyncio
from telethon.tl.types import ChannelParticipantAdmin as admin
from telethon.tl.types import ChannelParticipantCreator as owner
from telethon.tl.types import UserStatusOffline as off
from telethon.tl.types import UserStatusOnline as onn
from telethon.tl.types import UserStatusRecently as rec
from telethon.utils import get_display_name
from telethon import custom, events
from FahriUserBot import CMD_HELP, bot
from FahriUserBot.events import register

@register(outgoing=True, pattern=r"^;tags(?: |$)(on|off|all|bots|rec|admins|owner)?")
async def _(event):
    okk = event.text
    lll = event.pattern_match.group(2)
    users = 0
    o = 0
    nn = 0
    rece = 0
    if lll:
        xx = f"{lll}"
    else:
        xx = ""
    async for bb in bot.iter_participants(event.chat_id, 99):
        users = users + 1
        x = bb.status
        y = bb.participant
        if isinstance(x, on):
            o = o + 1
            if "on" in okk:
                xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
        if isinstance(x, off):
            nn = nn + 1
            if "off" in okk:
                if not (bb.bot or bb.deleted):
                    xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
        if isinstance(x, rec):
            rece = rece + 1
            if "rec" in okk:
                if not (bb.bot or bb.deleted):
                    xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
        if isinstance(y, owner):
            if "admin" or "owner" in okk:
                xx += f"\n꧁[{get_display_name(bb)}](tg://user?id={bb.id})꧂"
        if isinstance(y, admins):
            if "admin" in okk:
                if not bb.deleted:
                    xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
        if "all" in okk:
            if not (bb.bot or bb.deleted):
                xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
        if "bots" in okk:
            if bb.bot:
                xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
    await event.client.send_message(e.chat_id, xx)
    await event.delete()


CMD_HELP.update(
    {
        "tags": "**Modules:** Tags\
        \n\n**explanation:** ;tags all\
        \n**explanation:** Tag top 100 Member di grup.\
        \n\n**explanation:** ;tags owner\
        \n**explanation:** Tag Owner group chat\
        \n\n**explanation: **;tags admins\
        \n**explanation:** Tag Admins group chat.\
        \n\n**explanation:** ;tags bots\
        \n**explanation:** Tag Bot di dalam grup.\
        \n\n**explanation:** ;tags rec\
        \n**explanation: **Tag Member yang baru aktif.\
        \n\n**explanation:** ;tags on\
        \n**explanation: **Tag Member Yang Sedang On (hanya berfungsi jika privasi dimatikan)\
        \n\n**explanation:** ;tags off\
        \n**explanation: **Tag Member Yang Sedang Off (hanya berfungsi jika privasi dimatikan)\
        "
    }
)
