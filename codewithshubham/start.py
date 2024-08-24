from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""ʜᴇʏ {msg.from_user.mention},

ɪ ᴀᴍ {me2},
ᴛʀᴜꜱᴛᴇᴅ ꜱᴛʀɪɴɢ ɢᴇɴʀᴀᴛᴏʀ ʙᴏᴛ.
ꜰᴜʟʟʏ ꜱᴀꜰᴇ ᴀɴᴅ ꜱᴇᴄᴜʀᴇ.
ɴᴏ ᴇʀʀᴏʀ.

ᴍᴀᴅᴇ ʙʏ  : [ᴛᴇᴀᴍ ᴄʀᴇᴀᴛᴏʀ](t.me/the_creator_botz) !""",
        reply_markup=InlineKeyboardMarkup(
            [
              [
                    InlineKeyboardButton("ᴀᴅᴍɪɴ", url="https://t.me/shubham_X_Official")
              ],[
                    InlineKeyboardButton("ɢᴇɴʀᴀᴛᴇ ꜱᴛʀɪɴɢ", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url="https://t.me/unreal_X_support"),
                    InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url="https://t.me/unreal_X_bot")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
