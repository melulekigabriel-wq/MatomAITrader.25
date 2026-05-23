from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

import os
import logging
import asyncio

# Setup logging to see all output
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    logger.error("❌ BOT_TOKEN environment variable not set!")
    print("❌ BOT_TOKEN environment variable not set!")
    exit(1)

logger.info(f"✅ BOT_TOKEN found: {TOKEN[:10]}...")
print(f"✅ BOT_TOKEN found: {TOKEN[:10]}...")

# START COMMAND
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"✅ /start command from user {update.effective_chat.id}")
    print(f"✅ /start command from user {update.effective_chat.id}")
    await update.message.reply_text("🔥 MATOM AI TRADER IS ONLINE! 🔥")

async def main():
    """Start the bot"""
    try:
        logger.info("🚀 Starting MATOM AI TRADER bot...")
        print("🚀 Starting MATOM AI TRADER bot...")
        
        app = Application.builder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        
        logger.info("✅ Bot initialized successfully!")
        print("✅ Bot initialized successfully!")
        logger.info("🔥 MATOM AI TRADER RUNNING... 🔥")
        print("🔥 MATOM AI TRADER RUNNING... 🔥")
        
        async with app:
            await app.start()
            logger.info("✅ App started!")
            print("✅ App started!")
            
            await app.updater.start_polling(allowed_updates=Update.ALL_TYPES)
            logger.info("✅ Bot polling started - waiting for messages!")
            print("✅ Bot polling started - waiting for messages!")
            
            try:
                await asyncio.Event().wait()
            except KeyboardInterrupt:
                logger.info("🛑 Bot stopped")
                print("🛑 Bot stopped")
            finally:
                await app.updater.stop()
                await app.stop()
        
    except Exception as e:
        logger.critical(f"❌ CRITICAL ERROR: {str(e)}")
        print(f"❌ CRITICAL ERROR: {str(e)}")
        import traceback
        logger.critical(traceback.format_exc())
        print(traceback.format_exc())
        raise

if __name__ == "__main__":
    print("=" * 50)
    print("MATOM AI TRADER BOT - STARTING")
    print("=" * 50)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot shutdown complete")
    except Exception as e:
        print(f"Bot crashed: {str(e)}")
