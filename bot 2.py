
import asyncio
import os
from telegram import Bot
from telegram.constants import ParseMode

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=BOT_TOKEN)

async def send_startup_message():
    await bot.send_message(
        chat_id=CHAT_ID,
        text="✅ Chris, your Solaxy bot is now LIVE and fully updated for Python 3.13.",
        parse_mode=ParseMode.HTML
    )

if __name__ == "__main__":
    asyncio.run(send_startup_message())
