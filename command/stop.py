from telegram.ext import ConversationHandler
from func.delete_job import delete
from func.work_db import delete_db


async def stop(update, context):
    await update.message.reply_text("Всего хорошего")
    chat_id = update.effective_message.chat_id
    user = update.effective_user
    delete(str(chat_id), context)
    delete_db(user.id)
    return ConversationHandler.END
