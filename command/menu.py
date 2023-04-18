from func.keybord import change, get


async def menu(update, context):
    change(['/stop', '/help', '/menu', '/play', '/balance'])
    await update.message.reply_text("вернул назад", reply_markup=get())
    return "beginning"
