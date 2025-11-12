from aiogram import types
from database.db_handler import DatabaseHandler
from keyboards.builders import get_start_keyboard

db_handler = DatabaseHandler('quiz_bot.db')


async def cmd_stats(message: types.Message, db_handler):
    stats = await db_handler.get_stats(message.from_user.id)
    text = (
        f"📊 Ваша статистика:\n"
        f"— Последний результат: {stats['last_score']}\n"
        f"— Всего игр: {stats['total_games']}\n"
        f"— Лучший результат: {stats['best_score']}\n"
    )

    await message.answer(text, reply_markup=get_start_keyboard())
