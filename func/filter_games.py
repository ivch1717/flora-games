from games.guess_the_flower import guess_the_flower
from games.fire_tree_stone import fts


async def filter(update, context):
    if update.message.text == 'игра угадай цветок':
        await guess_the_flower(update, context)
        return "1games_1"
    if update.message.text == 'игра огонь дерево вода':
        await fts(update, context)
        return "2games_1"
