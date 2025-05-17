import commands as c
import apikey as key
from telegram.ext import ApplicationBuilder

async def main():
    app = ApplicationBuilder().token(key.API_KEY).build()

    app.add_handler(c.helpFunc)
    app.add_handler(c.startFunc)
    app.add_handler(c.stopFunc)
    app.add_handler(c.persistFunc)
    app.add_handler(c.IOFunc)

    print("Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())