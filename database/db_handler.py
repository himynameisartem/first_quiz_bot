import aiosqlite


class DatabaseHandler:
    def __init__(self, db_path: str):
        self.db_path = db_path

    async def create_table(self):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute('''CREATE TABLE IF NOT EXISTS quiz_state 
                             (user_id INTEGER PRIMARY KEY, 
                             question_index INTEGER,
                             last_score INTEGER DEFAULT 0,
                             total_games INTEGER DEFAULT 0,
                             best_score INTEGER DEFAULT 0)
                             ''')
            await db.commit()

    async def update_quiz_index(self, user_id: int, index: int):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                'INSERT INTO quiz_state (user_id, question_index) VALUES (?, ?) '
                'ON CONFLICT(user_id) DO UPDATE SET question_index = excluded.question_index',
                (user_id, index)
            )
            await db.commit()

    async def get_quiz_index(self, user_id: int) -> int:
        async with aiosqlite.connect(self.db_path) as db:
            async with db.execute('SELECT question_index FROM quiz_state WHERE user_id = (?)', (user_id,)) as cursor:
                results = await cursor.fetchone()
                return results[0] if results is not None else 0

    async def save_result(self, user_id: int, score: int):
        async with aiosqlite.connect(self.db_path) as db:
            async with db.execute('SELECT best_score, total_games FROM quiz_state WHERE user_id = ?', (user_id,)) as cursor:
                results = await cursor.fetchone()
                if results:
                    best_score, total_games = results
                    best_score = max(best_score, score)
                    total_games += 1
                    await db.execute('''UPDATE quiz_state 
                            SET last_score = ?, best_score = ?, total_games = ? WHERE user_id = ?''',
                                     (score, best_score, total_games, user_id))
                else:
                    await db.execute('''INSERT INTO quiz_state 
                            (user_id, question_index, last_score, total_games, best_score)
                            VALUES (?, 0, ?, 1, ?)''',
                                     (user_id, score, score))
                await db.execute('UPDATE quiz_state SET question_index = 0 WHERE user_id = ?', (user_id,))
                await db.commit()

    async def get_stats(self, user_id: int):
        async with aiosqlite.connect(self.db_path) as db:
            async with db.execute('SELECT last_score, total_games, best_score FROM quiz_state WHERE user_id = ?',
                                  (user_id,)) as cursor:
                results = await cursor.fetchone()
                if results:
                    return {
                        "last_score": results[0],
                        "total_games": results[1],
                        "best_score": results[2]
                    }
                else:
                    return {"last_score": 0,
                            "total_games": 0,
                            "best_score": 0}
