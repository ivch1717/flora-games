from func.keybord import change, get

async def play(update, context):
    change(['игра угадай цветок', 'открыть набор семян'])
    await update.message.reply_text("Добро пожаловать в прекрасный зелёный мир, выберете игру, и "
                                    "заработайте как можно больше тугриков, желаем удачи!",
                                    reply_markup=get())
    return "play"
