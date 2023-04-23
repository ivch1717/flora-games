from func.keybord import change, get


async def play(update, context):
    change(['игра угадай цветок', 'открыть набор семян', 'игра огонь дерево вода', 'игра набери 23 шишки',
            'игра годовые кольца', 'посадка дерева'])
    await update.message.reply_text("Добро пожаловать в прекрасный зелёный мир, выберите игру, и "
                                    "заработайте как можно больше тугриков, желаем удачи!",
                                    reply_markup=get())
    return "play"
