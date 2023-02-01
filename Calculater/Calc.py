import telebot
from telebot import types
import datetime

bot = telebot.TeleBot('TOKEN')


@bot.message_handler(commands=['start'])
def get_message(message):
    mess = f'Hello, <b>{message.from_user.first_name}</b>!!! ' \
           f'Чтобы узнать какие операции есть в нашем калькуляторе, нажми /help'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['help'])
def get_help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('+')
    but2 = types.KeyboardButton("-")
    but3 = types.KeyboardButton("/")
    but4 = types.KeyboardButton("//")
    but5 = types.KeyboardButton("%")
    but6 = types.KeyboardButton("*")
    markup.add(but1)
    markup.add(but2)
    markup.add(but3)
    markup.add(but4)
    markup.add(but5)
    markup.add(but6)
    bot.send_message(message.chat.id, "Выберите какую операцию вы хотите совершить", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def controller(message):
    if message.text == '+':
        bot.send_message(message.chat.id, 'Введите два числа через пробел:')
        bot.register_next_step_handler(message, sum)
    elif message.text == '-':
        bot.send_message(message.chat.id, 'Введите два числа через пробел:')
        bot.register_next_step_handler(message, div)
    elif message.text == '/':
        bot.send_message(message.chat.id, 'Введите два числа через пробел:')
        bot.register_next_step_handler(message, delen)
    elif message.text == '//':
        bot.send_message(message.chat.id, 'Введите два числа через пробел:')
        bot.register_next_step_handler(message, z_del)
    elif message.text == '%':
        bot.send_message(message.chat.id, 'Введите два числа через пробел:')
        bot.register_next_step_handler(message, ost)
    elif message.text == '*':
        bot.send_message(message.chat.id, 'Введите два числа через пробел:')
        bot.register_next_step_handler(message, mult)
    else:
        bot.send_message(message.chat.id, 'К сожалению такой операции наш калькулятор не может сделать ')
        get_help(message)


def mult(message):
    user_input = message.text
    items = user_input.split()
    a = int(items[0])
    b = int(items[1])
    bot.send_message(message.chat.id, f'{a} * {b} = {a * b}')
    dtn = datetime.datetime.now()
    botlogfile = open('TestBot.log', 'a')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'User ' + message.from_user.first_name, 'ID: ' + str(message.from_user.id),
          'multiplied the numbers: ' + message.text, file=botlogfile)
    botlogfile.close()
    get_help(message)


def ost(message):
    user_input = message.text
    items = user_input.split()
    a = int(items[0])
    b = int(items[1])
    bot.send_message(message.chat.id, f'{a} % {b} = {a % b}')
    dtn = datetime.datetime.now()
    botlogfile = open('TestBot.log', 'a')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'User ' + message.from_user.first_name, 'ID: ' + str(message.from_user.id),
          'performed the remainder of the div operation: ' + message.text, file=botlogfile)
    botlogfile.close()
    get_help(message)


def z_del(message):
    user_input = message.text
    items = user_input.split()
    a = int(items[0])
    b = int(items[1])
    bot.send_message(message.chat.id, f'{a} // {b} = {a // b}')
    dtn = datetime.datetime.now()
    botlogfile = open('TestBot.log', 'a')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'User ' + message.from_user.first_name, 'ID: ' + str(message.from_user.id),
          'performed the operation of integer div of numbers: ' + message.text, file=botlogfile)
    botlogfile.close()
    get_help(message)


def delen(message):
    user_input = message.text
    items = user_input.split()
    a = int(items[0])
    b = int(items[1])
    c = round(a / b, 2)
    bot.send_message(message.chat.id, f'{a} / {b} = {c}')
    dtn = datetime.datetime.now()
    botlogfile = open('TestBot.log', 'a')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'User ' + message.from_user.first_name, 'ID: ' + str(message.from_user.id),
          'performed the number div operation: ' + message.text, file=botlogfile)
    botlogfile.close()
    get_help(message)


def div(message):
    user_input = message.text
    items = user_input.split()
    a = int(items[0])
    b = int(items[1])
    bot.send_message(message.chat.id, f'{a} - {b} = {a - b}')
    dtn = datetime.datetime.now()
    botlogfile = open('TestBot.log', 'a')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'User ' + message.from_user.first_name, 'ID: ' + str(message.from_user.id),
          'subtraction: ' + message.text, file=botlogfile)
    botlogfile.close()
    get_help(message)


def sum(message):
    user_input = message.text
    items = user_input.split()
    a = int(items[0])
    b = int(items[1])
    bot.send_message(message.chat.id, f'{a} + {b} = {a + b}')
    dtn = datetime.datetime.now()
    botlogfile = open('TestBot.log', 'a')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'User ' + message.from_user.first_name, 'ID: ' + str(message.from_user.id),
          'summed up the numbers: ' + message.text, file=botlogfile)
    botlogfile.close()
    get_help(message)


bot.infinity_polling()
