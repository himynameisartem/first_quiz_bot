from aiogram import types
from aiogram.filters.command import Command
from aiogram import F
from data.quiz_data import quiz_data
from keyboards.builders import generate_options_keyboard


class QuizHandler:
    def __init__(self, db_handler):
        self.db_handler = db_handler

    async def get_question(self, message: types.Message, user_id: int):
        current_question_index = await self.db_handler.get_quiz_index(user_id)
        correct_index = quiz_data[current_question_index]['correct_option']
        opts = quiz_data[current_question_index]['options']

        kb = generate_options_keyboard(opts, opts[correct_index])
        await message.answer(f"{quiz_data[current_question_index]['question']}", reply_markup=kb)

    async def new_quiz(self, message: types.Message):
        user_id = message.from_user.id
        await self.db_handler.update_quiz_index(user_id, 0)
        await self.get_question(message, user_id)

    async def cmd_quiz(self, message: types.Message):
        await message.answer(f"Давайте начнем квиз!")
        await self.new_quiz(message)
