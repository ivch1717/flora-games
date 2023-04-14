from telegram.ext import ConversationHandler
from func.delete_job import delete

async def stop(update, context):
    await update.message.reply_text("Всего хорошего")
    chat_id = update.effective_message.chat_id
    delete(str(chat_id), context)
    return ConversationHandler.END
