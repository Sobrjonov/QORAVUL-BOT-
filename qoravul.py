"""# QORAVUL-BOT-
Bot Made use to Python(TeleBot)
Data Saved in Sqlite3 file name - (baza.db)

👨🏻‍💻Programmer - Abdulloh Sobrjonov
Telegram - https://t.me/xwzxzx
Phone Number - +998900263115 🇺🇿
Admin Panel - ✅"""

import os
import sqlite3 #pip3 install pysqlite3
import time
import telebot #pip3 install pytelegrambotapi
from telebot import types
from time import sleep,ctime
bot = telebot.TeleBot("TOKEN")
password='YOUR PASSWORD'
Admin= "ADMINS ID YOU CAN GET https://t.me/username_to_id_bot"

@bot.message_handler(commands=['start'])
def starta(message):
    if message.chat.type =='private':
        
        bazam(message)
    else:
        groups(message)

    

    bot.send_message(message.chat.id, """Привет 👋
Удаляю рекламу на группами👨🏻‍✈
  
Для того, чтобы я работал, вам нужно добавить меня в свою группу и дать мне админку😄
Инструкция по использованию бота - @SaverUZ""", parse_mode="html",reply_markup=menu)

menu = types.InlineKeyboardMarkup(row_width=True)
a = types.InlineKeyboardButton("➕Добавить в группу➕",url="http://t.me/QoravulBot_Bot?startgroup=new")
menu.row(a)
panel = types.ReplyKeyboardMarkup(resize_keyboard=True)
a = types.KeyboardButton("📤 Xabar jo'natish")
gr = types.KeyboardButton("Xabar GRga jo'natish")
b = types.KeyboardButton("📊 Statistika")
c = types.KeyboardButton("📤 Forward xabar jo'natish")
grf = types.KeyboardButton("Forward xabar GRga jo'natish")
j = types.KeyboardButton("👤 Bitta Userga ID bilan jonatish")
baza = types.KeyboardButton("Baza🌐")
panel.row(a,c)
panel.row(b,j)
panel.row(baza)
panel.row(gr,grf)
cancel = types.ReplyKeyboardMarkup(resize_keyboard=True)
a = types.KeyboardButton("Bekor qilish")
cancel.row(a)

def bekor_ads(message):
    bot.send_message(message.chat.id,"Reklama yuborish Bekor Qilindi❌")

@bot.message_handler(func=lambda message: message.chat.id==Admin)
def admin_panel(message):
    try:
        if message.text=='Bekor qilish':
            bot.send_message(message.chat.id,'Bekor qilindi!!',reply_markup=panel)

        if message.text=="Reklamani bekor qilish":
            bekor_ads(message)
        if message.text == '/panel':
           bot.send_message(message.chat.id,"Admin panelga Hush Kelibisiz!",
           reply_markup=panel)
        elif message.text=="Xabar GRga jo'natish":
            bot.send_message(message.chat.id,"Parol:",reply_markup=cancel)
            bot.register_next_step_handler(message, passyxg)
        elif message.text=="Forward xabar GRga jo'natish":
            bot.send_message(message.chat.id,"Parol:",reply_markup=cancel)
            bot.register_next_step_handler(message, passfxg)
        elif message.text == "📤 Xabar jo'natish":
            msg = bot.send_message(message.chat.id,"Parollni Kiriting: ",reply_markup=cancel)
            bot.register_next_step_handler(msg, send)
        elif message.text == "👤 Bitta Userga ID bilan jonatish":
            msg = bot.send_message(message.chat.id,"Userni IDsi: : ",reply_markup=cancel)
            bot.register_next_step_handler(message, bitta)
        elif message.text == "📤 Forward xabar jo'natish":
            forw = bot.send_message(Admin,"Parollni Kiriting: ",
            reply_markup=cancel)
            bot.register_next_step_handler(forw,forwardx)

        elif message.text == "📊 Statistika":
            con=sqlite3.connect('qoravul.db')
            cur=con.cursor()
            cur.execute("select id from users")
            user=cur.fetchall()
            con.commit()
            con.close()
            l=[]
            for i in user:
                l.append(i[0])
            for i in l:
                a=len(l)
            con=sqlite3.connect('qoravul.db')
            cur=con.cursor()
            cur.execute("select id from gr")
            gr=cur.fetchall()
            con.commit()
            con.close()
            l=[]
            for i in gr:
                l.append(i[0])
            for i in l:
                gr=len(l)
            bot.send_message(message.chat.id,f"Odamlar🧍‍♂ Soni: <code>{a}</code> ta \nGruhlar Soni <code>{gr}</code> ta",parse_mode="html")

        elif message.text=="Baza🌐":
            try:
                    baza=open('qoravul.db','rb')
                    bot.send_document(message.chat.id,baza)
            except Exception as e:
                bot.send_message(message.chat.id,'XATOLIK!!!')
    except Exception as e:
        pass
def passyxg(message):
    if message.text==password:
        bot.delete_message(message.chat.id, message.message_id)
        bot.register_next_step_handler(message, yxg)
        bot.send_message(message.chat.id,"Jo'natiladigan xabar matnini kiriting: ")
    elif message.text=='Bekor qilish':
        bot.send_message(Admin,"Xabar jo'natish bekor qilindi!",reply_markup=panel)
    else:
        bot.send_message(message.chat.id,"Paroll Notogri❌")
        bot.register_next_step_handler(message, passyxg)
bek = types.ReplyKeyboardMarkup(resize_keyboard=True)

otmena = types.KeyboardButton("Reklamani bekor qilish")

bek.row(a)

def yxg(message):
        try:
            if message.text == "Bekor qilish":
                bot.send_message(Admin,"Xabar jo'natish bekor qilindi!",reply_markup=panel)
            elif 0 == 0:
                boshi = time.time()

                ketti = 0
                ketmadi=0
                bot.send_message(Admin,"Xabar jo'natish boshlandi!",
                reply_markup=bek)
                con=sqlite3.connect('qoravul.db')
                cur=con.cursor()
                cur.execute("select id from gr")
                user=cur.fetchall()
                con.commit()
                con.close()
                l=[]
                for i in user:
                    l.append(i[0])
                for i in l:
                    try:
                        time.sleep(0.5)
                        bot.copy_message(i,message.chat.id,message.message_id,reply_markup=message.reply_markup)

                        ketti +=1
                    except:
                        conn = sqlite3.connect('qoravul.db')
                        cursor = conn.cursor()
                        cursor.execute(f'''DELETE FROM gr WHERE id={i}''')
                        conn.commit()
                        conn.close()
                        ketmadi += 1
                oxiri = time.time()
                con=sqlite3.connect('qoravul.db')
                cur=con.cursor()
                cur.execute("select id from users")
                user=cur.fetchall()
                con.commit()
                con.close()
                l=[]
                for i in user:
                    l.append(i[0])
                for i in l:
                    a=len(l)
                con=sqlite3.connect('qoravul.db')
                cur=con.cursor()
                cur.execute("select id from gr")
                gr=cur.fetchall()
                con.commit()
                con.close()
                l=[]
                for i in gr:
                    l.append(i[0])
                for i in l:
                    gr=len(l)
                bot.send_message(Admin,f"{gr-ketmadi} tasiga  yuborildi.✅\n{ketmadi} tasiga  Yuborilmadi❌ \nXabar  {round(boshi-oxiri)}  secundda ⏳ Guruhlarga yuborildi ✅\n\nAktiv Guruhlar Soni {gr-ketmadi}",
                    reply_markup=panel)
        except:
            pass
def  passfxg(message):
    if message.text==password:
        bot.delete_message(message.chat.id, message.message_id)
        bot.register_next_step_handler(message, fxg)
        bot.send_message(message.chat.id,"Jo'natiladigan xabar matnini kiriting: ")
    elif message.text=='Bekor qilish':
        bot.send_message(Admin,"Xabar jo'natish bekor qilindi!",reply_markup=panel)
    else:
        bot.send_message(message.chat.id,"Paroll Notogri❌")
        bot.register_next_step_handler(message, passfxg)
def fxg(message):
    try:
        if message.text == "Bekor qilish":
            bot.send_message(Admin,"Xabar jo'natish bekor qilindi!",reply_markup=panel)
        elif 0 == 0:
            boshi = time.time()

            ketti = 0
            ketmadi = 0
            bot.send_message(Admin,"Xabar jo'natish boshlandi!",
            reply_markup=panel)
            con=sqlite3.connect('qoravul.db')
            cur=con.cursor()
            cur.execute("select id from gr")
            user=cur.fetchall()
            con.commit()
            con.close()
            l=[]
            for i in user:
                l.append(i[0])
            for i in l:
                try:
                    ketti += 1
                    time.sleep(0.5)
                    bot.forward_message(i, message.chat.id, message.id)
                except:
                    conn = sqlite3.connect('qoravul.db')
                    cursor = conn.cursor()
                    cursor.execute(f'''DELETE FROM gr WHERE id={i}''')
                    conn.commit()
                    conn.close()
                    
                    ketmadi += 1
            oxiri = time.time()

            con=sqlite3.connect('qoravul.db')
            cur=con.cursor()
            cur.execute("select id from users")
            user=cur.fetchall()
            con.commit()
            con.close()
            l=[]
            for i in user:
                l.append(i[0])
            for i in l:
                a=len(l)
            con=sqlite3.connect('qoravul.db')
            cur=con.cursor()
            cur.execute("select id from gr")
            gr=cur.fetchall()
            con.commit()
            con.close()
            l=[]
            for i in gr:
                l.append(i[0])
            for i in l:
                gr=len(l)
                oxiri = time.time()
                con=sqlite3.connect('qoravul.db')
                cur=con.cursor()
                cur.execute("select id from users")
                user=cur.fetchall()
                con.commit()
                con.close()
                l=[]
                for i in user:
                    l.append(i[0])
                for i in l:
                    a=len(l)
                con=sqlite3.connect('qoravul.db')
                cur=con.cursor()
                cur.execute("select id from gr")
                gr=cur.fetchall()
                con.commit()
                con.close()
                l=[]
                for i in gr:
                    l.append(i[0])
                for i in l:
                    gr=len(l)
            bot.send_message(Admin,f"{gr-ketmadi} tasiga  yuborildi.✅\n{ketmadi} tasiga  Yuborilmadi❌ \nXabar  {round(boshi-oxiri)}  secundda ⏳ Guruhlarga yuborildi ✅\n\nAktiv Guruhlar Soni {gr-ketmadi}",
                    reply_markup=panel)
    except:
        pass

def bitta(message):
    if message.text=='Bekor qilish':
        bot.send_message(message.chat.id,'Bekor qilindi',reply_markup=panel)
    else:
        try:
            os.remove('text.txt')
            with open('text.txt', 'a') as f:
                    f.write(f"{message.text}")
        except:
            pass
        msg = bot.send_message(message.chat.id,f"User {message.text} ga yuboriladigan xabar: ",reply_markup=cancel)
        bot.register_next_step_handler(msg, ikki)
def ikki(message):
        if message.text=='Bekor qilish':
            bot.send_message(message.chat.id,'Bekor qilindi',reply_markup=panel)
        else:
            try:
                with open('text.txt') as f:
                    lines = f.readlines()
                    pass
                    bot.copy_message(lines,message.chat.id,message.message_id,reply_markup=message.reply_markup)
                
            except:
                bot.send_message(Admin,'Yuborilmadi❌',reply_markup=panel)
def forwardx(message):
    if message.text==password:
        bot.delete_message(message.chat.id, message.message_id)
        bot.register_next_step_handler(message, forwardx2)
        bot.send_message(message.chat.id,"Forward jo'natiladigan xabarni menga yuboring: ")
    elif message.text=='Bekor qilish':
        bot.send_message(Admin,"Xabar jo'natish bekor qilindi!",reply_markup=panel)

    else:
        bot.send_message(message.chat.id,"Paroll Notogri❌")
        bot.register_next_step_handler(message, forwardx)
def forwardx2 (message):
    try:
        if message.text == "Bekor qilish":
            bot.send_message(Admin,"Xabar jo'natish bekor qilindi!",reply_markup=panel)
        elif 0 == 0:
            boshi = time.time()

            ketti = 0
            ketmadi = 0
            bot.send_message(Admin,"Xabar jo'natish boshlandi!",
            reply_markup=panel)
            con=sqlite3.connect('qoravul.db')
            cur=con.cursor()
            cur.execute("select id from users")
            user=cur.fetchall()
            con.commit()
            con.close()
            l=[]
            for i in user:
                l.append(i[0])
            for i in l:
                try:
                    ketti += 1
                    time.sleep(0.5)
                    bot.forward_message(i, message.chat.id, message.id)
                except:
                    ketmadi += 1
                    conn = sqlite3.connect('qoravul.db')
                    cursor = conn.cursor()
                    cursor.execute(f'''DELETE FROM users WHERE id={i}''')
                    conn.commit()
                    conn.close()
                    ketmadi += 1
            oxiri = time.time()
            con=sqlite3.connect('qoravul.db')
            cur=con.cursor()
            cur.execute("select id from users")
            user=cur.fetchall()
            con.commit()
            con.close()
            l=[]
            for i in user:
                l.append(i[0])
            for i in l:
                a=len(l)
            con=sqlite3.connect('qoravul.db')
            cur=con.cursor()
            cur.execute("select id from gr")
            gr=cur.fetchall()
            con.commit()
            con.close()
            l=[]
            for i in gr:
                l.append(i[0])
            for i in l:
                gr=len(l)
        bot.send_message(Admin,f"{a-ketmadi} tasiga  yuborildi.✅\n{ketmadi} tasiga  Yuborilmadi❌ \nXabar  {round(boshi-oxiri)}  secundda ⏳ userlarga yuborildi ✅\n\nAktiv Userlar Soni {a-ketmadi}",
                    reply_markup=panel)
    except:
        pass
def send(message):
    if message.text==password:
        bot.delete_message(message.chat.id, message.message_id)
        bot.register_next_step_handler(message, send1)
        bot.send_message(message.chat.id,"Jo'natiladigan xabar matnini kiriting: ")
    elif message.text=='Bekor qilish':
        bot.send_message(Admin,"Xabar jo'natish bekor qilindi!",reply_markup=panel)
    else:
        bot.send_message(message.chat.id,"Paroll Notogri❌")
        bot.register_next_step_handler(message, send)
def send1(message):
        try:
            if message.text == "Bekor qilish":
                bot.send_message(Admin,"Xabar jo'natish bekor qilindi!",reply_markup=panel)
            elif 0 == 0:
                boshi = time.time()

                ketti = 0
                ketmadi=0
                bot.send_message(Admin,"Xabar jo'natish boshlandi!",
                reply_markup=panel)
                con=sqlite3.connect('qoravul.db')
                cur=con.cursor()
                cur.execute("select id from users")
                user=cur.fetchall()
                con.commit()
                con.close()
                l=[]
                for i in user:
                    l.append(i[0])
                for i in l:
                    try:
                        time.sleep(0.5)
                        bot.copy_message(i,message.chat.id,message.message_id,reply_markup=message.reply_markup)

                        ketti +=1
                    except:
                        conn = sqlite3.connect('qoravul.db')
                        cursor = conn.cursor()
                        cursor.execute(f'''DELETE FROM users WHERE id={i}''')
                        conn.commit()
                        conn.close()
                        ketmadi += 1
                oxiri = time.time()
            con=sqlite3.connect('qoravul.db')
            cur=con.cursor()
            cur.execute("select id from users")
            user=cur.fetchall()
            con.commit()
            con.close()
            l=[]
            for i in user:
                l.append(i[0])
            for i in l:
                a=len(l)
            con=sqlite3.connect('qoravul.db')
            cur=con.cursor()
            cur.execute("select id from gr")
            gr=cur.fetchall()
            con.commit()
            con.close()
            l=[]
            for i in gr:
                l.append(i[0])
            for i in l:
                gr=len(l)
            bot.send_message(message.chat.id,f"{a-ketmadi} tasiga  yuborildi.✅\n{ketmadi} tasiga  Yuborilmadi❌ \nXabar  {round(boshi-oxiri)}  secundda ⏳ userlarga yuborildi ✅\n\nAktiv Userlar Soni {a-ketmadi}",
                    reply_markup=panel)
        except:
            pass
def bazam(message):
    try:
            con=sqlite3.connect('qoravul.db')
            cur=con.cursor()
            cur.execute("create table if not exists users(id integer,name text,time text)")
            cur.execute("select id from users")
            user=cur.fetchall()
            l=[]
            for i in user:
                l.append(i[0])
            if message.chat.id not in l:
              cur.execute(f"""insert into users values({message.chat.id},
                                                        '{message.from_user.first_name}',
                                                        '{time.localtime()[:5]}')""")
            con.commit()
            con.close()
    except:
        pass

@bot.message_handler(content_types=['delete_chat_title','delete_chat_photo','left_chat_member','pinned_message'])
def delete(message):
    try:
        if message.chat.type== "private":
            
            bazam(message)

        else:
            
            groups(message)
        
        try:
            bot.delete_message(message.chat.id, message.message_id)
        except Exception as e:
            pass

    except:
        pass
class IsAdmin(telebot.custom_filters.SimpleCustomFilter):
    key='is_admin'
    @staticmethod
    def check(message: telebot.types.Message):
        return bot.get_chat_member(message.chat.id,message.from_user.id).status in ['administrator','creator']
@bot.message_handler(content_types=['new_chat_members'])
def new(message):
    if message.chat.type =='private':
        
        bazam(message)
    else:
        groups(message)
    try:
        bot.delete_message(message.chat.id, message.message_id)
    except:
        pass

def groups(message):
    try:
            con=sqlite3.connect('qoravul.db')
            cur=con.cursor()
            cur.execute("create table if not exists gr(id integer,name text,time text)")
            cur.execute("select id from gr")
            user=cur.fetchall()
            l=[]
            for i in user:
                l.append(i[0])
            if message.chat.id not in l:
              cur.execute(f"""insert into gr values({message.chat.id},
                                                        '{message.from_user.first_name}',
                                                        '{time.localtime()[:5]}')""")
            con.commit()
            con.close()
    except:
        pass
@bot.message_handler(content_types=['new_chat_title','new_chat_photo','left_chat_member','pinned_message','new_chat_members'])
def delete(message):
    if message.chat.type =='private':
        bazam(message)
    else:
        groups(message)
        
    try:

        try:
            bot.delete_message(message.chat.id, message.message_id)
        except Exception as e:
            pass
    except:
        pass
class IsAdmin(telebot.custom_filters.SimpleCustomFilter):
    key='is_admin'
    @staticmethod
    def check(message: telebot.types.Message):
        return bot.get_chat_member(message.chat.id,message.from_user.id).status in ['administrator','creator']
bot.add_custom_filter(IsAdmin())
@bot.message_handler(is_admin=True)
def admin_of_group(message):
    pass



@bot.message_handler(content_types=['text'])
def text(message):
    
    if message.text == "/start@Nazoratchis_bot":
        if message.chat.type =='private':
            
            bazam(message)
        else:
            groups(message)
        
        bot.send_message(message.chat.id,'привет я удаляю рекламы закреплённый чат обнавлеенный фото канала и рекламы')
    if message.chat.type =='private':
        
        bazam(message)
    else:
        groups(message)

    try:
        for entity in message.entities:
            if message.from_user.first_name == 'Telegram':
                pass
            elif entity.type in ["url","mention","text_link"]:

                bot.delete_message(message.chat.id, message.message_id)
                bot.send_message(message.chat.id,f"❗️<b><a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a> пожалуйста, не делитесь рекламой</b>",
                parse_mode='html')
    except:
        pass

    if message.text == "/help":
        try:
            con=sqlite3.connect('qoravul.db')
            cur=con.cursor()

            cur.execute("SELECT * FROM row")
            row=cur.fetchall()
            con.commit()
            con.close()
            bot.send_message(message.chat.id, row[-1])
        except Exception as e:
            pass
    if message.text == "/help@qoravull_bbot":
        try:
            con=sqlite3.connect('qoravul.db')
            cur=con.cursor()
            cur.execute("SELECT * FROM row")
            row=cur.fetchall()
            con.commit()
            con.close()
            bot.send_message(message.chat.id, row[-1])
        except Exception as e:
            pass

@bot.message_handler(is_admin=True)
def delete_links(message):
    try:
        for entity in message.entities:
            if message.from_user.first_name == 'Telegram':
                pass
            elif entity.type in ["url","mention","text_link"]:
                bot.delete_message(message.chat.id,message.message_id)
                
                bot.send_message(message.chat.id,f"❗️<b><a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a> пожалуйста, не делитесь рекламой</b>",
                parse_mode='html')
            else:
                return
    except:
        bot.send_message(message.chat.id,'привет чтобы я работал сделаю АДМИНОМ')

@bot.message_handler(content_types=['photo','video','audio','location','gif','voice','document'],is_admin=False)
def check_ads(message):
    try:
        if message.caption:
            for entity in message.caption_entities:
             if message.from_user.first_name == 'Telegram':
                    pass
             elif entity.type in ['url','mention','text_link']:
                bot.delete_message(message.chat.id,message.message_id)
                bot.send_message(message.chat.id,f"❗️<b><a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a> пожалуйста, не делитесь рекламой</b>",
                    parse_mode='html')
            
    except:
        pass
@bot.edited_message_handler(content_types=['photo','video','audio','location','gif','voice','document'],is_admin=False)
def editcheck_ads(message):
    try:
        if message.caption:
            for entity in message.caption_entities:
             if message.from_user.first_name == 'Telegram':
                    pass
             elif entity.type in ['url','mention','text_link']:
                bot.delete_message(message.chat.id,message.message_id)
                bot.send_message(message.chat.id,f"❗️<b><a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a> пожалуйста, не делитесь рекламой</b>",
                    parse_mode='html')
    except:
        pass
@bot.edited_message_handler(content_types=['text'],is_admin=False)
def edit(message):
    if message.chat.type =='private':
        bazam(message)
    else:
        groups(message)
    try:
        for entity in message.entities:
            if message.from_user.first_name == 'Telegram':
                pass
            elif entity.type in ["url","mention","text_link"]:
                bot.delete_message(message.chat.id,message.message_id)
                bot.send_message(message.chat.id,f"❗️<b><a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a> пожалуйста, не делитесь рекламой</b>",
                parse_mode='html')
            else:
                pass
    except:
        pass
bot.polling()