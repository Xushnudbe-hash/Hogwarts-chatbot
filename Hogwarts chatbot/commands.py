from telegram.ext import CommandHandler, MessageHandler, filters
import threading
import chatbot as cb

async def IOhandler(update, context):
    if cb.isRunning:
        cb.prompt = update.message.text
        print("\nBot running, got prompt: " + cb.prompt)
        await update.message.reply_text('Thinking...')
        cb.promptEvent.set()
        cb.responseEvent.wait()
        cb.responseEvent.clear()
        print("Done, responding with: " + cb.response)
        await update.message.reply_text(cb.response)

IOFunc = MessageHandler(filters.TEXT & (~filters.COMMAND), IOhandler)

async def help_command(update, context):
    await update.message.reply_text(
        "🤖 Hogwarts Bot Help Menu\n\n"
        "/help – Show this help message\n"
        "/hello – Start conversation\n"
        "/stop – Stop conversation\n"
        "/persistence [on|off] – Toggle memory between messages"
    )

helpFunc = CommandHandler('help', help_command)

async def hello(update, context):
    if not cb.isRunning:
        cb.isRunning = True
        thread = threading.Thread(target=cb.startConversation)
        thread.start()
        await update.message.reply_text("Hello! Send a prompt to start chatting.")
    else:
        await update.message.reply_text("Conversation already running.")

startFunc = CommandHandler('hello', hello)

async def stop(update, context):
    if not cb.isRunning:
        await update.message.reply_text("Nothing to stop.")
    else:
        cb.isRunning = False
        await update.message.reply_text("Conversation stopped.")

stopFunc = CommandHandler('stop', stop)

async def persistence(update, context):
    if cb.isRunning:
        await update.message.reply_text("Stop the conversation before toggling persistence.")
        return

    if context.args and len(context.args) == 1:
        param = context.args[0].lower()
        if param == "on":
            cb.persistance = True
            await update.message.reply_text("Persistence is ON.")
        elif param == "off":
            cb.persistance = False
            await update.message.reply_text("Persistence is OFF.")
        else:
            await update.message.reply_text("Unknown parameter. Use 'on' or 'off'.")
    else:
        await update.message.reply_text("Usage: /persistence [on|off]")

persistFunc = CommandHandler('persistence', persistence)