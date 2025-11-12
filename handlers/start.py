from aiogram import types
from aiogram.filters.command import Command
from keyboards.builders import get_start_keyboard
from database.db_handler import DatabaseHandler

db_handler = DatabaseHandler("quiz_bot.db")


async def cmd_start(message: types.Message):
    await db_handler.create_table()

    stats = await db_handler.get_stats(message.from_user.id)
    text = (
        f"👋 Привет, {message.from_user.first_name}!\n"
        f"Добро пожаловать в квиз!\n\n"
        f"📊 Ваша статистика:\n"
        f"— Последний результат: {stats['last_score']}\n"
        f"— Всего игр: {stats['total_games']}\n"
        f"— Лучший результат: {stats['best_score']}\n\n"
        f"Нажмите кнопку ниже, чтобы начать ⬇️"
    )

    await message.answer(text, reply_markup=get_start_keyboard())
