import sqlite3


class Database:
    connection: sqlite3.Connection
    cursor: sqlite3.Cursor

    def __init__(self):
        self.connection = sqlite3.connect('src/db/ns.db')
        self.cursor = self.connection.cursor()
        self._create_config_table()

    def __del__(self):
        self.connection.close()

    def __enter__(self) -> 'Database':
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        try:
            self.connection.commit()
        finally:
            return True;

    def _create_config_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS credentials (
                id integer primary key autoincrement,
                uid text not null,
                token text not null,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.connection.commit()