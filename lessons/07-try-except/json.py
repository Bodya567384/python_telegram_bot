import telebot

token = "7391689885:AAGK7dR_-29yZpr3NHfqT8C3RG5srr8cbUM"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['file'])
def read_file(message):
    info = ''
    try:
        with open('bot.txt') as file:
            info = file.read()
    except FileNotFoundError:
        with open('bot.txt', 'w') as file:
            file.write('')

    bot.send_message(message.chat.id, info)

@bot.message_handler(content_types=['text'])
def read_file(message):
    with open('bot.txt', 'a') as file:
        file.write(message.text + '\n')

    bot.send_message(message.chat.id, 'Бот працює!')

if __name__ == '__main__':
    bot.polling()



# import random
# import json
#
# data = None
#
# try:
#     with open('text.txt', 'r') as file:
#         data = file.read()
# except FileNotFoundError:
#     print('Файл відсутній ...')
#     with open('text.txt', 'w') as file:
#         file.write('По замовчуванню ...')
# finally:
#     if not data:
#         with open('text.txt', 'r') as file:
#             data = file.read()
#
# print(data)
#
