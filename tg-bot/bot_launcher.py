import os
import telebot

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(content_types=['photo'])
def handle_photos(message):
    if message.photo:
        print(message.photo)
    else:
        bot.reply_to(message, "No images found in the message.")


if __name__ == '__main__':
    bot.infinity_polling()