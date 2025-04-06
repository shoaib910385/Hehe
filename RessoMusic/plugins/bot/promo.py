from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from RessoMusic import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message, User
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden, PeerIdInvalid, ChatAdminRequired
from pyrogram.enums import ChatAction, ChatType, MessageEntityType
from pyrogram import Client, filters, enums
from RessoMusic.misc import SUDOERS

buttons = [
    [
        InlineKeyboardButton(
            text="➕ ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ", 
            url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users"
        ),
    ],
]

@app.on_message(filters.command(["promo"]) & SUDOERS)
async def promos(client, message: Message):
    AMBOT = f"""{app.mention},
🤖 ᴀᴅᴠᴀɴᴄᴇᴅ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ ᴠɪᴅᴇᴏᴄʜᴀᴛs 🤖
⚡️ғᴇᴀᴛᴜʀᴇs ⚡️
➻ ɪ ᴄᴀɴ ᴘʟᴀʏ ꜱᴏɴɢ ɪɴ ɢʀᴏᴜᴘ ᴠᴄ.
➻ ɴᴏ ʟᴀɢ.
➻ ʙᴇꜱᴛ ꜱᴏᴜɴᴅ Qᴜᴀʟɪᴛʏ.
➻ 24×7 ᴜᴘᴛɪᴍᴇ.
➻ ʟᴀɢ ғʀᴇᴇ.
"""
    await message.reply(
        text=AMBOT,
        reply_markup=InlineKeyboardMarkup(buttons)
    )
    await RessoMusic.send_photo(
                chat_id,
                photo="https://telegra.ph//file/14ec9c3ff42b59867040a.jpg",
                caption=f"**{shayari}**",
                reply_markup=add_buttons,
    )
