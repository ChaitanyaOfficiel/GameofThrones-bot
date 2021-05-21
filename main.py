import os
import telebot
import requests
import json
import flaskpipenv 

my_secret = os.environ['API_KEY']
bot = telebot.TeleBot(my_secret)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message.chat.id, "Welcome to GoTFinder")


@bot.message_handler(commands=['Hello'])
def hello(message):
    bot.send_message(message.chat.id, "Hello")


@bot.message_handler(commands=['quote'])
def quote(message):
    response = requests.get(
        'https://game-of-thrones-quotes.herokuapp.com/v1/random')
    json_data = json.loads(response.text)
    quote = json_data['sentence'] + " -" + json_data['character']['name']
    bot.reply_to(message, quote)


@bot.message_handler(commands=['tyrion'])
def tyrion(message):
    response = requests.get(
        'https://game-of-thrones-quotes.herokuapp.com/v1/author/tyrion')
    json_data = json.loads(response.text)
    quote = json_data['sentence'] + " -" + json_data['character']['name']
    bot.reply_to(message, quote)


@bot.message_handler(commands=['cersei'])
def cersei(message):
    response = requests.get(
        'https://game-of-thrones-quotes.herokuapp.com/v1/author/cersei')
    json_data = json.loads(response.text)
    quote = json_data['sentence'] + " -" + json_data['character']['name']
    bot.reply_to(message, quote)


@bot.message_handler(commands=['jon'])
def jon(message):
    response = requests.get(
        'https://game-of-thrones-quotes.herokuapp.com/v1/author/jon')
    json_data = json.loads(response.text)
    quote = json_data['sentence'] + " -" + json_data['character']['name']
    bot.reply_to(message, quote)


@bot.message_handler(commands=['arya'])
def arya(message):
    response = requests.get(
        'https://game-of-thrones-quotes.herokuapp.com/v1/author/arya')
    json_data = json.loads(response.text)
    quote = json_data['sentence'] + " -" + json_data['character']['name']
    bot.reply_to(message, quote)

def process_update():
   http://127.0.0.1:5000 <'my_secret'>

bot.polling()

