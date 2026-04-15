import telebot
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

if not TOKEN:
    print('Token is not found!')
    exit()   

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Я ECHO-бот. Напиши мені щось, і я повторю це!")

@bot.message_handler(commands=['info'])
def send_info(message):
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    user_text = message.text

    reply_text = f"Привіт, {user_name}!\n" \
                 f"Твій Telegram ID: {user_id}\n" \
                 f"Ти щойно надіслав мені текст: '{user_text}'"
    
    bot.reply_to(message, reply_text)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    print('Bot is running...')
    bot.infinity_polling()