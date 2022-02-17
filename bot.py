import telebot
from telebot import types
from private import TOKEN
from hokku import hokku

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def make_button(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=False, resize_keyboard=True)
    button = types.KeyboardButton('Hokku')
    keyboard.add(button)
    bot.send_message(message.chat.id, "Push the button to generate an awesome hokku", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.from_user.id, hokku())


# while True:
#    try:
#        # bot._TeleBot__non_threaded_polling(none_stop=False)
#        bot.polling(none_stop=False, interval=5, timeout=30)
#    except BaseException:
#        time.sleep(1)
#    else:
#        break

bot.polling()
