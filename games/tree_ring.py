from func.keybord import change, get
from random import randint
from func.work_db import choice_db, get_db

stavka = 0
massiv_selection = []
step = 2
ans = []


async def tre_ring(update, context):
    change(['10', '50', '100', '200', '500'])
    await update.message.reply_text("Какой билетик вы покупаете?", reply_markup=get())


async def stake_tree_ring(update, context):
    global stavka, ans
    if not update.message.text.isdigit():
        await update.message.reply_text("введите корректное значение")
        return "4games_1"
    if int(update.message.text) <= 0:
        await update.message.reply_text("введите корректное значение")
        return "4games_1"
    if int(update.message.text) > get_db(update.effective_user.id):
        await update.message.reply_text("у вас не такого количества тугриков")
        return "4games_1"
    change(['38', '42', '17', '28', '7', '55'])
    await update.message.reply_text(
        f"вы должны угадать в какой год под деревом росли грибы, известно, что у дерева 64 годовых кольца, а так же,"
        f"что под деревом грибы росли в 6 годах, чем больше вы угадаете, тем больше тугриков вы получите",
        reply_markup=get())

    stavka = int(update.message.text)
    choice_db(update.effective_user.id, -stavka)
    while len(ans) < 6:
        x = randint(1, 64)
        if x not in ans:
            ans.append(x)

    await update.message.reply_text(f"выберите вашу 1 догадку, напишите число от 1 до 64, "
                                    f"какой год по вашему был грибной")
    return "4games_2"


async def pick_ring(update, context):
    global step, massiv_selection
    if not update.message.text.isdigit():
        await update.message.reply_text("введите корректное значение")
        return "4games_2"
    if int(update.message.text) in massiv_selection:
        await update.message.reply_text("вы уже выбирали такой год, напишите другой")
    elif 1 <= int(update.message.text) <= 64:
        massiv_selection.append(int(update.message.text))
        if step >= 7:
            await result_tree_ring(update, context)
            return "play"
        await update.message.reply_text(f"выберите вашу {step} догадку, напишите число от 1 до 64, "
                                        f"какой год по вашему был грибной")
        step += 1
    else:
        await update.message.reply_text("введите корректное значение")
    return "4games_2"


async def result_tree_ring(update, context):
    global ans, massiv_selection
    await update.message.reply_text(f"года, в которые грибы росли под деревом: {ans[0]}, {ans[1]}, {ans[2]}, {ans[3]}, "
                                    f"{ans[4]}, {ans[5]}")
    win = 0
    for i in massiv_selection:
        if i in ans:
            win += 1
    change(['игра угадай цветок', 'открыть набор семян', 'игра огонь дерево вода', 'игра набери 23 шишки',
            'игра годовые кольца', 'посадка дерева'])
    await update.message.reply_text(f"ты угадал {win} раз, ты выиграл {int(stavka * win)} тугриков")
    choice_db(update.effective_user.id, int(stavka * win / 2))
