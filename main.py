from pyrogram import Client, filters 


API_ID = "6362436"
API_HASH = "c0e8c637c6ea7c97fce7f4d9622aa023"
BOT_TOKEN = "5542287006:AAHx2XSh1bQWRGevqoc2TmcZ7jBFkyI_d6o"

OXYVER = Client(
    name = "Pyrogrambot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


@OXYVER.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text("** If You Want To Know More Contact My Owner @Oxyver_Owner**")
