from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(Filters.command(["bot"]))
async def start(client, message):
    await message.reply_text("Url Uploader Bot",
                             reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("⚜️ Go ⚜️", url="https://t.me/SenithUrlUploaderBot")]
        ]))
    
