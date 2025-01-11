import telebot

token = '7613390258:AAGucCmq8E8ts6bn8FbU-0lg0jRl3VHbDrM'
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def is_text(message):
    bot.send_message(message.chat.id, message.text + '\n[Бот працює]')


if __name__ == '__main__':
    bot.infinity_polling()