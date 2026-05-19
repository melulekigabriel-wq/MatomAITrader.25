from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from signals import generate_signal
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    data = generate_signal()

    message = f"""
🔥 MATOM AI TRADER 🔥

SIGNAL: {data['signal']}

CONFIDENCE: {data['confidence']}%

MARKET STRUCTURE:
{data['bos']}

TREND:
{data['trend']}

SMART MONEY CONCEPTS:
✅ {data['order_block']}
✅ {data['liquidity']}
✅ {data['fvg']}
"""

    await update.message.reply_text(message)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot is running...")

app.run_polling()
