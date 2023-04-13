from games.guess_the_flower import guess_the_flower


async def filter(update, context):
    if update.message.text == 'игра угадай цветок':
        await guess_the_flower(update, context)
        return "1games_1"
