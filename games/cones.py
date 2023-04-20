from func.keybord import change, get
from random import randint
from func.work_db import choice_db, get_db

stavka = 0
cnt = 0


async def cones(update, context):
    change(['10', '50', '100', '200', '500'])
    await update.message.reply_text("сколько ставите?", reply_markup=get())


async def stake_cones(update, context):
    global stavka, cnt
    if not update.message.text.isdigit():
        await update.message.reply_text("введите корректное значение")
        return "3games_1"
    if int(update.message.text) <= 0:
        await update.message.reply_text("введите корректное значение")
        return "3games_1"
    if int(update.message.text) > get_db(update.effective_user.id):
        await update.message.reply_text("у вас не такого количества тугриков")
        return "3games_1"
    cnt = randint(2, 20)
    change(["играть ещё", "закончить игру"])
    await update.message.reply_text(
        f"Вы должны собрать 23 шишки с дерева, сейчас у вас есть {cnt} шишек, вы можете либо потрясти дерево,и тогда "
        f"с него упадёт от 1 до 10 шишек, либо закончить игру. Чем больше шишек у вас будет, тем больше тугриков вы "
        f"получите. Так же вам может выпасть красная шишка, тогда вы сами выбираете сколько она даст шишек: от 1 до 10",
        reply_markup=get())
    stavka = int(update.message.text)
    choice_db(update.effective_user.id, -stavka)
    return "3games_2"


async def take_cones(update, context):
    global cnt, x
    x = randint(1, 11)
    if x == 11:
        change(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        await update.message.reply_text(f'вам выпала красная шишка, выберите любое значение от 1 до 10',
                                        reply_markup=get())
        return
    cnt += x
    await update.message.reply_text(f"вам выпало {x} шишек, у вас сейчас {cnt} шишек")


async def red_cones(update, context):
    global cnt
    if not update.message.text.isdigit():
        await update.message.reply_text("такого варианта не было, повторите ещё раз")
        return "3games_3"
    if 1 <= int(update.message.text) <= 10:
        cnt += int(update.message.text)
        change(["играть ещё", "закончить игру"])
        await update.message.reply_text(f"вам выпало {update.message.text} шишек, у вас сейчас {cnt} шишек",
                                        reply_markup=get())
        if cnt > 23:
            change(['игра угадай цветок', 'открыть набор семян', 'игра огонь дерево вода', 'игра набери 23 шишки',
                    'игра годовые кольца'])
            await update.message.reply_text("ты проиграл", reply_markup=get())
            return "play"

        return "3games_2"
    else:
        await update.message.reply_text("введите корректное значение")
        return "3games_3"


async def result_cones(update, context):
    global cnt, stavka
    change(['игра угадай цветок', 'открыть набор семян', 'игра огонь дерево вода', 'игра набери 23 шишки',
            'игра годовые кольца'])
    await update.message.reply_text(f"ты получил {max(0, int(stavka * ((cnt - 17) / 2)))} тугриков", reply_markup=get())
    choice_db(update.effective_user.id, max(0, int(stavka * ((cnt - 17) / 2))))


async def filter_cones(update, context):
    global cnt, x
    if update.message.text.lower() == "играть ещё":
        await take_cones(update, context)
        if x == 11:
            return "3games_3"
        if cnt > 23:
            change(['игра угадай цветок', 'открыть набор семян', 'игра огонь дерево вода', 'игра набери 23 шишки',
                    'игра годовые кольца'])
            await update.message.reply_text("ты проиграл", reply_markup=get())
            return "play"
        return "3games_2"
    elif update.message.text.lower() == "закончить игру":
        await result_cones(update, context)
        return "play"
    else:
        await update.message.reply_text("такого варианта не было, повторите ещё раз")
        return "3games_2"
