from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, filters
from command.start import start
from command.stop import stop
from command.play import play
from func.filter_games import filter
from games.guess_the_flower import choice, result

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        "beginning": [CommandHandler('play', play)],
        "play": [MessageHandler(filters.TEXT & ~filters.COMMAND, filter)],
        "1games_1": [MessageHandler(filters.TEXT & ~filters.COMMAND, choice)],
        "1games_2": [MessageHandler(filters.TEXT & ~filters.COMMAND, result)],
    },
    fallbacks=[CommandHandler('stop', stop)]
)