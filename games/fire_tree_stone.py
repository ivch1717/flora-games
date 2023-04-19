from func.keybord import change, get
from random import randint
from func.work_db import choice_db, get_db

stavka = 0


async def fts(update, context):
    change(['10', '50', '100', '200', '500'])
    await update.message.reply_text("сколько ставите?", reply_markup=get())


async def stake_fts(update, context):
    global stavka
    if int(update.message.text) <= 0:
        await update.message.reply_text("введите корректное значение")
        return "2games_1"
    if int(update.message.text) > get_db(update.effective_user.id):
        await update.message.reply_text("у вас не такого количества денег")
        return "2games_1"
    change(["огонь", "дерево", "камень"])
    await update.message.reply_text(
        "Огонь сжигает дерево. Дерево разрушает камень. А камень тушит огонь. Вы и вашt абонент выбирают стихию, "
        "в случае победы вы получаете 1.75 от прибыли, в случае ничьи ваши деньги сохраняются. ", reply_markup=get())
    await update.message.reply_text("на что ставите?", reply_markup=get())
    stavka = int(update.message.text)
    return "2games_2"


async def result_fts(update, context):
    global stavka
    if update.message.text.lower() not in ["огонь", "дерево", "камень"]:
        await update.message.reply_text("такого варианта не было, повторите ещё раз")
        return "2games_2"
    bot_ans = randint(0, 2)
    change(['игра угадай цветок', 'открыть набор семян', 'игра огонь дерево вода', 'игра набери 23 шишки'])
    if bot_ans == 0:
        await update.message.reply_text("противник выбрал огонь")
    elif bot_ans == 1:
        await update.message.reply_text("противник выбрал дерево")
    else:
        await update.message.reply_text("противник выбрал камень")
    if (bot_ans == 0 and update.message.text == "огонь") or (bot_ans == 1 and update.message.text == "дерево") or (
            bot_ans == 2 and update.message.text == "камень"):
        await update.message.reply_text("у вас ничья", reply_markup=get())
    elif (bot_ans == 1 and update.message.text == "огонь") or (bot_ans == 2 and update.message.text == "дерево") or (
            bot_ans == 0 and update.message.text == "камень"):
        choice_db(update.effective_user.id, int(stavka * 0.75))
        await update.message.reply_text("поздравляем, ты победил!!", reply_markup=get())
    else:
        choice_db(update.effective_user.id, -stavka)
        await update.message.reply_text("ты проиграл", reply_markup=get())
    return "play"
