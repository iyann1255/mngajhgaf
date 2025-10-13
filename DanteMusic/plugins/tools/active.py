from pyrogram import filters
from pyrogram.types import Message

from strings import get_command
from DanteMusic import app
from DanteMusic.misc import SUDOERS
from DanteMusic.utils.database.memorydatabase import (
    get_active_chats,
    get_active_video_chats,
)

# Commands
ACTIVEVC_COMMAND = get_command("ACTIVEVC_COMMAND")
ACTIVEVIDEO_COMMAND = get_command("ACTIVEVIDEO_COMMAND")


@app.on_message(filters.command(ACTIVEVC_COMMAND) & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text("ɢᴇᴛᴛɪɴɢ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ...\nᴘʟᴇᴀsᴇ ʜᴏʟᴅ ᴏɴ.")
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "ᴘʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴘ"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += f"<blockquote><b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n</b></blockquote>"
        else:
            text += f"<blockquote><b>{j + 1}. {title}</b> [`{x}`]\n</b></blockquote>"
        j += 1
    if not text:
        await mystic.edit_text("ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ's")
    else:
        await mystic.edit_text(
            f"<blockquote><b>**ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ's:-**\n\n{text}</b></blockquote>",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(ACTIVEVIDEO_COMMAND) & SUDOERS)
async def activevi_(_, message: Message):
    mystic = await message.reply_text("ɢᴇᴛᴛɪɴɢ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ...\nᴘʟᴇᴀsᴇ ʜᴏʟᴅ ᴏɴ.")
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "ᴘʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴘ"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += f"<blockquote><b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n</b></blockquote>"
        else:
            text += f"<blockquote><b>{j + 1}. {title}</b> [`{x}`]\n</b></blockquote>"
        j += 1
    if not text:
        await mystic.edit_text("ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ's")
    else:
        await mystic.edit_text(
            f"<blockquote><b>**ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ's:-**\n\n{text}</b></blockquote>",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(["ac"]) & SUDOERS)
async def vc(client, message: Message):
    ac_audio = str(len(await get_active_chats()))
    ac_video = str(len(await get_active_video_chats()))
    await message.reply_text(
        f"<blockquote><b><u>ᴀᴄᴛɪᴠᴇ ᴄʜᴀᴛs ɪɴғᴏ</u></b> :\n\nᴠᴏɪᴄᴇ : {ac_audio}\nᴠɪᴅᴇᴏ  : {ac_video}</b></blockquote>"
    )


__MODULE__ = "Active"
__HELP__ = """<blockquote><b><u>Active Commands:</u>
/ac - <u>Cʜᴇᴄᴋ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ᴏɴ ʙᴏᴛ.</u>
/activevoice - <u>Cʜᴇᴄᴋ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ᴀɴᴅ ᴠɪᴅᴇᴏ ᴄᴀʟʟs ᴏɴ ʙᴏᴛ.v
/activevideo - <u>Cʜᴇᴄᴋ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄᴀʟʟs ᴏɴ ʙᴏᴛ.</u>
/stats - <u>Cʜᴇᴄᴋ Bᴏᴛs Sᴛᴀᴛs</u></blockquote>"""
