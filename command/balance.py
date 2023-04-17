from func.work_db import get_db


async def balance(update, context):
    await update.message.reply_text(get_db(update.effective_user.id))
