import time, re
from config import BOT_USERNAME
from pyrogram.enums import MessageEntityType
from pyrogram import filters
from pyrogram.types import Message
from DanteMusic import app
from DanteMusic.mongo.readable_time import get_readable_time
from DanteMusic.mongo.afkdb import add_afk, is_afk, remove_afk



@app.on_message(filters.command(["afk", "brb"], prefixes=["/", "!", ""]))
async def active_afk(_, message: Message):
    if message.sender_chat:
        return
    user_id = message.from_user.id
    verifier, reasondb = await is_afk(user_id)
    if verifier:
        await remove_afk(user_id)
        try:
            afktype = reasondb["type"]
            timeafk = reasondb["time"]
            data = reasondb["data"]
            reasonafk = reasondb["reason"]
            seenago = get_readable_time((int(time.time() - timeafk)))
            if afktype == "text":
                send = await message.reply_text(
                    f"<b><blockquote>**{message.from_user.first_name}**\nKembali online dan tidak aktif selama {seenago}</b></blockquote>",
                    disable_web_page_preview=True,
                )
            if afktype == "text_reason":
                send = await message.reply_text(
                    f"<b><blockquote>**{message.from_user.first_name}**\nKembali online dan tidak aktif selama {seenago}\n\n alasan : `{reasonafk}`</b></blockquote>",
                    disable_web_page_preview=True,
                )
            if afktype == "animation":
                if str(reasonafk) == "None":
                    send = await message.reply_animation(
                        data,
                        caption=f"<b><blockquote>**{message.from_user.first_name}**\nkembali online dan tidak aktif selama  {seenago}</b></blockquote>",
                    )
                else:
                    send = await message.reply_animation(
                        data,
                        caption=f"<b><blockquote>**{message.from_user.first_name}**\nkembali online dan pergi  {seenago}\n\nalasan: `{reasonafk}`</b></blockquote>",
                    )
            if afktype == "photo":
                if str(reasonafk) == "None":
                    send = await message.reply_photo(
                        photo=f"downloads/{user_id}.jpg",
                        caption=f"<b><blockquote>**{message.from_user.first_name}**\nKembali online dan tidak aktif selama {seenago}</b></blockquote>",
                    )
                else:
                    send = await message.reply_photo(
                        photo=f"downloads/{user_id}.jpg",
                        caption=f"<b><blockquote>**{message.from_user.first_name}**\nKembali online dan pergi {seenago}\n\nalasan: `{reasonafk}`</b></blockquote>",
                    )
        except Exception:
            send = await message.reply_text(
                f"<b><blockquote>**{message.from_user.first_name}**\nKembali online.</b></blockquote>",
                disable_web_page_preview=True,
            )

    if len(message.command) == 1 and not message.reply_to_message:
        details = {
            "type": "text",
            "time": time.time(),
            "data": None,
            "reason": None,
        }
    elif len(message.command) > 1 and not message.reply_to_message:
        _reason = (message.text.split(None, 1)[1].strip())[:100]
        details = {
            "type": "text_reason",
            "time": time.time(),
            "data": None,
            "reason": _reason,
        }
    elif len(message.command) == 1 and message.reply_to_message.animation:
        _data = message.reply_to_message.animation.file_id
        details = {
            "type": "animation",
            "time": time.time(),
            "data": _data,
            "reason": None,
        }
    elif len(message.command) > 1 and message.reply_to_message.animation:
        _data = message.reply_to_message.animation.file_id
        _reason = (message.text.split(None, 1)[1].strip())[:100]
        details = {
            "type": "animation",
            "time": time.time(),
            "data": _data,
            "reason": _reason,
        }
    elif len(message.command) == 1 and message.reply_to_message.photo:
        await app.download_media(
            message.reply_to_message, file_name=f"{user_id}.jpg"
        )
        details = {
            "type": "photo",
            "time": time.time(),
            "data": None,
            "reason": None,
        }
    elif len(message.command) > 1 and message.reply_to_message.photo:
        await app.download_media(
            message.reply_to_message, file_name=f"{user_id}.jpg"
        )
        _reason = message.text.split(None, 1)[1].strip()
        details = {
            "type": "photo",
            "time": time.time(),
            "data": None,
            "reason": _reason,
        }
    elif len(message.command) == 1 and message.reply_to_message.sticker:
        if message.reply_to_message.sticker.is_animated:
            details = {
                "type": "text",
                "time": time.time(),
                "data": None,
                "reason": None,
            }
        else:
            await app.download_media(
                message.reply_to_message, file_name=f"{user_id}.jpg"
            )
            details = {
                "type": "photo",
                "time": time.time(),
                "data": None,
                "reason": None,
            }
    elif len(message.command) > 1 and message.reply_to_message.sticker:
        _reason = (message.text.split(None, 1)[1].strip())[:100]
        if message.reply_to_message.sticker.is_animated:
            details = {
                "type": "text_reason",
                "time": time.time(),
                "data": None,
                "reason": _reason,
            }
        else:
            await app.download_media(
                message.reply_to_message, file_name=f"{user_id}.jpg"
            )
            details = {
                "type": "photo",
                "time": time.time(),
                "data": None,
                "reason": _reason,
            }
    else:
        details = {
            "type": "text",
            "time": time.time(),
            "data": None,
            "reason": None,
        }

    await add_afk(user_id, details)    
    await message.reply_text(f"<b><blockquote>{message.from_user.first_name} Sekarang afk!</b></blockquote>")




chat_watcher_group = 1


@app.on_message(
    ~filters.me & ~filters.bot & ~filters.via_bot,
    group=chat_watcher_group,
)
async def chat_watcher_func(_, message):
    if message.sender_chat:
        return
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    if message.entities:
        possible = ["/afk", f"/afk@{BOT_USERNAME}"]
        message_text = message.text or message.caption
        for entity in message.entities:
            if entity.type == MessageEntityType.BOT_COMMAND:
                if (message_text[0 : 0 + entity.length]).lower() in possible:
                    return

    msg = ""
    replied_user_id = 0


    
    verifier, reasondb = await is_afk(user_id)
    if verifier:
        await remove_afk(user_id)
        try:
            afktype = reasondb["type"]
            timeafk = reasondb["time"]
            data = reasondb["data"]
            reasonafk = reasondb["reason"]
            seenago = get_readable_time((int(time.time() - timeafk)))
            if afktype == "text":
                msg += f"<b><blockquote>**{user_name[:25]}**\nkembali online dan tidak aktif selama  {seenago}\n\n</b></blockquote>"
            if afktype == "text_reason":
                msg += f"<b><blockquote>**{user_name[:25]}**\nkembali online dan tidak aktif selama {seenago}\n\nalasan: `{reasonafk}`\n\n</b></blockquote>"
            if afktype == "animation":
                if str(reasonafk) == "None":
                    send = await message.reply_animation(
                        data,
                        caption=f"<b><blockquote>**{user_name[:25]}**\nKembali online dan tidak aktif selama  {seenago}\n\n</b></blockquote>",
                    )
                else:
                    send = await message.reply_animation(
                        data,
                        caption=f"<b><blockquote>**{user_name[:25]}**\nkembali online dan tidak aktif selama {seenago}\n\nalasan: `{reasonafk}`\n\n</b></blockquote>",
                    )
            if afktype == "photo":
                if str(reasonafk) == "None":
                    send = await message.reply_photo(
                        photo=f"downloads/{user_id}.jpg",
                        caption=f"<b><blockquote>**{user_name[:25]}**\nkembali online dan tidak aktif {seenago}\n\n</b></blockquote>",
                    )
                else:
                    send = await message.reply_photo(
                        photo=f"downloads/{user_id}.jpg",
                        caption=f"<b><blockquote>**{user_name[:25]}**\nkembali online dan tidak aktif selama {seenago}\n\nalasan: `{reasonafk}`\n\n</b></blockquote>",
                    )
        except:
            msg += f"<b><blockquote>**{user_name[:25]}**\nKembali online\n\nSelamat datang kembali!</b></blockquote>"


    if message.reply_to_message:
        try:
            replied_first_name = message.reply_to_message.from_user.first_name
            replied_user_id = message.reply_to_message.from_user.id
            verifier, reasondb = await is_afk(replied_user_id)
            if verifier:
                try:
                    afktype = reasondb["type"]
                    timeafk = reasondb["time"]
                    data = reasondb["data"]
                    reasonafk = reasondb["reason"]
                    seenago = get_readable_time((int(time.time() - timeafk)))
                    if afktype == "text":
                        msg += (
                            f"<b><blockquote>**{replied_first_name[:25]}**Sedang afk online {seenago}\n\n</b></blockquote>"
                        )
                    if afktype == "text_reason":
                        msg += f"<b><blockquote>**{replied_first_name[:25]}**Telah afk sejak itu {seenago}\n\nalasan: `{reasonafk}`\n\n</b></blockquote>"
                    if afktype == "animation":
                        if str(reasonafk) == "None":
                            send = await message.reply_animation(
                                data,
                                caption=f"<b><blockquote>**{replied_first_name[:25]}**ᴇ {seenago}\n\n</b></blockquote>",
                            )
                        else:
                            send = await message.reply_animation(
                                data,
                                caption=f"<b><blockquote>**{replied_first_name[:25]}**Telah afk sejak {seenago}\n\nalasan: `{reasonafk}`\n\n</b></blockquote>",
                            )
                    if afktype == "photo":
                        if str(reasonafk) == "None":
                            send = await message.reply_photo(
                                photo=f"downloads/{replied_user.id}.jpg",
                                caption=f"<b><blockquote>**{replied_first_name[:25]}**Telah kembali sejak {seenago}\n\n</b></blockquote>",
                            )
                        else:
                            send = await message.reply_photo(
                                photo=f"downloads/{replied_user.id}.jpg",
                                caption=f"<b><blockquote>**{replied_first_name[:25]}**Telah afk sejak itu  {seenago}\n\nalasan: `{reasonafk}`\n\n</b></blockquote>",
                            )
                except Exception:
                    msg += f"<b><blockquote>**{replied_first_name}**Telah afk\ntunggu.\n\n</b></blockquote>"
        except:
            pass

    if message.entities:
        entity = message.entities
        j = 0
        for x in range(len(entity)):
            if (entity[j].type) == MessageEntityType.MENTION:
                found = re.findall("@([_0-9a-zA-Z]+)", message.text)
                try:
                    get_user = found[j]
                    user = await app.get_users(get_user)
                    if user.id == replied_user_id:
                        j += 1
                        continue
                except:
                    j += 1
                    continue
                verifier, reasondb = await is_afk(user.id)
                if verifier:
                    try:
                        afktype = reasondb["type"]
                        timeafk = reasondb["time"]
                        data = reasondb["data"]
                        reasonafk = reasondb["reason"]
                        seenago = get_readable_time((int(time.time() - timeafk)))
                        if afktype == "text":
                            msg += (
                                f"<b><blockquote>**{user.first_name[:25]}** sudah afk sejak itu {seenago}\n\n</b></blockquote>"
                            )
                        if afktype == "text_reason":
                            msg += f"<b><blockquote>**{user.first_name[:25]}** Telah afk sejak itu  {seenago}\n\nalasan: `{reasonafk}`\n\n</b></blockquote>"
                        if afktype == "animation":
                            if str(reasonafk) == "None":
                                send = await message.reply_animation(
                                    data,
                                    caption=f"<b><blockquote>**{user.first_name[:25]}** Telah afk sejak {seenago}\n\n</b></blockquote>",
                                )
                            else:
                                send = await message.reply_animation(
                                    data,
                                    caption=f"<b><blockquote>**{user.first_name[:25]}** Telah afk sejak {seenago}\n\nalasan: `{reasonafk}`\n\n</b></blockquote>",
                                )
                        if afktype == "photo":
                            if str(reasonafk) == "None":
                                send = await message.reply_photo(
                                    photo=f"downloads/{user.id}.jpg",
                                    caption=f"<b><blockquote>**{user.first_name[:25]}** Telah afk sejak {seenago}\n\n</b></blockquote>",
                                )
                            else:
                                send = await message.reply_photo(
                                    photo=f"downloads/{user.id}.jpg",
                                    caption=f"<b><blockquote>**{user.first_name[:25]}** Telah afk sejak {seenago}\n\nalasan: `{reasonafk}`\n\n</b></blockquote>",
                                )
                    except:
                        msg += f"<b><blockquote>**{user.first_name[:25]}** ɪs ᴀғᴋ\n\n</b></blockquote>"
            elif (entity[j].type) == MessageEntityType.TEXT_MENTION:
                try:
                    user_id = entity[j].user.id
                    if user_id == replied_user_id:
                        j += 1
                        continue
                    first_name = entity[j].user.first_name
                except:
                    j += 1
                    continue
                verifier, reasondb = await is_afk(user_id)
                if verifier:
                    try:
                        afktype = reasondb["type"]
                        timeafk = reasondb["time"]
                        data = reasondb["data"]
                        reasonafk = reasondb["reason"]
                        seenago = get_readable_time((int(time.time() - timeafk)))
                        if afktype == "text":
                            msg += f"<b><blockquote>**{first_name[:25]}** Telah afk sejak {seenago}\n\n</b></blockquote>"
                        if afktype == "text_reason":
                            msg += f"<b><blockquote>**{first_name[:25]}** Telah afk sejak {seenago}\n\nalasan: `{reasonafk}`\n\n</b></blockquote>"
                        if afktype == "animation":
                            if str(reasonafk) == "None":
                                send = await message.reply_animation(
                                    data,
                                    caption=f"<b><blockquote>**{first_name[:25]}** Telah afk sejak {seenago}\n\n</b></blockquote>",
                                )
                            else:
                                send = await message.reply_animation(
                                    data,
                                    caption=f"*<b><blockquote>*{first_name[:25]}** Telah afk sejak {seenago}\n\nalasan: `{reasonafk}`\n\n</b></blockquote>",
                                )
                        if afktype == "photo":
                            if str(reasonafk) == "None":
                                send = await message.reply_photo(
                                    photo=f"downloads/{user_id}.jpg",
                                    caption=f"<b><blockquote>**{first_name[:25]}** Telah afk sejak  {seenago}\n\n</b></blockquote>",
                                )
                            else:
                                send = await message.reply_photo(
                                    photo=f"downloads/{user_id}.jpg",
                                    caption=f"<b><blockquote>**{first_name[:25]}** Telah afk sejak  {seenago}\n\nʀᴇᴀsᴏɴ: `{reasonafk}`\n\n</b></blockquote>",
                                )
                    except:
                        msg += f"<b><blockquote>**{first_name[:25]}** ɪs ᴀғᴋ\n\n</b></blockquote>"
            j += 1
    if msg != "":
        try:
            send = await message.reply_text(msg, disable_web_page_preview=True)
        except:
            return


__MODULE__ = "Afk"
__HELP__ = """<blockquote><b><u>Afk Commands:</u></b>
/afk - ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴀғᴋ.
/unafk - ᴜɴᴛᴜᴋ ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ ᴀғᴋ.
/brb - ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ʙʀʙ.</b></blockquote>
"""