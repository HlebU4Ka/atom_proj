import telebot


def send_telegram_notification(chat_id, message):
    bot_token = 'TELEGRAM_BOT_API_KEY'
    bot = telebot.TeleBot(bot_token)
    bot.send_message(chat_id, message)
