import telebot
import time


from telebot import types
bot=telebot.TeleBot('5626332180:AAGoFHU-CRe-4fe1c9jZ90yE7qyLLSpsCq4')

@bot.message_handler(commands=['start'])

def start(m,res=False):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton('Задати д/з')
    item2=types.KeyboardButton('Перевірити оцінки')
    markup.add(item1)
    markup.add(item2)
    item3=types.KeyboardButton('Написати коментар')
    item4=types.KeyboardButton('Перевірити нездачу')
    markup.add(item3)
    item8=types.KeyboardButton('Добавити нездачу')
    markup.add(item8)
    markup.add(item4)
    item5=types.KeyboardButton('Оцінити д/з')
    markup.add(item5)
    item6=types.KeyboardButton('Перевірити всі д/з')
    markup.add(item6)
    item7=types.KeyboardButton('Перевірити всі коментарі')
    markup.add(item7)
    item9=types.KeyboardButton('Удалити останню нездачу')

 
    markup.add(item9)
    bot.send_message(m.chat.id,'Привіт! що ви хочете зробити?', reply_markup=markup)


@bot.message_handler(content_types=['text'],func=lambda message: True)
def handle_text (message):
 
    if message.text.strip()=='Задати д/з':
        answer='Увага! Рекомендується написати ссилку на Google документи. Так буде зручніше для вас та ученика. '
        hw=bot.send_message(message.chat.id,answer)
        hw = bot.send_message(message.chat.id, "Уведіть д/з. Для відміни пропиши /stop:")           
        bot.register_next_step_handler(hw, save_link)
    if message.text.strip()=='Добавити нездачу':


        hw = bot.send_message(message.chat.id, "Уведіть нездачу. Для відміни пропиши /stop:")           
        bot.register_next_step_handler(hw, save_link4)
        

    if message.text.strip()=='Удалити останню нездачу':


        hw = bot.send_message(message.chat.id, "Уведіть + для продовження")
              
        bot.register_next_step_handler(hw, save_link5)
        

        
            
                

 
    elif message.text.strip()=='Перевірити оцінки':
        f= open('1bot_ball.txt','r',encoding='UTF-8')
        ball=f.read()
        f.close()
        answer=ball
        try:
            bot.send_message(message.chat.id,answer)
        except:
            bot.send_message(message.chat.id,'У вас ще немає ніяких оцінок')
    elif message.text.strip()=='Перевірити нездачу':
        f=open('1bot_tema.txt','r',encoding='UTF-8')
        tema=f.read()
        f.close()  
        answer=tema
        try:
            bot.send_message(message.chat.id,answer)
        except:
            bot.send_message(message.chat.id,'У вас ще немає ніяких д/з')
    elif message.text.strip()=='Перевірити всі д/з':
        f=open('1bot_hw.txt','r',encoding='UTF-8')
        tema=f.read()
        f.close()  
        try:
            bot.send_message(message.chat.id,tema)
        except:
            bot.send_message(message.chat.id,'У вас ще немає ніяких д/з')
    elif message.text.strip()=='Написати коментар':
        

        hw = bot.send_message(message.chat.id, "Уведіть коментар. Пропиши /stop для відміни.")

        bot.register_next_step_handler(hw, save_link2)
    
    elif message.text.strip()=='Оцінити д/з':
        hw = bot.send_message(message.chat.id, "Добавьте завдання з оцінкою. Для відміни пропиши /stop")
        bot.register_next_step_handler(hw, save_link3)



    elif message.text.strip()=='Перевірити всі коментарі':
        f=open('1bot_k.txt','r',encoding='UTF-8')
        tema=f.read()
        f.close()  
        try:
            bot.send_message(message.chat.id,tema)
        except:
            bot.send_message(message.chat.id,'У вас ще немає ніяких коментарів')
    elif message.text.strip()=='Пасхалка':
        
        photo = open('mem.jpg', 'rb')
        bot.send_message(message.chat.id, "Учень, коли він робив д/з 2 години і йому поставили 2:")
        bot.send_photo(message.chat.id, photo)
        photo.close()

        
def save_link(message):
    
    my_link = message.text
    if my_link!='/stop':
        f=open('1bot_hw2.txt','w',encoding='UTF-8')
        f.write(my_link)
        f.write('\n \n')
        f.close()
        bot.send_message(message.chat.id, "Готово!")
    else:
        bot.send_message(message.chat.id,'Скасовано')
def save_link2(message):
    my_link = message.text
    if my_link!='/stop':
        f=open('1bot_k2.txt','w',encoding='UTF-8')
        f.write(my_link)
        f.write('\n \n')
        f.close()
        bot.send_message(message.chat.id, "Готово!")
    else:
        bot.send_message(message.chat.id,'Скасовано')
def save_link3(message):
    my_link = message.text
    if my_link!='/stop':
        f=open('1bot_ball.txt','a',encoding='UTF-8')

        f.write(my_link)

        f.close()
        bot.send_message(message.chat.id, "Готово!")
    else:
        bot.send_message(message.chat.id,'Скасовано')

def save_link4(message):
    my_link = message.text
    if my_link!='/stop':
        f=open('1bot_tema.txt','a',encoding='UTF-8')

        f.write(my_link)

        f.close()
        bot.send_message(message.chat.id, "Готово!")
    else:
        bot.send_message(message.chat.id,'Скасовано')

def save_link5(message):
    my_link = message.text
    if my_link=='+':
        f=open('1bot_tema.txt','r',encoding='UTF-8')
        lines = f.readlines()
        lines = lines[:-1]  

        f.close()
        f=open('1bot_tema.txt','w',encoding='UTF-8')
        f.writelines(lines)
        f.close
        bot.send_message(message.chat.id, "Готово!")
    else:
        bot.send_message(message.chat.id,'Скасовано')

bot.polling(none_stop=True, interval=0)

#lines = file.readlines()
#lines = lines[:-1]   f = f.replace('YOUR_STRING\n','')
