from func.keybord import change, get
from command.help import help


async def start(update, context):
    change(['/stop', '/help', '/info', '/play'])
    user = update.effective_user
    chat_id = update.effective_message.chat_id
    context.job_queue.run_once(help, 5, chat_id=chat_id, name=str(chat_id))
    await update.message.reply_html(
        rf"Привет {user.mention_html()}!",
        reply_markup=get()
    )
    return "beginning"
