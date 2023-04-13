from telegram.ext import ConversationHandler


async def stop(update, context):
    await update.message.reply_text("Всего хорошего")
    return ConversationHandler.END
