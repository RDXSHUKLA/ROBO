

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from JARVISROBO import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT, BOT_NAME

# <============================================== CONSTANTS =========================================================>
STATS_IMG = [
    "https://graph.org/file/257fe1ec8828b836c70f7.jpg",
]
START_IMG = [
    "https://graph.org/file/8dcccaaa09c3ec38d9c75.jpg",
    "https://graph.org/file/74d2385efc329c13c11e9.jpg",
    "https://graph.org/file/d818146f35f6a439a7a7f.jpg",
    "https://graph.org/file/d1d68eaaa8aecc68f8387.jpg",
    "https://graph.org/file/257fe1ec8828b836c70f7.jpg",
    "https://graph.org/file/8b044edab3d3173544439.jpg",
    "https://graph.org/file/8ed87bfd7c0b3dbdd1bf5.jpg",
    "https://graph.org/file/1a33887db1a3b5dee1b0a.jpg",
    "https://graph.org/file/04ea07e42660988229834.jpg",
    "https://graph.org/file/abb6b4bb00e2751bc9f54.jpg",
]

HEY_IMG = "https://graph.org/file/8ed87bfd7c0b3dbdd1bf5.jpg"

ALIVE_ANIMATION = [
     "https://te.legra.ph/file/eace7a5d8d4b515a11e50.jpg",
     "https://telegra.ph/file/f09aa12ffdf215b2aa6f0.jpg",
]

FIRST_PART_TEXT = "*ʜᴇʏ* `{}` , 💫 . . ."

PM_START_TEXT = """
*❖ ᴛʜɪs ɪs* ˹sᴛʀᴀɴɢᴇʀ ʀᴏʙᴏ˼ !
✦ ᴛʜᴇ ᴍᴏsᴛ ᴩᴏᴡᴇʀғᴜʟ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴩ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ᴀɴᴅ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs 🌹

──────────────────
*❖ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs.*
"""

START_BTN = [
   [
        InlineKeyboardButton(
            text="▪️ ᴀᴅᴅ ᴍᴇ ▪️",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
   [
        InlineKeyboardButton(text="▫️ʜᴇʟᴩ & ᴄᴏᴍᴍᴀɴᴅs▫️", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton(text="🔸 ᴀʙᴏᴜᴛ 🔸", callback_data="Jarvis_"),
        InlineKeyboardButton(text="🕯️ sᴜᴩᴩᴏʀᴛ 🕯️", url=f"https://t.me/MASTIWITHFRIENDSXD"),
    ],
   [
        InlineKeyboardButton(text="💻 ᴅᴇᴠᴇʟᴏᴩᴇʀ 💻", url=f"tg://user?id={OWNER_ID}"),
        InlineKeyboardButton(text="📺 sᴏᴜʀᴄᴇ 📺", callback_data="git_source"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="✧ ᴀᴅᴅ ᴍᴇ ✧",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="🕯️ sᴜᴩᴩᴏʀᴛ 🕯️", url=f"https://t.me/MASTIWITHFRIENDSXD"),
        InlineKeyboardButton(text="💻 ᴅᴇᴠᴇʟᴏᴩᴇʀ 💻", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="▪️ᴜᴘᴅᴀᴛᴇs▪️", url="https://t.me/SHIVANSH474"),
        ib(text="🔸sᴜᴩᴩᴏʀᴛ ᴄʜᴀᴛ🔸", url="https://t.me/MASTIWITHFRIENDSXD"),
    ],
    [
        ib(
            text="🔺 ᴀᴅᴅ ᴍᴇ 🔺",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = f"""
*❖ » sᴛʀᴀɴɢᴇʀ ʀᴏʙᴏ ᴇxᴄʟᴜsɪᴠᴇ ꜰᴇᴀᴛᴜʀᴇs*

ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ ꜱᴇᴄᴛɪᴏɴ.
 ✦ ɪɴ ᴘᴍ : ᴡɪʟʟ ꜱᴇɴᴅ ʏᴏᴜ ʜᴇʟᴘ ꜰᴏʀ ᴀʟʟ ꜱᴜᴘᴘᴏʀᴛᴇᴅ ᴍᴏᴅᴜʟᴇꜱ.
 ✦ ɪɴ ɢʀᴏᴜᴘ : ᴡɪʟʟ ʀᴇᴅɪʀᴇᴄᴛ ʏᴏᴜ ᴛᴏ ᴘᴍ, ᴡɪᴛʜ ᴀʟʟ ᴛʜᴀᴛ ʜᴇʟᴘ ᴍᴏᴅᴜʟᴇꜱ.
 """