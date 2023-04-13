from telegram import ReplyKeyboardMarkup

reply_keyboard = [['/start', '/stop', '/help', '/info']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)