import telebot
import requests
import os

# Render par variables set karenge, isliye yahan direct token mat likhna
BOT_TOKEN = os.environ.get('BOT_TOKEN')
API_KEY = os.environ.get('CRICKET_API_KEY')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Cricket Bot chalu hai! Score ke liye /score likho.")

@bot.message_handler(commands=['score'])
def get_score(message):
    url = f"https://api.cricapi.com/v1/cricScore?apikey={API_KEY}"
    try:
        data = requests.get(url).json()
        matches = data.get('data', [])
        msg = "🏏 *Live Scores:*\n\n"
        for m in matches[:5]:
            msg += f"📌 {m['t1']} vs {m['t2']}\nScore: {m['ms']}\n\n"
        bot.send_message(message.chat.id, msg, parse_mode="Markdown")
    except:
        bot.reply_to(message, "API error! Baad mein koshish karein.")

bot.infinity_polling()
