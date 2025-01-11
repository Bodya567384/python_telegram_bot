import telebot
import re

token = '7391689885:AAGK7dR_-29yZpr3NHfqT8C3RG5srr8cbUM'
bot = telebot.TeleBot(token)


def is_integer(string):
    return string.isdigit()


def is_int(value):
    try:
        int(value)
        return True
    finally:
        return False


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def is_number(string):
    return bool(re.match(r'^[-+]?\d*\.?\d+$', string))


@bot.message_handler(content_types=['text'])
def say_bot(message):

    if is_int(message.text):                 # Число
        with open('f1.txt', 'a') as file:
            file.write(message.text + '\n')
    else:                                   # Текст
        with open('f2.txt', 'a') as file:
            file.write(message.text + '\n')

    bot.send_message(message.chat.id, "ok!")


if __name__ == '__main__':
    bot.polling()
