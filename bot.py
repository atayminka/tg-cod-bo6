from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

async def start(update: Update, context):
    await update.message.reply_text("Hello! Send me your data.")

async def echo(update: Update, context):
    user_input = update.message.text
    # Process and save data here
    await update.message.reply_text(f"You sent: {user_input}")

app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, echo))

app.run_polling()
