from func.keybord import change, get
from random import randint
from func.work_db import choice_db, get_db

cnt_set = 0
legendary_plants = [["lega1.png", 1000], ["lega2.png", 950], ["lega3.png", 900], ["lega4.png", 800]]
flowers = [["f1.jpg", 350], ["f2.png", 300], ["f3.jpg", 250], ["f4.png", 400], ["f5.png", 350], ["f6.png", 500],
           ["f7.png", 300], ["f8.png", 450], ["f9.png", 400], ]


def add_set():
    global cnt_set
    cnt_set += 1


async def result_cones(update, context):
    global cnt_set
    if cnt_set > 0:
        await update.message.reply_text(f'мы открыли бесплатный набор семян который у вас был,'
                                        f'наборов семян осталось: {cnt_set}')
    else:
        if get_db(update.effective_user.id) < 100:
            await update.message.reply_text('один набор семян стоит 100 тугриков, у вас нет таких денег')
        else:
            choice_db(update.effective_user.id, -100)
            if randint(1, 2) == 1:
                i = randint(0, 3)
                await context.bot.send_photo(chat_id=update.effective_user.id,
                                             photo=open(f"resourse/seed/legendary_plants/{legendary_plants[i][0]}",
                                                        'rb'))
                choice_db(update.effective_user.id, legendary_plants[i][1])
            else:
                i = randint(0, 8)
                await context.bot.send_photo(chat_id=update.effective_user.id,
                                             photo=open(f"resourse/seed/flowers/{flowers[i][0]}", 'rb'))
                choice_db(update.effective_user.id, flowers[i][1])
