import asyncio
import logging
from functools import partial
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F

from config import API_TOKEN, DATABASE_NAME
from database.db_handler import DatabaseHandler
from handlers.start import cmd_start
from handlers.quiz import QuizHandler
from handlers.callbacks import CallbackHandler
from handlers.stats import cmd_stats
from keyboards.builders import get_start_keyboard

logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()

    db_handler = DatabaseHandler(DATABASE_NAME)
    await db_handler.create_table()

    quiz_handler = QuizHandler(db_handler)
    callback_handler = CallbackHandler(db_handler)

    async def handle_retry(message: types.Message):
        user_id = message.from_user.id
        await callback_handler.reset_user_progress(user_id)
        await message.answer("Готовы начать заново?", reply_markup=get_start_keyboard(start_label="Начать заново"))
        await quiz_handler.cmd_quiz(message)

    dp.message.register(
        partial(cmd_start, db_handler=db_handler),
        Command("start")
    )
    dp.message.register(quiz_handler.cmd_quiz, Command("quiz"))
    dp.message.register(quiz_handler.cmd_quiz, F.text == "Начать игру")
    dp.message.register(handle_retry, F.text == "Попробовать ещё раз")
    dp.message.register(
        partial(cmd_stats, db_handler=db_handler), Command("stats"))
    dp.message.register(partial(cmd_stats, db_handler=db_handler),
                        F.text == "Посмотреть статистику")
    dp.message.register(handle_retry, F.text == "Начать заново")

    dp.callback_query.register(
        callback_handler.right_answer, F.data.startswith("right_answer"))
    dp.callback_query.register(
        callback_handler.wrong_answer, F.data.startswith("wrong_answer"))

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
