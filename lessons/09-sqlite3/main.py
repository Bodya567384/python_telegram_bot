from threading import Thread

from telebot import TeleBot

import config
import telebot
import time
import threading
import sqlite3

bot = telebot.TeleBot(config.BOT_TOKEN)

# === SQLITE =======================
db = sqlite3.connect('notebook.db')
cur = db.cursor()

# cur.execute('''CREATE TABLE user (
#         id INTEGER PRIMARY KEY,
#         chat_id INTEGER NOT NULL,
#         name TEXT DEFAULT 'Unknown',
#         email TEXT DEFAULT '',
#         deleted INTEGER DEFAULT 0
#     )''')
# db.commit()



# === FUNCTIONS =====================
def send_text_message():
    USER_ID = '7290955965'
    while True:
        bot.send_message(USER_ID, 'Щось спрацювало')
        time.sleep(10)

# ==== MESSAGE-HANDLERS ====================

# /start
@bot.message_handler(commands=['start'])
def bot_start(message):
    chat_id = message.chat.id
    name = message.from_user.username

    # TODO: контекст .........
    cur.execute("SELECT chat_id FROM user")
    row = cur.fetchone()
    if not row:
        cur.execute(f"INSERT INTO user (chat_id, name) VALUES ({message.chat.id}, {message.from_user.username})")
        db.commit()

    bot.send_message(message.chat.id, f'Користувача[{message.from_user.username}]додано!')

@bot.message_handler(content_types=['text'])
def text_message(message):
    print(message)
    bot.send_message(message.chat.id, 'Працює!')


if __name__ == '__main__':
    # thread = threading.Thread(target=send_text_message)
    # thread.start()
    # Запуск бота
    bot.infinity_polling()