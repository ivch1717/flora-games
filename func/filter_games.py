from games.guess_the_flower import guess_the_flower
from games.fire_tree_stone import fts
from games.cones import cones


async def filter(update, context):
    if update.message.text.lower() == 'игра угадай цветок':
        await guess_the_flower(update, context)
        return "1games_1"
    if update.message.text.lower() == 'игра огонь дерево вода':
        await fts(update, context)
        return "2games_1"
    if update.message.text.lower() == 'игра набери 23 шишки':
        await cones(update, context)
        return "3games_1"
