from database.database import get_db_connection

async def create_table():
    conn = await get_db_connection()
    async with conn.cursor() as cursor:
        await cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER UNIQUE,
                username TEXT,
                first_name TEXT,
                last_name TEXT,
                time_added TEXT
            )
        """)
        await conn.commit()
    await conn.close()