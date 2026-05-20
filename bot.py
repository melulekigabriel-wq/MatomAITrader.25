from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

from signals import generate_signal
from config import BOT_NAME
import os

TOKEN = os.getenv("BOT_TOKEN")

# START COMMAND
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        f"🔥 Welcome to {BOT_NAME} 🔥\n\nUse /signal to get trading signals."
    )

# SIGNAL COMMAND
async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):

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

MULTI-TIMEFRAME ANALYSIS:
15m → {data['timeframes']['15m']}
1H → {data['timeframes']['1H']}
4H → {data['timeframes']['4H']}
Daily → {data['timeframes']['Daily']}

OVERALL TREND:
{data['overall_trend']}

SMART MONEY CONCEPTS:
✅ {data['order_block']}
✅ {data['liquidity']}
✅ {data['fvg']}

CANDLESTICK ANALYSIS:
✅ {data['candlestick']}
"""

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
        "✅ MATOM AI TRADER is online and running."
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("signal", signal))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("status", status))

print("MATOM AI TRADER RUNNING...")

app.run_polling()
