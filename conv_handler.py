from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, filters
from command.start import start
from command.stop import stop
from command.play import play
from func.filter_games import filter
from games.guess_the_flower import choice, result
from games.fire_tree_stone import result_fts, stake_fts
from command.menu import menu

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        "beginning": [CommandHandler('play', play)],
        "play": [MessageHandler(filters.TEXT & ~filters.COMMAND, filter), CommandHandler("menu", menu)],
        "1games_1": [MessageHandler(filters.TEXT & ~filters.COMMAND, choice), CommandHandler("menu", menu)],
        "1games_2": [MessageHandler(filters.TEXT & ~filters.COMMAND, result), CommandHandler("menu", menu)],
        "2games_1": [MessageHandler(filters.TEXT & ~filters.COMMAND, stake_fts), CommandHandler("menu", menu)],
        "2games_2": [MessageHandler(filters.TEXT & ~filters.COMMAND, result_fts), CommandHandler("menu", menu)],
    },
    fallbacks=[CommandHandler('stop', stop)]
)