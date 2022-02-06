from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
	Lasiya2 = InlineKeyboardMarkup([
		[InlineKeyboardButton("Url Uploader Bot", url="https://t.me/SenithUrlUploaderBot")],
		 ])
	help_image = "https://telegra.ph/file/0562e30782d01a6e51f4c.jpg"
	await message.reply_photo(help_image,  caption="**♔English help♔**\n• Just Send your Youtube video url⛓ \n• And i will give Method list to select your choice😋\n\n**♔සිංහල උදව්**\n• කොපි කරගත් Youtube ලින්කුව එවන්න.\n• By : Senith Chandul",reply_markup=Lasiya2)
