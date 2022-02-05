from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel 😇", url="https://t.me/+IU1ta7Gg19VkYzE1")],
        [InlineKeyboardButton(
            "Report Bugs 🙈", url="https://t.me/tujan3")],
         [InlineKeyboardButton("Our Group 😇", url="https://t.me/trtechguide")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
