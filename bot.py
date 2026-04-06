import telebot
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

RATE = 85
MIN_AMOUNT = 1000
BTC_ADDRESS = "bc1q7rjkstpk3j7rw5un0csnsa8z6dl6fthsm8tfpp"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome 👋\n\n💰 Minimum Buy: ₹1000\n💲 Rate: ₹85 per USDT\n\nEnter amount in INR:"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    try:
        amount = float(text)

        if amount < MIN_AMOUNT:
            await update.message.reply_text("❌ Minimum ₹1000 required")
            return

        usdt = amount / RATE

        await update.message.reply_text(
            f"💰 You will receive: {usdt:.2f} USDT\n\n"
            f"📥 Send BTC to:\n{BTC_ADDRESS}\n\n"
            f"⚠️ Send within 10 minutes\n\n"
            f"After payment send:\nTXID + Your USDT Address"
        )

    except:
        await update.message.reply_text("❌ Enter valid amount")

app = ApplicationBuilder().token("8733073066:AAEw1ZsCMzuKVljczSkzDZ1-HU8aT29bybI").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle_message))

app.run_polling()