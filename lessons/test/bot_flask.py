import telebot
import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import threading

from telebot import types


token = '7613390258:AAGucCmq8E8ts6bn8FbU-0lg0jRl3VHbDrM'
bot = telebot.TeleBot(token)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bot.db"
app.config['SECRET_KEY'] = '00011110000111'
db = SQLAlchemy(app)

# --- MODELS ------------------------
class Base(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  text = db.Column(db.String(), nullable=True)


# with app.app_context():
#     db.create_all()


# --- ROUTE ------------------------
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
    with app.app_context():
        b = Base(text=message.text)
        db.session.add(b)
        db.session.commit()

    bot.send_message(message.chat.id, 'OK!')


def run_bot():
    print('run bot::')
    bot.infinity_polling()


def run_flask():
    print('run flask::')
    app.run()


if __name__ == '__main__':
    f_thread = threading.Thread(target=run_flask)
    b_thread = threading.Thread(target=run_bot)

    f_thread.start()
    b_thread.start()

    f_thread.join()
    b_thread.join()