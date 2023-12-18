import sqlite3

class StarWarsDataBase:

    def __init__(self):
        self.conn  = sqlite3.connect('star_wars.db', check_same_thread=False)
        self.cursor = self.conn.cursor()

    def create_people_table(self):
        self.cursor.execute("""
        
        CREATE TABLE IF NOT EXISTS people(
        id integer PRIMARY KEY AUTOINCREMENT, name text, height text, hair_color text)""")
        self.conn.commit()

    def insert_human_tu_table(self, data):
        self.cursor.execute("""
        INSERT INTO people (name, height, hair_color)
        VALUES (:name, :height, :hair_color)
        """, {'name': data['name'], 'height': data['height'], 'hair_color': data['hair_color']})
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

if __name__ == '__main__':
    db = StarWarsDataBase()
    db.create_people_table()
    db.close_connection()