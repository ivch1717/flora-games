from func.keybord import change, get


async def start(update, context):
    change(['/stop', '/help', '/info', '/play'])
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет {user.mention_html()}!",
        reply_markup=get()
    )
    return "beginning"
