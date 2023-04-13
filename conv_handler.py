from telegram.ext import CommandHandler, ConversationHandler
from command.start import start
from command.stop import stop

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
    },
    fallbacks=[CommandHandler('stop', stop)]
)