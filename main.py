from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from pyrogram.errors import UserNotParticipant 

API_ID = "6362436"
API_HASH = "c0e8c637c6ea7c97fce7f4d9622aa023"
BOT_TOKEN = "5542287006:AAHx2XSh1bQWRGevqoc2TmcZ7jBFkyI_d6o"

OXYVER = Client(
    name = "Pyrogrambot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

force_channel = "Oxyver"


@OXYVER.on_message(filters.command("start"))
async def start_cmd(bot, msg):
    if force_channel:
        try:
            user = await bot.get_chat_member(force_channel, msg.from_user.id)
            if user.status == "kicked out":
                await msg.reply_text("You Are Banned")
                return
        except UserNotParticipant:
            await msg.reply_text(
                text="You Are Not A Member Of My Channel",
                reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("Join Channel 📣", url=f"t.me/{force_channel}")
                 ]]
                )
            )


    await msg.reply_text("** If You Want To Know More Contact My Owner @Oxyver_Owner**")


print("Bot Started")

OXYVER.run()
