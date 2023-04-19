from func.keybord import change, get
from random import randint
from func.work_db import choice_db, get_db

flowers = 0
stavka = 0


async def guess_the_flower(update, context):
    change(['10', '50', '100', '200', '500'])
    await update.message.reply_text("сколько ставите?", reply_markup=get())


async def choice(update, context):
    global stavka
    if int(update.message.text) <= 0:
        await update.message.reply_text("введите корректное значение")
        return "2games_1"
    if int(update.message.text) > get_db(update.effective_user.id):
        await update.message.reply_text("у вас не такого количества денег")
        return "2games_1"
    change(["роза", "гвоздика"])
    await update.message.reply_text(
        "выберите на какой цветок вы делаете ставку: на розу или гвоздику, в случае если выпала трава, "
        "вы проиграли, если вы угадали, то ваша ставка удвоится",
        reply_markup=get())
    stavka = int(update.message.text)
    return "1games_2"


async def result(update, context):
    global flowers
    if update.message.text.lower() == 'роза':
        flowers = 0
    elif update.message.text.lower() == 'гвоздика':
        flowers = 1
    else:
        await update.message.reply_text("такого варианта не было, повторите ещё раз")
        return "1games_2"
    text = ""
    rnd = randint(0, 2)
    if rnd == 0:
        text += "выпала роза\n"
    elif rnd == 1:
        text += "выпала гвоздика\n"
    else:
        text += "выпала трава\n"
    if flowers == rnd:
        text += "Поздравляем, ты выиграл!"
        choice_db(update.effective_user.id, stavka)
    else:
        text += "Ты проиграл"
        choice_db(update.effective_user.id, -stavka)
    change(['игра угадай цветок', 'открыть набор семян', 'игра огонь дерево вода', 'игра набери 23 шишки'])
    await update.message.reply_text(text, reply_markup=get())
    return "play"
