from aiogram import types
from aiogram import F
from data.quiz_data import quiz_data
from keyboards.builders import generate_options_keyboard


class CallbackHandler:
    def __init__(self, db_handler):
        self.db_handler = db_handler

    async def right_answer(self, callback: types.CallbackQuery):
        await self._clear_keyboard(callback)

        # Получаем текст ответа из callback_data
        selected_answer = callback.data.split(":")[1]
        current_question_index = await self.db_handler.get_quiz_index(callback.from_user.id)
        current_question = quiz_data[current_question_index]['question']

        # Выводим ответ пользователя
        await callback.message.answer(f"✅ Ваш ответ: {selected_answer}")

        current_question_index += 1
        await self.db_handler.update_quiz_index(callback.from_user.id, current_question_index)

        if current_question_index < len(quiz_data):
            await self._get_next_question(callback.message, callback.from_user.id)
        else:
            await callback.message.answer("🎉 Поздравляю! Это был последний вопрос. Квиз завершен!")

    async def wrong_answer(self, callback: types.CallbackQuery):
        await self._clear_keyboard(callback)

        # Получаем текст ответа из callback_data
        selected_answer = callback.data.split(":")[1]
        current_question_index = await self.db_handler.get_quiz_index(callback.from_user.id)
        current_question = quiz_data[current_question_index]['question']
        correct_option = quiz_data[current_question_index]['correct_option']
        correct_answer = quiz_data[current_question_index]['options'][correct_option]

        # Выводим ответ пользователя и правильный ответ
        await callback.message.answer(f"❌ Ваш ответ: {selected_answer}\n"
                                      f"Правильный ответ: {correct_answer}")

        current_question_index += 1
        await self.db_handler.update_quiz_index(callback.from_user.id, current_question_index)

        if current_question_index < len(quiz_data):
            await self._get_next_question(callback.message, callback.from_user.id)
        else:
            await callback.message.answer("🎉 Поздравляю! Это был последний вопрос. Квиз завершен!")

    async def _clear_keyboard(self, callback: types.CallbackQuery):
        await callback.bot.edit_message_reply_markup(
            chat_id=callback.from_user.id,
            message_id=callback.message.message_id,
            reply_markup=None
        )

    async def _get_next_question(self, message: types.Message, user_id: int):
        from handlers.quiz import QuizHandler
        quiz_handler = QuizHandler(self.db_handler)
        await quiz_handler.get_question(message, user_id)
