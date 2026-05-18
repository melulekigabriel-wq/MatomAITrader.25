from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    pairs = ["EUR/USD", "GBP/USD", "USD/JPY", "XAU/USD"]
    signals = ["BUY", "SELL", "WAIT"]

    pair = random.choice(pairs)
    signal = random.choice(signals)
    confidence = random.randint(70, 95)

    message = f"""
🔥 MATOM AI TRADER 🔥

PAIR: {pair}

SIGNAL: {signal}

CONFIDENCE: {confidence}%

TREND: BULLISH

RISK: MODERATE
"""

    await update.message.reply_text(message)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
