# bot.py
# Simple Telegram User Bot using Telethon
# Contact: @AsikpitX

from telethon import TelegramClient, events
import os

# Replace these with your own API ID and API HASH
api_id = int(os.environ.get("API_ID", "YOUR_API_ID"))
api_hash = os.environ.get("API_HASH", "YOUR_API_HASH")

# Session name
bot = TelegramClient("userbot_session", api_id, api_hash)

@bot.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    await event.reply("Hello! I am your User Bot 🤖\nContact: @AsikpitX")

@bot.on(events.NewMessage(pattern='/ping'))
async def ping_handler(event):
    await event.reply("Pong! 🏓")

print("Bot is running...")
bot.start()
bot.run_until_disconnected()
