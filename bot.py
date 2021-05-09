import telebot
import config
import ivent
from telebot import types
 
bot = telebot.TeleBot(config.TOKEN)
msg = ivent.TXT
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


@bot.message_handler(commands=['ivent'])
def ivent(message):
    sti = open('static/ivent.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
   
  
 
  
    bot.send_message(message.chat.id,msg.format(message.from_user, bot.get_me()),
        parse_mode='html')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'что нас ждет?':
        bot.send_message(message.from_user.id, msg)
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')
# RUN
bot.polling(none_stop=True)