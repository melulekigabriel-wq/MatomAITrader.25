import sys
import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ----------------------------
# BASIC STARTUP LOGS
# ----------------------------
print("=" * 60, flush=True)
print("MATOM AI TRADER - BOT STARTUP", flush=True)
print("=" * 60, flush=True)

# ----------------------------
# LOGGING SETUP (SAFE FOR RENDER)
# ----------------------------
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

logger = logging.getLogger(__name__)

print("✅ Logging configured", flush=True)

# ----------------------------
# LOAD TOKEN
# ----------------------------
TOKEN = os.getenv("BOT_TOKEN")

print(f"BOT_TOKEN: {'SET' if TOKEN else 'NOT SET'}", flush=True)

if not TOKEN:
    print("❌ BOT_TOKEN is missing! Set it in Render environment variables.", flush=True)
    sys.exit(1)

# ----------------------------
# SIMPLE TEST COMMAND
# ----------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot is alive and working!")

# ----------------------------
# MAIN APP
# ----------------------------
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("🚀 Bot is running...", flush=True)

    app.run_polling()

if __name__ == "__main__":
    main()