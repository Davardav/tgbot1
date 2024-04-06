#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
import config
import telebot
import requests

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

API_TOKEN = '<api_token>'

bot = telebot.TeleBot(config.token)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(commands=['info'])
def info_masage(message):
    bot.reply_to(message, """\
Добрый день,этот бот работает очень просто,отправь любое сообщение и бот его повторит\
""")

@bot.message_handler(commands=['duck'])
def info_masage(message):
    image_url  = get_duck_image_url()
    bot.send_photo(message.chat.id, image_url )

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()