async def help(update, context):
    await update.message.reply_text("Чтобы начать играть нажмите /play, "
                                    "чтобы закончить разговор нажмите    /stop, "
                                    "чтобы узнать свой баланс нажмите /balance")
