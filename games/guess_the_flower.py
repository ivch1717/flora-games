from func.keybord import change, get
from random import randint
flowers = 0


async def guess_the_flower(update, context):
    change(["роза", "гвоздика"])
    await update.message.reply_text("выберите на какой цветок вы делаете ставку: на розу или гвоздику",
                                    reply_markup=get())


async def choice(update, context):
    global flowers
    if update.message.text == 'роза':
        flowers = 0
    else:
        flowers = 1
    await update.message.reply_text("сколько ставите?")
    return "1games_2"


async def result(update, context):
    text = ""
    rnd = randint(0, 3)
    if rnd == 0:
        text += "выпала роза\n"
    elif rnd == 1:
        text += "выпала гвоздика\n"
    else:
        text += "выпала трава\n"
    if flowers == rnd:
        text += "Поздравляем, ты выиграл!"
    else:
        text += "Ты проиграл"
    change(['10', '50', '100', '200', '500'])
    await update.message.reply_text(text)
    return "1games_1"


