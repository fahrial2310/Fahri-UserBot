""" Alvin Userbot help command """
import asyncio
from userbot import CMD_HELP
from userbot.events import register

modules = CMD_HELP

@register(outgoing=True, pattern="^;help(?: |$)(.*)")
async def help(Alvin):
    """ For .help command,"""
    args = Alvin.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await Alvin.edit(str(CMD_HELP[args]))
        else:
            await Alvin.edit("**sorry master,i don't have that command,type ;help ツ**")
            await asyncio.sleep(200)
            await Alvin.delete()
    else:
        await Alvin.edit("☠️")
        await asyncio.sleep(3)
        await Alvin.edit("**☠️MODULES☠️:**\n"
                        "`admin` | `adzan` | `afk` | `bored` | `vip` | `animation`|  `android` | `anime` | `anti_spambot` | `aria` | `ascii`|"
                        "`blacklist` | `carbon`  | `chat` | `delete` | `mutechat` | `corona` | `creating` | `deepfry` | `emogames`|"
                        "`eval` | `exec` | `term` | `fgban` | `federation` | `figlet` | `tags` | `filters` | `gban` | `gcast` | `googledrive` | `gcommit` | `github`|"
                        "`glitch` | `gps` | `hash` | `base64` | `hentai` | `heroku` | `id` | `memeimage` | `power`|"
                        "`lastfm` | `locks` | `master` | `aeshtetic` | `detect` | `mastergame` | `helpers` | `hazmat`|"
                        "`instagram` | `impostor` | `memes` | `misc` | `app` | `undelete` | `grab` | `clone`|"
                        "`randomprofil` | `song` | `tiny` | `tempmail` | `tiktok` | `wordcloud`|" 
                        "`lyrics` | `mega` | `justforfun` | `memify` | `mentions` | `purge` | `purgeme` | `edit`|"
                        "`sd` | `random` | `sleep` | `shutdown` | `repo`  |`readme` | `repeat` | `restart`|"
                        "`raw` | `nekobot` | `notes` | `off` | `phreaker` | `pm` | `profil` | `quotly`|  `rastick` | `resi` | `reverse` | `salam` | `sangmata`|"
                        "`santet` | `image_search` | `currency` | `google` | `wiki`| `ud` | `tts` | `translate`| `youtube` | `rip`|"
                        "`removebg` | `ocr` | `qrcode` | `barcode` | `paste` | `getpaste` | `nekobin` | `direct` | `screenshot` | `sed` | `snips` | `spammer` | `spotifynow` | `ssvideo`|"
                        "`stickers` | `stickers2` | `sysd` | `botver` | `pip` | `alive` | `tag_all` | `telegraph` | `timedate` | `torrent`|" 
                        "`transform` | `updater` |`downloader` | `waifu` | `wallpaper` | `weather`|"
                        "`webupload` | `welcome`|  `info` | `ping` | `signal` | `xiaomi` | `zipfile`")
        await Alvin.reply("\n**HOW TO USE????,** **EXAMPLE:**\n**TYPE** `;help afk` **FOR INFORMATION MODULES**GO TO**GROUP SUPPORT**\n[CLICK HERE TO GO](t.me/Alvin_Userbot_Group)")
        await asyncio.sleep(1000)
        await Alvin.delete()
