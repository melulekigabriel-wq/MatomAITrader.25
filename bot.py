from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from signals import generate_signal
from config import BOT_NAME

import os

TOKEN = os.getenv("BOT_TOKEN")

CHAT_ID = None

# START COMMAND
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    global CHAT_ID

    CHAT_ID = update.effective_chat.id

    await update.message.reply_text(
        f"🔥 Welcome to {BOT_NAME} 🔥\n\nUse /signal to get trading signals."
    )

# SIGNAL COMMAND
async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):

    data = generate_signal()

    message = format_signal(data)

    await update.message.reply_text(message)

# HELP COMMAND
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    help_text = """
AVAILABLE COMMANDS:

/start - Start bot
/signal - Get signal
/help - Show commands
/status - Bot status
"""

    await update.message.reply_text(help_text)

# STATUS COMMAND
async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "✅ MATOM AI TRADER is online and monitoring markets."
    )

# FORMAT SIGNAL
def format_signal(data):

    return f"""
🚨 MATOM AI SIGNAL 🚨

PAIR: {data['pair']}

SIGNAL: {data['signal']}

CONFIDENCE: {data['confidence']}%

ENTRY: {data['entry']}

STOP LOSS: {data['stop_loss']}

TAKE PROFIT: {data['take_profit']}

MARKET STRUCTURE:
{data['bos']}

CHoCH:
{data['choch']}

TREND:
{data['trend']}

MULTI-TIMEFRAME:
15m → {data['timeframes']['15m']}
1H → {data['timeframes']['1H']}
4H → {data['timeframes']['4H']}
Daily → {data['timeframes']['Daily']}

SESSION:
{data['session']}

VOLATILITY:
{data['volatility']}

CANDLESTICK:
{data['candlestick']}
"""

# AUTO SIGNAL TASK
async def auto_signal(app):

    global CHAT_ID

    if CHAT_ID is None:
        return

    data = generate_signal()

    # Send only strong signals
    if data['confidence'] >= 80:

        await app.bot.send_message(
            chat_id=CHAT_ID,
            text=format_signal(data)
        )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("signal", signal))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("status", status))

scheduler = AsyncIOScheduler()

scheduler.add_job(
    auto_signal,
    "interval",
    minutes=5,
    args=[app]
)

scheduler.start()

print("MATOM AI TRADER RUNNING...")

app.run_polling()
