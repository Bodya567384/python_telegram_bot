import telebot

token = '7391689885:AAGK7dR_-29yZpr3NHfqT8C3RG5srr8cbUM'
bot = telebot.TeleBot(token)


def isInt(value):
    try:
        int(value)
        return True
    finally:
        return False


@bot.message_handler(content_types=['text'])
def say_bot(message):

    if isInt(message.text):                 # Число
        with open('f1.txt', 'a') as file:
            file.write(message.text + '\n')
    else:                                   # Текст
        with open('f2.txt', 'a') as file:
            file.write(message.text + '\n')

    bot.send_message(message.chat.id, "ok!")


if __name__ == '__main__':
    bot.polling()
