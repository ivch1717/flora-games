from games.guess_the_flower import guess_the_flower
from games.fire_tree_stone import fts
from games.cones import cones
from games.tree_ring import tre_ring
from games.seed_set import result_cones


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
    if update.message.text.lower() == 'игра годовые кольца':
        await tre_ring(update, context)
        return "4games_1"
    if update.message.text.lower() == 'открыть набор семян':
        await result_cones(update, context)
        return "play"
