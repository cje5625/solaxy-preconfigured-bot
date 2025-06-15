
import os
import time
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=BOT_TOKEN)

def send_startup_message():
    bot.send_message(chat_id=CHAT_ID, text="✅ Chris, your Solaxy Bot is now LIVE. All systems are tracking.")

if __name__ == "__main__":
    send_startup_message()
    while True:
        time.sleep(60)
