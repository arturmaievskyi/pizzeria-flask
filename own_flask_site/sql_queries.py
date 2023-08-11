import sqlite3


class ShopDB:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.db_name = "shop.db"

    def open(self): #функція що відкриває базу даних
        self.conn =sqlite3.connect(self.db_name) # з'єднання з базою даних (БД)
        self.cursor = self.conn.cursor() #курсор (посилання) на БД

    def close(self): #функція що закриває базу даних
        self.cursor.close()
        self.conn.close()
    def get_all(self):
        self.open()
        self.cursor.execute("SELECT * FROM pizza")
        data = self.cursor.fetchall()
        self.close()
        return data

    def get_item(self, id):
        self.open()
        self.cursor.execute("SELECT * FROM WHERE id==(?)", [id])
        data = self.cursor.fetchone()
        self.close()
        return data