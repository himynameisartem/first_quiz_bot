from aiogram import types
from aiogram import F
from data.quiz_data import quiz_data
from keyboards.builders import generate_options_keyboard


class CallbackHandler:
    def __init__(self, db_handler):
        self.db_handler = db_handler

    async def right_answer(self, callback: types.CallbackQuery):
        await self._clear_keyboard(callback)
        await callback.message.answer("Верно!")
        await self._handle_next_question(callback)

    async def wrong_answer(self, callback: types.CallbackQuery):
        await self._clear_keyboard(callback)

        current_question_index = await self.db_handler.get_quiz_index(callback.from_user.id)
        correct_option = quiz_data[current_question_index]['correct_option']
        await callback.message.answer(f"Неправильно. Правильный ответ: {quiz_data[current_question_index]['options'][correct_option]}")

        await self._handle_next_question(callback)

    async def _clear_keyboard(self, callback: types.CallbackQuery):
        await callback.bot.edit_message_reply_markup(
            chat_id=callback.from_user.id,
            message_id=callback.message.message_id,
            reply_markup=None
        )

    async def _handle_next_question(self, callback: types.CallbackQuery):
        user_id = callback.from_user.id
        current_question_index = await self.db_handler.get_quiz_index(user_id)

        current_question_index += 1
        await self.db_handler.update_quiz_index(user_id, current_question_index)

        if current_question_index < len(quiz_data):
            from handlers.quiz import QuizHandler
            quiz_handler = QuizHandler(self.db_handler)
            await quiz_handler.get_question(callback.message, user_id)
        else:
            await callback.message.answer("Это был последний вопрос. Квиз завершен!")
