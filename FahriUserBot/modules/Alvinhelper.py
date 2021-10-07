""" Userbot module for other small commands. """
from FahriUserBot import CMD_HELP, ALIVE_NAME
from FahriUserBot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^;mhelp$")
async def usit(e):
    await e.edit(
        f"**Hi master {DEFAULTUSER} If You Don't Know The Command To Order Me Type** `;help` Or you can ask for help to:\n"
        "\n[Telegram](t.me/Alvin_junior)"
        "\n[Group Support](t.me/Alvin_image_editor_group)"
        " | [Updates Channel](t.me/t.me/Alvin_image_editor)"
        "\n[Repo](https://github.com/fahrial2310/Fahri-Userbot)"
        "\n\n[Instagram](https://www.instagram.com/fahri2310/)"
        " | [Github](https://github.com/fahrial2310)"
        " | [Youtube](https://bit.ly/Alvin_JuniorYT)"
    )
    #don't edit or delete this


@register(outgoing=True, pattern="^;vars$")
async def var(m):
    await m.edit(
        f"**Here List of Vars From {DEFAULTUSER}:**\n"
        "\n[LIST VARS](https://github.com/fahrial2310/Fahri-UserBot/blob/FahriUserBot/varshelper.txt)")


CMD_HELP.update({
    "helpers":
    ";mhelp\
\nexplanation: Help For Fahri-Userbot.\
\n;vars\
\nexplanation: To View Multiple List of Vars."
})
