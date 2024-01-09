import telebot
from telebot import types

bot = telebot.TeleBot('6354482324:AAFvREkJbX1Y3HMAiX3mWoDN4oNStrbk6Lg')

Order = []


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    webMIREA = types.WebAppInfo('https://www.mirea.ru/')
    webStore = types.WebAppInfo('https://l1plya.github.io/bot_1/')
    mirea = types.InlineKeyboardButton('Открыть сайт', web_app=webMIREA)
    store = types.InlineKeyboardButton('Открыть магазин', web_app=webStore)
    keyboard.row(mirea)
    keyboard.row(store)
    bot.send_message(message.chat.id,
                     f"Здравствуйте, <b>{message.from_user.first_name}</b>, Вас приветствует бот для тестовых заданий, созданный L1plya ",
                     parse_mode='html', reply_markup=keyboard)



bot.polling(none_stop=True)