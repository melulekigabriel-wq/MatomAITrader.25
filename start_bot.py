#!/usr/bin/env python3

import sys
import os

# Force unbuffered output to ensure logs appear in Render
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0) if hasattr(os, 'fdopen') else sys.stdout
sys.stderr = sys.stdout

print("=" * 60, flush=True)
print("MATOM AI TRADER - BOT STARTUP", flush=True)
print("=" * 60, flush=True)

import logging

# Configure logging to output to console immediately
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

print("✅ Logging configured", flush=True)

TOKEN = os.getenv("BOT_TOKEN")
print(f"BOT_TOKEN env var: {'SET' if TOKEN else 'NOT SET'}", flush=True)

if not TOKEN:
    print("❌ ERROR: BOT_TOKEN not found!", flush=True)
    logger.error("BOT_TOKEN environment variable is not set!")
    sys.exit(1)

print(f"✅ Token found: {TOKEN[:10]}...", flush=True)

try:
    print("Importing telegram...", flush=True)
    from telegram import Update
    from telegram.ext import Application, CommandHandler, ContextTypes
    print("✅ Telegram modules imported", flush=True)
    
    print("Setting up command handlers...", flush=True)
    
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        print(f"📨 /start received from {update.effective_chat.id}", flush=True)
        await update.message.reply_text("🔥 MATOM AI TRADER IS ONLINE! 🔥")
    
    async def main():
        print("🚀 Building Application...", flush=True)
        app = Application.builder().token(TOKEN).build()
        print("✅ Application built", flush=True)
        
        print("📝 Adding command handlers...", flush=True)
        app.add_handler(CommandHandler("start", start))
        print("✅ Handlers added", flush=True)
        
        print("🔥 MATOM AI TRADER RUNNING 🔥", flush=True)
        logger.info("Bot is starting polling...")
        
        async with app:
            await app.start()
            print("✅ App started, beginning polling...", flush=True)
            await app.updater.start_polling(allowed_updates=Update.ALL_TYPES)
            print("✅ Polling started! Waiting for messages...", flush=True)
            
            try:
                import asyncio
                await asyncio.Event().wait()
            except KeyboardInterrupt:
                print("🛑 Received keyboard interrupt", flush=True)
            finally:
                await app.updater.stop()
                await app.stop()
    
    print("⏳ Starting async main...", flush=True)
    import asyncio
    asyncio.run(main())
    
except Exception as e:
    print(f"❌ CRITICAL ERROR: {str(e)}", flush=True)
    import traceback
    print(traceback.format_exc(), flush=True)
    logger.critical(f"Critical error: {str(e)}")
    logger.critical(traceback.format_exc())
    sys.exit(1)
