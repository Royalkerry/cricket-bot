import telebot
import requests
import os

# Render par variables set karenge, isliye yahan direct token mat likhna
BOT_TOKEN = os.environ.get('8290843314:AAH9OjlfB-D6zBiCUs1nwuEopqKW_cCHAZ0')
API_KEY = os.environ.get('ced95e87-9652-4913-b5e6-9b3bd2c7561c')

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
