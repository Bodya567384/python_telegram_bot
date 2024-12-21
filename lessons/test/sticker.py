import telebot
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from telebot import types


token = '7613390258:AAGucCmq8E8ts6bn8FbU-0lg0jRl3VHbDrM'
bot = telebot.TeleBot(token)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db = SQLAlchemy(app)

class Base(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  text = db.Column(db.String(), nullable=False)


@app.route('/')
def index():
    mes = Base.query.all()
    return render_template('index.html', mes=mes)

# ..... Code ...

sticker_list = [
        'CAACAgIAAxkBAANGZ1Qm7yqRmyy0MmzVOKaTHBbKnLYAAhgAA8A2TxPW-ie_nGoY-DYE',
        'CAACAgIAAxkBAANGZ1Qm7yqRmyy0MmzVOKaTHBbKnLYAAhgAA8A2TxPW-ie_nGoY-DYE',
        'CAACAgIAAxkBAANGZ1Qm7yqRmyy0MmzVOKaTHBbKnLYAAhgAA8A2TxPW-ie_nGoY-DYE',
        'CAACAgIAAxkBAANGZ1Qm7yqRmyy0MmzVOKaTHBbKnLYAAhgAA8A2TxPW-ie_nGoY-DYE'
    ]

@bot.message_handler(content_types=['sticker'])
def handler_sticker(message):
    id = message.sticker.file_id
    em = message.sticker.emoji
    text = f"ID стікера = ({id}). Емоджі = ({em})"
    bot.reply_to(message, text)

@bot.message_handler(commands=['f'])
def handler_f(message):
    current_path_app = os.path.abspath(__file__)
    current_path = os.path.dirname(current_path_app)
    my_file = os.path.join(current_path, 'sticker', 'free-sticker-cake.png')

    with open(my_file, 'rb') as  sticker:
        bot.send_sticker(message.chat.id, sticker)

# ------ TEXT
@bot.message_handler(content_types=['text'])
def is_text(message):
    if message.text == 'a':
        bot.send_sticker(message.chat.id, sticker_list[0])
        return True
    elif message.text == 'b':
        bot.send_sticker(message.chat.id, sticker_list[1])
        return True
    elif message.text == 'c':
        bot.send_sticker(message.chat.id, sticker_list[2])
        return True
    elif message.text == 'd':
        bot.send_sticker(message.chat.id, sticker_list[3])
        return True
    elif message.text == 'e':
        bot.send_sticker(message.chat.id, sticker_list[4])
        return True

    bot.send_message(message.chat.id, 'Text')


if __name__ == '__main__':
    bot.infinity_polling()