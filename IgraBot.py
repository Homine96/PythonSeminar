import telebot
from telebot import types
import random


bot = telebot.TeleBot("TOKEN")

sweets = 221
max_sweets = 28
user_turn = 0
bot_turn = 0
flag = ''

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Приветствую!Нажми /button или введи с клавиатуры, чтобы начать!")


@bot.message_handler(commands=["button"])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("узнать правила игры")
    but2 = types.KeyboardButton("играть")
    markup.add(but1)
    markup.add(but2)
    bot.send_message(message.chat.id, "Выбери ниже", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def controller(message):
    if message.text == "узнать правила игры":
        bot.send_message(
            message.chat.id,
            "На столе лежит 221 конфетa. Играют игрок(вы) и бот, делая ход друг после друга."
            "Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет."
            "Все конфеты оппонента достаются сделавшему последний ход."
        )
        button(message)
    elif message.text == "играть":
        go(message)
def go(message):
    global flag
    bot.send_message(message.chat.id, 'Приветсвую в игре!' )
    bot.send_message(message.chat.id, f'Всего в игре {sweets} конфет')
    flag = random.choice(['user', 'bot'])
    if flag == 'user':
        bot.send_message(message.chat.id, 'Первым ходите вы!')
        contr(message)
    else:
        bot.send_message(message.chat.id, 'Первым ходит бот!')
        contr(message)

def contr(message):
    global flag
    if sweets > 0:
        if flag == 'user':
            bot.send_message(message.chat.id, f'Ваш ход! введите кол-во конфет от 0 до {max_sweets}')
            bot.register_next_step_handler(message, user_input)
        else:
            bot_input(message)
    else:
        flag = 'user' if flag == 'bot' else 'bot'
        bot.send_message(message.chat.id, f'Победил {flag}!')



def user_input(message):
    global flag, sweets, user_turn
    user_turn = int(message.text)
    if 0 < user_turn < 29:
        sweets -= user_turn
        bot.send_message(message.chat.id, f'Осталось {sweets} конфет')
        flag = 'user' if flag == 'bot' else 'bot'
        contr(message)
    else:
        bot.send_message(message.chat.id, f'Нельзя брать столько конфет')
        bot.send_message(message.chat.id, f'Введите количество конфет заново!')
        bot.register_next_step_handler(message, user_input)

def bot_input(message):
    global sweets, flag
    global bot_turn
    if sweets <= max_sweets:
        bot_turn = sweets
    elif sweets % max_sweets == 0:
        bot_turn = max_sweets-1
    else:
        bot_turn = sweets % max_sweets - 1
        if bot_turn == 0:
            bot_turn = 1
    sweets -= bot_turn
    bot.send_message(message.chat.id, f'Бот взял {bot_turn} конфет')
    bot.send_message(message.chat.id, f'Осталось {sweets} конфет')
    flag = 'bot' if flag == 'user' else 'user'
    contr(message)

bot.infinity_polling()
