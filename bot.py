from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

from database import Trade, SessionLocal
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from trade_manager import get_statistics
from engine import run_engine
from config import BOT_NAME

import os
import logging
import asyncio

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    logger.error("❌ BOT_TOKEN environment variable not set!")
    raise ValueError("BOT_TOKEN is required!")

logger.info(f"✅ BOT_TOKEN found: {TOKEN[:10]}...")

CHAT_ID = None

# START COMMAND
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    global CHAT_ID
    
    try:
        CHAT_ID = update.effective_chat.id
        
        await update.message.reply_text(
            f"🔥 Welcome to {BOT_NAME} 🔥\n\nUse /signal to get trading signals."
        )
        logger.info(f"✅ /start command from user {CHAT_ID}")
    except Exception as e:
        logger.error(f"❌ Error in start command: {str(e)}")
        await update.message.reply_text(f"Error: {str(e)}")

# SIGNAL COMMAND
async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    try:
        logger.info("📊 /signal command received")
        data = run_engine()
        message = format_signal(data)
        await update.message.reply_text(message)
    except Exception as e:
        logger.error(f"❌ Error in signal command: {str(e)}")
        await update.message.reply_text(f"❌ Error generating signal: {str(e)}")


# HELP COMMAND
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    help_text = """
AVAILABLE COMMANDS:

/start - Start bot
/signal - Get signal
/help - Show commands
/history - View recent signals
/status - Bot status
/stats - View performance statistics
"""
    
    await update.message.reply_text(help_text)


# HISTORY COMMAND
async def history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    try:
        db = SessionLocal()
        
        trades = db.query(Trade).order_by(Trade.id.desc()).limit(5).all()
        
        if not trades:
            
            await update.message.reply_text("No trade history yet.")
            
            return
        
        message = "📊 LAST 5 SIGNALS 📊\n\n"
        
        for trade in trades:
            
            message += f"""
PAIR: {trade.pair}
SIGNAL: {trade.signal}
CONFIDENCE: {trade.confidence}%
TREND: {trade.trend}
SESSION: {trade.session_name}

"""
        
        db.close()
        
        await update.message.reply_text(message)
    except Exception as e:
        logger.error(f"❌ Error in history command: {str(e)}")
        await update.message.reply_text(f"❌ Error retrieving history: {str(e)}")

# STATUS COMMAND
async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    try:
        await update.message.reply_text(
            "✅ MATOM AI TRADER is online and monitoring markets."
        )
    except Exception as e:
        logger.error(f"❌ Error in status command: {str(e)}")
    
# STATS COMMAND
async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    try:
        data = get_statistics()
        
        message = f"""
📊 MATOM AI STATISTICS

Total Trades: {data['total']}

Wins: {data['wins']}

Losses: {data['losses']}

Open Trades: {data['open']}

Win Rate: {data['win_rate']}%
"""
        
        await update.message.reply_text(message)
    except Exception as e:
        logger.error(f"❌ Error in stats command: {str(e)}")
        await update.message.reply_text(f"❌ Error retrieving stats: {str(e)}")
    
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
async def auto_signal(app: Application):
    
    global CHAT_ID
    
    if CHAT_ID is None:
        return
    
    try:
        data = run_engine()
        
        # Send only strong signals
        if data['confidence'] >= 80:
            
            await app.bot.send_message(
                chat_id=CHAT_ID,
                text=format_signal(data)
            )
            logger.info(f"📨 Auto signal sent - Confidence: {data['confidence']}%")
    except Exception as e:
        logger.error(f"❌ Error in auto_signal: {str(e)}")

async def main():
    """Start the bot with async polling"""
    try:
        logger.info("🚀 Initializing Telegram bot...")
        app = Application.builder().token(TOKEN).build()
        
        # Add handlers
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("signal", signal))
        app.add_handler(CommandHandler("help", help_command))
        app.add_handler(CommandHandler("status", status))
        app.add_handler(CommandHandler("history", history))
        app.add_handler(CommandHandler("stats", stats))
        
        logger.info("✅ Command handlers registered")
        
        # Setup scheduler for auto signals
        scheduler = AsyncIOScheduler()
        scheduler.add_job(
            auto_signal,
            "interval",
            minutes=5,
            args=[app]
        )
        scheduler.start()
        logger.info("✅ APScheduler started (auto-signals every 5 minutes)")
        
        logger.info("🔥 MATOM AI TRADER RUNNING... 🔥")
        logger.info(f"Bot Name: {BOT_NAME}")
        logger.info("Waiting for commands...")
        
        # Start the bot with async polling
        async with app:
            await app.start()
            await app.updater.start_polling(allowed_updates=Update.ALL_TYPES)
            logger.info("✅ Bot polling started!")
            
            # Keep the bot running
            try:
                await asyncio.Event().wait()
            except KeyboardInterrupt:
                logger.info("🛑 Bot stopped by user")
            finally:
                await app.updater.stop()
                await app.stop()
        
    except Exception as e:
        logger.critical(f"❌ CRITICAL ERROR: {str(e)}")
        import traceback
        logger.critical(traceback.format_exc())
        raise

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot shutdown complete")
