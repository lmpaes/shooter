import sqlite3


class DBProxy:

    def __inti__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
