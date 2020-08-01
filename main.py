from src.db.database import Database
from src.status import Status


def configure() -> None:
    with Database() as db:
        uid = input('What\'s your user id?')
        token = input('What\'s your token?')

        db.cursor.execute(f'INSERT INTO credentials (uid, token) VALUES ("{uid}", "{token}")')


def configured() -> bool:
    with Database() as db:
        config = db.connection.execute("SELECT id FROM credentials").fetchone()

        return config is not None;


if __name__ == '__main__':
    if not configured():
        configure()

    db = Database()
    id, uid, token, created_at = db\
        .cursor\
        .execute('SELECT * FROM credentials ORDER BY created_at DESC LIMIT 1')\
        .fetchone()
    text = input('Text: ')
    emoji = input('Emoji: ')
    status = Status(uid, token)
    status\
        .with_text(text)\
        .with_emoji(emoji)\
        .change()
