import telebot
from telebot.types import LabeledPrice

TOKEN = "8980820500:AAH3jbKarggc6wBYE7VDCCdH2wDuC5KsM2U"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "⭐ ចុច /deposit ដើម្បីផ្ទុក Telegram Stars"
    )

@bot.message_handler(commands=['deposit'])
def deposit(message):
    prices = [LabeledPrice(label="100 Stars", amount=100)]

    bot.send_invoice(
        chat_id=message.chat.id,
        title="Telegram Stars Deposit",
        description="Deposit 100 Telegram Stars",
        invoice_payload="stars_deposit",
        provider_token="",
        currency="XTR",
        prices=prices
    )

@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(pre_checkout_query):
    bot.answer_pre_checkout_query(
        pre_checkout_query.id,
        ok=True
    )

@bot.message_handler(content_types=['successful_payment'])
def success(message):
    bot.send_message(
        message.chat.id,
        f"✅ បានទទួល {message.successful_payment.total_amount} Stars"
    )

bot.infinity_polling()
