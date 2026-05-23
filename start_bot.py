import os
import sys
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

print("=" * 60, flush=True)
print("MATOM AI TRADER - BOT STARTUP", flush=True)
print("=" * 60, flush=True)

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")

print(f"BOT_TOKEN: {'SET' if TOKEN else 'NOT SET'}", flush=True)

if not TOKEN:
    print("❌ Missing BOT_TOKEN", flush=True)
    sys.exit(1)

# --------------------
# COMMAND
# --------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot is alive!")

# --------------------
# MAIN
# --------------------
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("🚀 Bot is running and polling Telegram...", flush=True)

    app.run_polling(drop_pending_updates=True)

# IMPORTANT - THIS MUST EXIST
if __name__ == "__main__":
    main()