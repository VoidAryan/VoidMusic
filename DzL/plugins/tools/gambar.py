# Credits <https://github.com/IndomieGorengSatu>
# @indomiegenetik

import random
import os

from pyrogram import filters
from DzL import userbot, app

@app.on_message(filters.command("gurl"))
async def asupan(client, message):
    y = await message.reply_text("**🔍Looking for gurl...**")
    try:
        asupannya = []
        async for asupan in userbot.one.search_messages("suchdiary", filter="photo"):
            asupannya.append(asupan)

        file=random.choice(asupannya)
        oh = await userbot.one.download_media(file)
        await app.send_photo(
            message.chat.id,
            oh,
            caption=f"**It's a joke, Sis {message.from_user.mention} 🥵**",
            )
        await y.delete()
    except Exception:
        await y.edit("**Failed to find sexygurl, more badmood...**")
    os.remove(oh)


@app.on_message(filters.command("xgurl"))
async def asupan(client, message):
    y = await message.reply_text("**🔍 Looking for xgurl...**")
    try:
        asupannya = []
        async for asupan in userbot.one.search_messages("kiddrugs", filter="photo"):
            asupannya.append(asupan)

        file=random.choice(asupannya)
        oh = await userbot.one.download_media(file)
        await app.send_photo(
            message.chat.id,
            oh,
            caption=f"**It's a joke, sister {message.from_user.mention} 🤗**",
            )
        await y.delete()
    except Exception:
        await y.edit("**Failed to find a xgurl, again bad mood...**")
    os.remove(oh)


@app.on_message(filters.command("xxgurl"))
async def asupan(client, message):
    y = await message.reply_text("**🔍 Looking for xxgurl Images...**")
    try:
        asupannya = []
        async for asupan in userbot.one.search_messages("ppcpanime", filter="photo"):
            asupannya.append(asupan)

        file=random.choice(asupannya)
        oh = await userbot.one.download_media(file)
        await app.send_photo(
            message.chat.id,
            oh,
            caption=f"**In {message.from_user.mention} the weaday picture, the xxgurl base😆**",
            )
        await y.delete()
    except Exception:
        await y.edit("**Failed to find pictures of xxgurl, again bad mood..**")
    os.remove(oh)
