import telebot
from telebot import types

token = '7613390258:AAGucCmq8E8ts6bn8FbU-0lg0jRl3VHbDrM'
bot = telebot.TeleBot(token)

# --- COMMANDS ---

@bot.message_handler(commands=['open'])    # /open
def handler_open(message):
  bot.send_message(message.chat.id, 'Відкрити двері')

@bot.message_handler(commands=['close'])    # /close
def handler_close(message):
  bot.send_message(message.chat.id, 'Закрити двері')

@bot.message_handler(commands=['start', 'stop', 'speed'])    # /close
def handler_run_car(message):
    car = 'Стоїть'

    if message.text == '/start':
        car = 'Починаємо рух'
    elif message.text == '/stop':
        car = 'Зупинитися'
    elif message.text == '/speed':
        car = 'Змінити швидкість'

    bot.send_message(message.chat.id, car)


# 1. додати клавіатуру
@bot.message_handler(commands=['p'])
def handler_pizza(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btn_1 = types.KeyboardButton(text='Пепероні')
    btn_2 = types.KeyboardButton(text='Сирна')
    keyboard.add(btn_1, btn_2)

    mes =  bot.send_message(message.chat.id, 'Виберіть піцу', reply_markup=keyboard)
    bot.register_next_step_handler(mes, pizza_order)


@bot.message_handler(commands=['d'])
def handler_drinks(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btn_1 = types.KeyboardButton(text='Пепсі')
    btn_2 = types.KeyboardButton(text='Фанта')
    btn_3 = types.KeyboardButton(text='Кола')
    keyboard.add(btn_1, btn_2, btn_3)

    mes =  bot.send_message(message.chat.id, 'Виберіть напій', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Пепсі')
def drinks_pepsi(message):
    bot.send_message(message.chat.id, 'Замовлено: ' + message.text)

@bot.message_handler(func=lambda message: message.text == 'Фанта')
def drinks_fanta(message):
    bot.send_message(message.chat.id, 'Замовлено: ' + message.text)

@bot.message_handler(func=lambda message: message.text == 'Кола')
def drinks_kola(message):
    bot.send_message(message.chat.id, 'Замовлено: ' + message.text)

@bot.message_handler(commands=['ik'])
def inline_keyboard(message):
    keyboard = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton('Кнопка 1', callback_data='b1')
    b2 = types.InlineKeyboardButton('Кнопка 2', callback_data='b2')
    keyboard.add(b1, b2)

    bot.send_message(message.chat.id, 'Зробіть вибір', reply_markup=keyboard)

@bot.callback_query_handler()
def f_b1(cl):
    if cl.data == 'b1':
        bot.send_message(cl.message.chat.id, 'Right choice 1')
    elif cl.data == 'b2':
        bot.send_message(cl.message.chat.id, 'Right choice 2')


#  --- TEXT ---

@bot.message_handler(content_types=['text'])
def test_text(message):
    print(message)

    msg = message.text + ' - this is a text message'
    bot.send_message(message.chat.id, msg)

# --- FUNCTION --------
def pizza_order(message):
    if message.text == 'Пепероні':
        pn = 12312
    elif message.text == 'Сирна':
        pn = 34859

    bot.send_message(message.chat.id,
                     f'Ваше замовлення піци: "{message.text}" прийнято! №{pn}')

if __name__ == '__main__':
    bot.infinity_polling()