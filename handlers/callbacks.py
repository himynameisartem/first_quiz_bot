from aiogram import types
from aiogram import F
from data.quiz_data import quiz_data
from keyboards.builders import generate_options_keyboard


class CallbackHandler:
    def __init__(self, db_handler):
        self.db_handler = db_handler
        self.scores = {}

    async def right_answer(self, callback: types.CallbackQuery):
        await self._clear_keyboard(callback)
        user_id = callback.from_user.id
        selected_answer = callback.data.split(":")[1]
        current_question_index = await self.db_handler.get_quiz_index(user_id)

        if current_question_index == 0:
            self.scores[user_id] = 0

        await callback.message.answer(f"✅ Ваш ответ: {selected_answer}")
        self.scores[user_id] = self.scores.get(user_id, 0) + 1
        current_question_index += 1

        await self.db_handler.update_quiz_index(user_id, current_question_index)
        if current_question_index < len(quiz_data):
            await self._get_next_question(callback.message, user_id)
        else:
            score = self.scores.get(user_id, 0)
            await self.db_handler.save_result(user_id, score)
            await callback.message.answer(f"🎉 Квиз завершён!\nВаш результат: {score}/{len(quiz_data)}")
            self.scores.pop(user_id, None)

    async def wrong_answer(self, callback: types.CallbackQuery):
        await self._clear_keyboard(callback)
        user_id = callback.from_user.id
        selected_answer = callback.data.split(":")[1]
        current_question_index = await self.db_handler.get_quiz_index(user_id)

        if current_question_index == 0:
            self.scores[user_id] = 0

        correct_option = quiz_data[current_question_index]['correct_option']
        correct_answer = quiz_data[current_question_index]['options'][correct_option]

        await callback.message.answer(f"❌ Ваш ответ: {selected_answer}\n"
                                      f"Правильный ответ: {correct_answer}")
        current_question_index += 1

        await self.db_handler.update_quiz_index(user_id, current_question_index)
        if current_question_index < len(quiz_data):
            await self._get_next_question(callback.message, user_id)
        else:
            score = self.scores.get(user_id, 0)
            await self.db_handler.save_result(user_id, score)
            await callback.message.answer(f"🎉 Квиз завершён!\nВаш результат: {score}/{len(quiz_data)}")
            self.scores.pop(user_id, None)

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
