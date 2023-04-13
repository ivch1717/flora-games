from telegram import ReplyKeyboardMarkup

reply_keyboard = [['/start']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


def change(comand_list):
    global reply_keyboard, markup
    reply_keyboard = [comand_list]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


def get():
    return markup
