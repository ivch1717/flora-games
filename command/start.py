from func.keybord import markup


async def start(update, context):
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет {user.mention_html()}!",
        reply_markup=markup
    )
    return 0
