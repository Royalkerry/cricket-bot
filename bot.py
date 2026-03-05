import telebot
import requests
import os
from flask import Flask
from threading import Thread

# Flask setup (UptimeRobot ke liye)
app = Flask('')
@app.route('/')
def home():
    return "Bot is Alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

# Bot setup
BOT_TOKEN = os.environ.get('BOT_TOKEN')
API_KEY = os.environ.get('CRICKET_API_KEY')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['score'])
def get_score(message):
    url = f"https://api.cricapi.com/v1/cricScore?apikey={API_KEY}"
    data = requests.get(url).json()
    matches = data.get('data', [])
    msg = "🏏 *Live Scores:*\n\n"
    for m in matches[:5]:
        msg += f"📌 {m['t1']} vs {m['t2']}\nScore: {m['ms']}\n\n"
    bot.send_message(message.chat.id, msg, parse_mode="Markdown")

# Dono ko saath chalane ke liye thread use karenge
def start_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    t = Thread(target=run)
    t.start()
    start_bot()
