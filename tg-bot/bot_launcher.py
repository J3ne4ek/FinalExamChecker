import telebot
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from grader.openai_api import send_to_openai

TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

IMAGES_DIR = 'images'
os.makedirs(IMAGES_DIR, exist_ok=True)

@bot.message_handler(content_types=['photo'])
def handle_photos(message):
    photo = message.photo[-1]
    file_info = bot.get_file(photo.file_id)
    file_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_info.file_path}"

    try:
        openai_response = send_to_openai(file_url)
        bot.reply_to(message, openai_response)
    except Exception as e:
        bot.reply_to(message, f"Failed to process the image with OpenAI API: {e}")

    # os.remove(image_path)

if __name__ == '__main__':
    bot.polling()
