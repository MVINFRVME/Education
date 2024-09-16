import telebot

bot = telebot.TeleBot("7517729527:AAFqoz3stzXwVQUJ7K9TD2q0akeGPr0Y_Co") # Токен, полученный от BotFather.


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "Капитан Прайс приветствует тебя! Напиши, что-то в чат!")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

    bot.send_message(message.chat.id, 'Я Пиклонтик!')


if __name__ == "__main__":
    bot.infinity_polling()
