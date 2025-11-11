import aiosqlite


class DatabaseHandler:
    def __init__(self, db_path: str):
        self.db_path = db_path

    async def create_table(self):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute('''CREATE TABLE IF NOT EXISTS quiz_state 
                             (user_id INTEGER PRIMARY KEY, question_index INTEGER)''')
            await db.commit()

    async def update_quiz_index(self, user_id: int, index: int):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute('INSERT OR REPLACE INTO quiz_state (user_id, question_index) VALUES (?, ?)',
                             (user_id, index))
            await db.commit()

    async def get_quiz_index(self, user_id: int) -> int:
        async with aiosqlite.connect(self.db_path) as db:
            async with db.execute('SELECT question_index FROM quiz_state WHERE user_id = (?)', (user_id,)) as cursor:
                results = await cursor.fetchone()
                return results[0] if results is not None else 0
