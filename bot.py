from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from signals import generate_signal
from config import BOT_NAME
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    data = generate_signal()

    message = f"""
🔥 {BOT_NAME} 🔥

PAIR: {data['pair']}

SIGNAL: {data['signal']}

CONFIDENCE: {data['confidence']}%

ENTRY: {data['entry']}

STOP LOSS: {data['stop_loss']}

TAKE PROFIT: {data['take_profit']}

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

print("MATOM AI TRADER IS RUNNING...")

app.run_polling()
