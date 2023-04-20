from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, filters
from command.start import start
from command.stop import stop
from command.play import play
from command.menu import menu
from func.filter_games import filter
from games.guess_the_flower import choice, result
from games.fire_tree_stone import result_fts, stake_fts
from games.cones import filter_cones, stake_cones, red_cones
from games.tree_ring import stake_tree_ring, pick_ring


conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        "beginning": [CommandHandler('play', play)],
        "play": [MessageHandler(filters.TEXT & ~filters.COMMAND, filter), CommandHandler("menu", menu)],
        "1games_1": [MessageHandler(filters.TEXT & ~filters.COMMAND, choice), CommandHandler("menu", menu)],
        "1games_2": [MessageHandler(filters.TEXT & ~filters.COMMAND, result)],
        "2games_1": [MessageHandler(filters.TEXT & ~filters.COMMAND, stake_fts), CommandHandler("menu", menu)],
        "2games_2": [MessageHandler(filters.TEXT & ~filters.COMMAND, result_fts)],
        "3games_1": [MessageHandler(filters.TEXT & ~filters.COMMAND, stake_cones), CommandHandler("menu", menu)],
        "3games_2": [MessageHandler(filters.TEXT & ~filters.COMMAND, filter_cones)],
        "3games_3": [MessageHandler(filters.TEXT & ~filters.COMMAND, red_cones)],
        "4games_1": [MessageHandler(filters.TEXT & ~filters.COMMAND, stake_tree_ring), CommandHandler("menu", menu)],
        "4games_2": [MessageHandler(filters.TEXT & ~filters.COMMAND, pick_ring)],
    },
    fallbacks=[CommandHandler('stop', stop)]
)