from games.seed_set import add_set


async def add_present2(context):
    add_set()
    await context.bot.send_message(context.job.chat_id, text=f'Вы получили подарок 1 бесплатный набор семян!')
    context.job_queue.run_once(add_present2, 86400 * 7, chat_id=context.job.chat_id,
                               name=str(context.job.chat_id))
