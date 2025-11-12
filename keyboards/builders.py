from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram import types


def generate_options_keyboard(answer_options, right_answer):
    builder = InlineKeyboardBuilder()

    for option in answer_options:
        callback_data = f"right_answer:{option}" if option == right_answer else f"wrong_answer:{option}"
        builder.add(types.InlineKeyboardButton(
            text=option,
            callback_data=callback_data)
        )

    builder.adjust(1)
    return builder.as_markup()


def get_start_keyboard(start_label: str = "Начать игру"):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text=start_label))
    builder.add(types.KeyboardButton(text="Посмотреть статистику"))
    return builder.as_markup(resize_keyboard=True)
