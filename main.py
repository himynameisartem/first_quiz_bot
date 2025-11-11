import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F

from config import API_TOKEN, DATABASE_NAME
from database.db_handler import DatabaseHandler
from handlers.start import cmd_start
from handlers.quiz import QuizHandler
from handlers.callbacks import CallbackHandler

logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()

    # Инициализация базы данных
    db_handler = DatabaseHandler(DATABASE_NAME)
    await db_handler.create_table()

    # Инициализация хендлеров
    quiz_handler = QuizHandler(db_handler)
    callback_handler = CallbackHandler(db_handler)

    # Регистрация хендлеров
    dp.message.register(cmd_start, Command("start"))
    dp.message.register(quiz_handler.cmd_quiz, Command("quiz"))
    dp.message.register(quiz_handler.cmd_quiz, F.text == "Начать игру")

    dp.callback_query.register(
        callback_handler.right_answer, F.data == "right_answer")
    dp.callback_query.register(
        callback_handler.wrong_answer, F.data == "wrong_answer")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
