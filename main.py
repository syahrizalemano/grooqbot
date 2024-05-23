import os
import telebot
from groq import Groq

# Inisialisasi klien Groq
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

# Inisialisasi bot dengan token
bot = telebot.TeleBot(os.getenv('TELEGRAM_BOT_TOKEN'))

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi! I am your Groq-powered bot. Ask me anything.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_message = message.text
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "you are a helpful assistant."
            },
            {
                "role": "user",
                "content": user_message,
            }
        ],
        model="llama3-8b-8192",
    )
    response = chat_completion.choices[0].message.content
    bot.reply_to(message, response)

if __name__ == '__main__':
    bot.polling()
  
