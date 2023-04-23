from random import randint
from func.work_db import choice_db, get_db

cnt_set = 0
legendary_plants = [["lega1.png", 1000], ["lega2.png", 950], ["lega3.png", 900], ["lega4.png", 800]]
flowers = [["f1.jpg", 350], ["f2.png", 300], ["f3.jpg", 250], ["f4.png", 400], ["f5.png", 350], ["f6.png", 500],
           ["f7.png", 300], ["f8.png", 450], ["f9.png", 400]]
tre = [["t1.jpg", 80], ["t2.png", 75], ["t3.png", 85], ["t4.png", 105], ["t5.png", 90], ["t6.png", 95],
       ["t7.png", 200], ["t8.png", 100], ["t9.png", 90], ["t10.png", 140], ["t11.png", 120]]
grass = [["g1.png", 20], ["g2.png", 10], ["g3.png", 25], ["g4.png", 5], ["g5.png", 2], ["g6.png", 8],
         ["g7.png", 15], ["g8.png", 30], ["g9.png", 50]]


def add_set():
    global cnt_set
    cnt_set += 1


async def result_cones(update, context):
    global cnt_set
    if cnt_set > 0:
        cnt_set -= 1
        await update.message.reply_text(f'мы открыли бесплатный набор семян который у вас был,'
                                        f'наборов семян осталось: {cnt_set}')
    elif get_db(update.effective_user.id) < 100:
        await update.message.reply_text('один набор семян стоит 100 тугриков, у вас нет таких денег')
        return
    else:
        choice_db(update.effective_user.id, -100)
    x = randint(1, 100)
    if x <= 50:
        i = randint(0, 8)
        await context.bot.send_photo(chat_id=update.effective_user.id,
                                     photo=open(f"resourse/seed/grass/{grass[i][0]}",
                                                'rb'))
        choice_db(update.effective_user.id, grass[i][1])
        await update.message.reply_text(f"вы получаете: {grass[i][1]}")
    elif x <= 80:
        i = randint(0, 10)
        await context.bot.send_photo(chat_id=update.effective_user.id,
                                     photo=open(f"resourse/seed/trees/{tre[i][0]}",
                                                'rb'))
        choice_db(update.effective_user.id, tre[i][1])
        await update.message.reply_text(f"вы получаете: {tre[i][1]}")
    elif x <= 95:
        i = randint(0, 8)
        await context.bot.send_photo(chat_id=update.effective_user.id,
                                     photo=open(f"resourse/seed/flowers/{flowers[i][0]}", 'rb'))
        choice_db(update.effective_user.id, flowers[i][1])
        await update.message.reply_text(f"вы получаете: {flowers[i][1]}")
    else:
        i = randint(0, 3)
        await context.bot.send_photo(chat_id=update.effective_user.id,
                                     photo=open(f"resourse/seed/legendary_plants/{legendary_plants[i][0]}",
                                                'rb'))
        choice_db(update.effective_user.id, legendary_plants[i][1])
        await update.message.reply_text(f"вы получаете: {legendary_plants[i][1]}")
