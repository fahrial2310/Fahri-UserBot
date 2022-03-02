from asyncio import sleep

from telethon.errors import rpcbaseerrors

from userbot import CMD_HELP

@register(outgoing=True, pattern=r"^\;del$")
async def delete_it(delme):
    msg_src = await delme.get_reply_message()
    if delme.reply_to_msg_id:
        try:
            await msg_src.delete()
            await delme.delete()
            """
            if BOTLOG:
                await delme.client.send_message(
                    BOTLOG_CHATID, "__This message has been deleted__")
            """
        except rpcbaseerrors.BadRequestError:
            await delme.edit("cannot delete message")
            """
            if BOTLOG:
                await delme.client.send_message(
                    BOTLOG_CHATID, "cannot delete message")
            """

@register(outgoing=True, pattern=r"^\;del 3s")
async def delete_it(delme):
    msg_src = await delme.get_reply_message()
    if delme.reply_to_msg_id:
        try:
            await delme.edit("This Message Will Deleted In 3(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 2(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 1(s)")
            await msg_src.delete()
            await delme.delete()
            """
            if BOTLOG:
                await delme.client.send_message(
                    BOTLOG_CHATID, "__This message has been deleted__")
            """
        except rpcbaseerrors.BadRequestError:
            await delme.edit("cannot delete message")
            """
            if BOTLOG:
                await delme.client.send_message(
                    BOTLOG_CHATID, "cannot delete message")
            """
            
@register(outgoing=True, pattern=r"^\;del 5s")
async def delete_it(delme):
    msg_src = await delme.get_reply_message()
    if delme.reply_to_msg_id:
        try:
            await delme.edit("This Message Will Deleted In 5(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 4(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 3(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 2(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 1(s)")
            await msg_src.delete()
            await delme.delete()
            """
            if BOTLOG:
                await delme.client.send_message(
                    BOTLOG_CHATID, "__This message has been deleted__")
            """
        except rpcbaseerrors.BadRequestError:
            await delme.edit("cannot delete message")
            """
            if BOTLOG:
                await delme.client.send_message(
                    BOTLOG_CHATID, "cannot delete message")
            """
            
@register(outgoing=True, pattern=r"^\;del 10s")
async def delete_it(delme):
    msg_src = await delme.get_reply_message()
    if delme.reply_to_msg_id:
        try:
            await delme.edit("This Message Will Deleted In 10(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 9(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 8(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 7(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 6(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 5(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 4(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 3(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 2(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 1(s)")
            await msg_src.delete()
            await delme.delete()
            """
            if BOTLOG:
                await delme.client.send_message(
                    BOTLOG_CHATID, "__This message has been deleted__")
            """
        except rpcbaseerrors.BadRequestError:
            await delme.edit("cannot delete message")
            """
            if BOTLOG:
                await delme.client.send_message(
                    BOTLOG_CHATID, "cannot delete message")
            """ 

@register(outgoing=True, pattern=r"^\;del 10s")
async def delete_it(delme):
    msg_src = await delme.get_reply_message()
    if delme.reply_to_msg_id:
        try:
            await delme.edit("This Message Will Deleted In 30(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 29(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 28(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 27(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 26(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 25(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 24(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 23(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 22(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 21(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 20(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 19(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 18(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 17(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 16(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 15(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 14(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 13(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 12(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 11(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 10(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 9(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 8(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 7(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 6(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 5(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 4(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 3(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 2(s)")
            await asyncio.sleep(1)
            await delme.edit("This Message Will Deleted In 1(s)")
            await msg_src.delete()
            await delme.delete()
            """
            if BOTLOG:
                await delme.client.send_message(
                    BOTLOG_CHATID, "__This message has been deleted__")
            """
        except rpcbaseerrors.BadRequestError:
            await delme.edit("cannot delete message")
            """
            if BOTLOG:
                await delme.client.send_message(
                    BOTLOG_CHATID, "cannot delete message")
            """
CMD_HELP.update({
    "delete":
    ";del\
    \nUsage: delete message.\
    \n;del 3s\
    \nUsage: delete message in 3 second.\
    \n;del 5s\
    \nUsage: delete message in 5 second.\
    \n;del 10s\
    \nUsage: delete message in 10 second.\
    \n;dal 30s\
    \nUsage: delete message in 30 second"
  }
)
