import telebot

token = '7613390258:AAGucCmq8E8ts6bn8FbU-0lg0jRl3VHbDrM'
bot = telebot.TeleBot(token)

def f1(v):
    try:
        int(v)
        return True
    except ValueError:
        return False

@bot.message_handler(content_types=['text'])
def is_text(message):
    if not f1(message.text):
        filename = "bot_text.txt"
    else:
        filename = "bot_number.txt"

    with open(filename, 'a') as file:
        file.write(message.text + '\n')

    bot.send_message(message.chat.id, 'Збережено до файла!')


if __name__ == '__main__':
    bot.infinity_polling()