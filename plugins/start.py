from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    Lasiya = InlineKeyboardMarkup([
        
        [InlineKeyboardButton("Url Uploader Bot", url="https://t.me/SenithUrlUploaderBot")],
        [InlineKeyboardButton(
            "Torrent Mirror Bot", url="https://t.me/SenithMirrorBot")],
        [InlineKeyboardButton(
            "Button Post Maker",url="https://t.me/BtnPostmakerBot")]
    ])
    thumbnail_url = "https://telegra.ph/file/0562e30782d01a6e51f4c.jpg"
    await message.reply_photo(thumbnail_url, caption=f"Hi <b>{message.from_user.first_name}</b>\n\n<b>Instructions for use..</b>\n• Type /help to get instructins.\n───── ❝ **Lets Play** ❞ ─────\n ", reply_markup=Lasiya)
    raise StopPropagation
