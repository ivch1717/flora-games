import logging
from telegram.ext import Application, CommandHandler
from resourse.bot_token import BOT_TOKEN
from conv_handler import conv_handler
from command.help import help


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(conv_handler)
    application.add_handler(CommandHandler("help", help))
    application.run_polling()


if __name__ == '__main__':
    main()
