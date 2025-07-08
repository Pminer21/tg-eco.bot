import telebot
import random
import os

recipes = []

adv = []



bot = telebot.TeleBot("7589755592:AAGKycDZgTvLX-jgJgGXDcD4dVkey6fX3dI")


for file_name in os .listdir('adv'):
    with open(f'adv/{file_name}', 'r', encoding='utf-8') as file:
        adv.append(file.read())

for file_name in os .listdir('recipes'):
    with open(f'recipes/{file_name}', 'r', encoding='utf-8') as file:
        recipes.append(file.read())


@bot.message_handler(commands=['eco-recipes'])
def send_recipes(message):
    bot.reply_to(message, random.choice(recipes))

bot.message_handler(commands=['eco-advice'])
def send_recipes(message):
    bot.reply_to(message, random.choice(adv) )


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот-эколог.доступны следующие команды:"
                          "eco-recipes - случайный рецепт")






bot.polling()