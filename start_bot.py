import os
import sys
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

print("🔥 BOT STARTING...", flush=True)

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    print("❌ BOT_TOKEN missing", flush=True)
    sys.exit(1)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("START RECEIVED", flush=True)
    await update.message.reply_text("🤖 Bot is alive and working!")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("🚀 Running polling...", flush=True)

    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()