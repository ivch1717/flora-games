from func.keybord import change, get
from func.work_db import add_db


async def start(update, context):
    change(['/stop', '/help', '/menu', '/play', '/balance'])
    user = update.effective_user
    add_db(user.id)
    await update.message.reply_html(
        rf"Привет {user.mention_html()}!",
        reply_markup=get()
    )
    return "beginning"
