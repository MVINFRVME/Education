from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telebot import TeleBot


def gen_markup():
    # Создаём объекты кнопок.
    button_1 = KeyboardButton(text="Собаки 🦮")
    button_2 = KeyboardButton(text="Кошки 🐈")

    # Создаём объект клавиатуры, добавляя в него кнопки.
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button_1, button_2)
    return keyboard


bot = TeleBot(
    '7517729527:AAFqoz3stzXwVQUJ7K9TD2q0akeGPr0Y_Co'
)  # Токен, полученный от BotFather.


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(
        message.from_user.id,
        "Какое животное тебе нравится больше?",
        reply_markup=gen_markup(),  # Отправляем клавиатуру.
    )


@bot.message_handler(func=lambda message: message.text == "Собаки 🦮")
def dog_answer(message):
    bot.send_message(
        message.from_user.id,
         "Я тоже люблю собак, они так мило машут хвостиком!",
        reply_markup=ReplyKeyboardRemove(),  # Удаляем клавиатуру.
    )


@bot.message_handler(func=lambda message: message.text == "Кошки 🐈")
def cat_answer(message):
    bot.send_message(
        message.from_user.id,
        "Я тоже люблю кошек, они так умилительно мурлыкают!",
        reply_markup=ReplyKeyboardRemove(),  # Удаляем клавиатуру.
    )


if __name__ == "__main__":
    bot.infinity_polling()