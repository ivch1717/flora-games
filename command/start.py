from func.keybord import change, get
from func.work_db import add_db
from func.present_everyday import add_present
from func.present_everyweek import add_present2


async def start(update, context):
    change(['/stop', '/help', '/menu', '/play', '/balance'])
    user = update.effective_user
    add_db(user.id)
    context.job_queue.run_once(add_present, 86400, chat_id=update.effective_message.chat_id,
                               name=str(update.effective_message.chat_id))
    context.job_queue.run_once(add_present2, 86400 * 7, chat_id=update.effective_message.chat_id,
                               name=str(update.effective_message.chat_id))
    await update.message.reply_html(
        rf"Привет {user.mention_html()}!",
        reply_markup=get()
    )
    return "beginning"
