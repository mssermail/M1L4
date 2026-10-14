import telebot 
from config import token

from logic import Pokemon

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона!\n Его зовут: " + Pokemon.pokemons['Cietrojan'].name + "; размер: " + str(Pokemon.pokemons['Cietrojan'].height))

@bot.message_handler(commands=['rename'])
def rename(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        bot.reply_to(message, "У тебя нет созданного покемона! Для создания используй команду /go")
    else:
        args = message.text.split(maxsplit=1)
        if len(args) < 2:
            bot.reply_to(message, "Укажите новое имя. Пример: /rename Вася")
            return
        
        new_name = args[1]
        
        Pokemon.pokemons['Cietrojan'].name = new_name
        bot.reply_to(message, "Новое имя твоего покемона: " + Pokemon.pokemons['Cietrojan'].name)

bot.infinity_polling(none_stop=True)

