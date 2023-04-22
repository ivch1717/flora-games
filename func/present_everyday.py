from func.work_db import choice_db


async def add_present(context):
    choice_db(context.job.chat_id, 100)
    await context.bot.send_message(context.job.chat_id, text=f'Вы получили подарок 100 тугриков!')
    context.job_queue.run_once(add_present, 86400, chat_id=context.job.chat_id,
                               name=str(context.job.chat_id))
