import asyncio
from os import remove
from sys import executable

from FahriUserBot import BOTLOG, BOTLOG_CHATID, CMD_HELP, TERM_ALIAS
from FahriUserBot.events import register


@register(outgoing=True, pattern=r"^\;eval(?: |$)(.*)")
async def evaluate(query):
    if query.is_channel and not query.is_group:
        return await query.edit("_Eval isn't permitted on channels_")

    if query.pattern_match.group(1):
        expression = query.pattern_match.group(1)
    else:
        return await query.edit("_Give an expression to evaluate._")

    if expression in ("userbot.session", "config.env"):
        return await query.edit("_That's a dangerous operation! Not Permitted!_")

    try:
        evaluation = str(eval(expression))
        if evaluation:
            if isinstance(evaluation, str):
                if len(evaluation) >= 4096:
                    file = open("output.txt", "w+")
                    file.write(evaluation)
                    file.close()
                    await query.client.send_file(
                        query.chat_id,
                        "output.txt",
                        reply_to=query.id,
                        caption="_Output too large, sending as file_",
                    )
                    remove("output.txt")
                    return
                await query.edit(
                    "**Query: **\n`"
                    f"{expression}"
                    "`\n**Result: **\n`"
                    f"{evaluation}"
                    "`"
                )
        else:
            await query.edit(
                "**Query: **\n`"
                f"{expression}"
                "`\n**Result: **\n_No Result Returned/False_"
            )
    except Exception as err:
        await query.edit(
            "**Query: **\n`" f"{expression}" "`\n**Exception: **\n" f"`{err}`"
        )

    if BOTLOG:
        await query.client.send_message(
            BOTLOG_CHATID, f"Eval query {expression} was executed successfully"
        )


@register(outgoing=True, pattern=r"^\;exec(?: |$)([\s\S]*)")
async def run(run_q):
    code = run_q.pattern_match.group(1)

    if run_q.is_channel and not run_q.is_group:
        return await run_q.edit("_Exec isn't permitted on channels!_")

    if not code:
        return await run_q.edit(
            "_At least a variable is required to"
            "execute. Use .help exec for an example._"
        )

    if code in ("userbot.session", "config.env"):
        return await run_q.edit("_That's a dangerous operation! Not Permitted!_")

    if len(code.splitlines()) <= 5:
        codepre = code
    else:
        clines = code.splitlines()
        codepre = (
            clines[0] +
            "\n" +
            clines[1] +
            "\n" +
            clines[2] +
            "\n" +
            clines[3] +
            "...")

    command = "".join(f"\n {l}" for l in code.split("\n.strip()"))
    process = await asyncio.create_subprocess_exec(
        executable,
        "-c",
        command.strip(),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    result = str(stdout.decode().strip()) + str(stderr.decode().strip())

    if result:
        if len(result) > 4096:
            file = open("output.txt", "w+")
            file.write(result)
            file.close()
            await run_q.client.send_file(
                run_q.chat_id,
                "output.txt",
                reply_to=run_q.id,
                caption="_Output too large, sending as file_",
            )
            remove("output.txt")
            return
        await run_q.edit(
            "**Query: **\n`" f"{codepre}" "`\n**Result: **\n`" f"{result}" "`"
        )
    else:
        await run_q.edit(
            "**Query: **\n`" f"{codepre}" "`\n**Result: **\n_No Result Returned/False_"
        )

    if BOTLOG:
        await run_q.client.send_message(
            BOTLOG_CHATID, "Exec query " + codepre + " was executed successfully"
        )


@register(outgoing=True, pattern=r"^\;term(?: |$)(.*)")
async def terminal_runner(term):
    curruser = TERM_ALIAS
    command = term.pattern_match.group(1)
    try:
        from os import geteuid

        uid = geteuid()
    except ImportError:
        uid = "This ain't it chief!"

    if term.is_channel and not term.is_group:
        return await term.edit("_Term commands aren't permitted on channels!_")

    if not command:
        return await term.edit(
            "_Give a command or use .help term for an example._"
        )

    if command in ("userbot.session", "config.env"):
        return await term.edit("_That's a dangerous operation! Not Permitted!_")

    process = await asyncio.create_subprocess_shell(
        command, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    result = str(stdout.decode().strip()) + str(stderr.decode().strip())

    if len(result) > 4096:
        output = open("output.txt", "w+")
        output.write(result)
        output.close()
        await term.client.send_file(
            term.chat_id,
            "output.txt",
            reply_to=term.id,
            caption="_Output too large, sending as file_",
        )
        remove("output.txt")
        return

    if uid == 0:
        await term.edit("`" f"{curruser}:~# {command}" f"\n{result}" "`")
    else:
        await term.edit("`" f"{curruser}:~$ {command}" f"\n{result}" "`")


"""
    if BOTLOG:
        await term.client.send_message(
            BOTLOG_CHATID,
            "Terminal Command " + command + " was executed sucessfully",
        )
"""

CMD_HELP.update({"eval": ">;eval 2 + 3"
                 "\nUsage: Evalute mini-expressions.",
                 "exec": ">;exec print('hello')"
                 "\nUsage: Execute small python scripts.",
                 "term": ">;term <cmd>"
                 "\nUsage: Run bash commands and scripts on your server.",
                 })
