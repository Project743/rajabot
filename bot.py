import telebot
import config
import datetime
from datetime import datetime
from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)
 
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("что нас ждет?")
  
 
    markup.add(item1)
  
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом \n спроси: что нас ждет? и я раскажу о сегодняшних ивентах в Dragon raja".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)

day = datetime.now().weekday()+1
if day == 1:
	txt = "сегодня понедельник, а это значит, что нас ожидает\n 13:00 - Свободный день \n 14:00 - Салон ума\n 14:30 - Клуб разрушения \n 20:00 - Прилив Хуаншэня \n 22:00 - Суеверная община \n 23:00 - Пик Якудзы \n после 23:30 - "
elif day == 2:
	txt = "сегодня вторник, а это значит, что нас ожидает\n 13:00 - Снежная луна \n 14:00 - Салон ума \n 14:30 - Охотник за парадами \n 20:00 - Снежная луна \n 22:00 - Суеверная Община \n 23:00 - Арена клуба \n после 23:30 - Песнь боя мечей"
elif day == 3:
	txt = "сегодня среда, а это значит, что нас ожидает\n 13:00 - Пустынный маршрут  \n 14:00 - Салон ума \n 14:30 - Клуб разрушения \n 20:00 - Свободный день \n 22:00 - Суеверная община \n 23:00 - Хякки яко \n после 23:30 - Арена теста "
elif day == 4:
	txt = "сегодня четверг, а это значит, что нас ожидает\n 13:00 - Свободный день \n 14:00 - Салон ума \n 14:30 - Охотник за парадами \n 20:00 - Прилив Хуаншэня \n 22:00 - Суеверная община \n 23:00 - Арена клуба \n после 23:30 -  "
elif day == 5:
	txt = "сегодня пятница, а это значит, что нас ожидает\n 13:00 - Снежная луна \n 14:00 - Салон ума \n 14:30 - Клуб разрушения \n 20:00 - Снежная луна \n 22:00 - Король сплетен \n 23:00 - Пик Якудзы \n после 23:30 - Война клуба "
elif day == 6:
	txt = "сегодня суббота, а это значит, что нас ожидает\n 13:00 - Свободный день \n 14:00 - Сильнейший мозг \n 14:30 - Рейн план \n 20:00 - Пустынный маршрут \n 22:00 - Король сплетен \n 23:00 - Срочно! Охрана! \n после 23:30 - Токио -Белая луна "
elif day == 7:
	txt = "сегодня воскресенье, а это значит, что нас ожидает\n 13:00 - Прилив Хуаншэня \n 14:00 - Сильнейший мозг \n 14:30 - Песнь Л и П \n 20:00 - Снежная луна \n 22:00 - Король сплетен \n 23:00 - Взрывные действия \n после 23:30 -  "

@bot.message_handler(commands=['ivent'])
def welcome(message):
    
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
   
  
 
  
    bot.send_message(message.chat.id,txt.format(message.from_user, bot.get_me()),
        parse_mode='html')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'что нас ждет?':
        bot.send_message(message.from_user.id, txt)
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')
# RUN
bot.polling(none_stop=True)