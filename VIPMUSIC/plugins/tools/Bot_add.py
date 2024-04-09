import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message
from config import LOGGER_ID as LOG_GROUP_ID
from VIPMUSIC import app  
from VIPMUSIC.core.userbot import Userbot
from VIPMUSIC.utils.database import delete_served_chat
from VIPMUSIC.utils.database import get_assistant


photo = [
     "https://telegra.ph/file/e444b74940e480dd62a11.jpg",
    "https://telegra.ph/file/06e5de22a8a02d0be0010.jpg",
    "https://telegra.ph/file/843359e2b1553b792df2d.jpg",
    "https://telegra.ph/file/d62b1af207276d22f1211.jpg",
    "https://telegra.ph/file/1e0e6a85cea882a6980ce.jpg",
    
]

@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    try:
        userbot = await get_assistant(message.chat.id)
        chat = message.chat
        for members in message.new_chat_members:
            if members.id == app.id:
                count = await app.get_chat_members_count(chat.id)
                username = message.chat.username if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐆ʀᴏᴜᴘ"
                msg = (
                    f"**📝ᴍᴜꜱɪᴄ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ #𝐍ᴇᴡ_𝐆ʀᴏᴜᴘ**\n\n"
                    f"**📌ᴄʜᴀᴛ ɴᴀᴍᴇ:** {message.chat.title}\n"
                    f"**🍂ᴄʜᴀᴛ ɪᴅ:** {message.chat.id}\n"
                    f"**🔐ᴄʜᴀᴛ ᴜꜱᴇʀɴᴀᴍᴇ:** @{username}\n"
                    f"**📈ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀꜱ:** {count}\n"
                    f"**🤔ᴀᴅᴅᴇᴅ ʙʏ:** {message.from_user.mention}"
                )
                await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(f"😍ᴀᴅᴅᴇᴅ ʙʏ😍", url=f"tg://openmessage?user_id={message.from_user.id}")]
             ]))
                await userbot.join_chat(f"{username}")
    except Exception as e:
        print(f"Error: {e}")
