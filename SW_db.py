import sqlite3


class StarWarsDataBase:
    def __init__(self):
        self.conn = sqlite3.connect("star_wars_starship.db", check_same_thread=False)
        self.cursor = self.conn.cursor()

    def create_starship_table(self):
        self.cursor.execute(
            """

        CREATE TABLE IF NOT EXISTS starship(
        id integer PRIMARY KEY AUTOINCREMENT, name text, model text, manufacturer text)"""
        )
        self.conn.commit()

    def insert_starship_tu_table(self, data):
        self.cursor.execute(
            """
        INSERT INTO starship (name, model, manufacturer)
        VALUES (:name, :model, :manufacturer)
        """,
            {
                "name": data["name"],
                "model": data["model"],
                "manufacturer": data["manufacturer"],
            },
        )
        self.conn.commit()

    def close_connection(self):
        self.conn.close()


if __name__ == "__main__":
    db = StarWarsDataBase()
    db.create_starship_table()
    db.close_connection()
