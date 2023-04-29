import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.delete()
    await message.reply_photo(
        photo=f"https://graph.org/file/1e151cf9b0afd0aff05a4.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 𝙃𝙚𝙡𝙡𝙤, 𝙄 𝘼𝙢 𝙎𝙪𝙥𝙚𝙧 𝙁𝙖𝙨𝙩 𝙈𝙪𝙨𝙞𝙘 𝙋𝙡𝙖𝙮𝙚𝙧
𝘽𝙤𝙩 𝙁𝙤𝙧 𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝙂𝙧𝙤𝙪𝙥𝙨 ...
┏━━━━━━━━━━━━━━━━━┓
┣★ 𝘾𝙧𝙚𝙖𝙩𝙤𝙧 : [𓆩 𝐂𝐎𝐃𝐄𝐑 𓆪](https://t.me/its_Coder_xD)
┣★ 𝙎𝙪𝙥𝙥𝙤𝙧𝙩 : [𝗔𝗥𝗖𝗛](https://t.me/ARCH_SUPPORTS)
┣★ 𝘾𝙝𝙖𝙣𝙣𝙚𝙡 : [𝗔𝗥𝗖𝗛 𝗧𝗘𝗔𝗠](https://t.me/ArchBots)
┗━━━━━━━━━━━━━━━━━┛
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•✯⭐ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ⭐✯•", url=f"https://t.me/KNAYA_MUSIC_BOT?startgroup=true"
                      )
                ]
            ]
    )