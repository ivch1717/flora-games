import logging
from telegram.ext import Application
from resourse.bot_token import BOT_TOKEN
from conv_handler import conv_handler


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
