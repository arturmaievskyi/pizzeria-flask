import sqlite3


class ShopDB_Pizzas:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.db_name = "pizzas.db"

    def open_pizzas(self): #функція що відкриває базу даних
        self.conn =sqlite3.connect(self.db_name) # з'єднання з базою даних (БД)
        self.cursor = self.conn.cursor() #курсор (посилання) на БД

    def close_pizzas(self): #функція що закриває базу даних
        self.cursor.close()
        self.conn.close()
    def get_all_pizzas(self):
        self.open_pizzas()
        self.cursor.execute("SELECT * FROM pizza")
        data_all_pizzas = self.cursor.fetchall()
        self.close_pizzas()
        return data_all_pizzas

    def get_pizza(self, id):
        self.open_pizzas()
        self.cursor.execute("SELECT * FROM pizza WHERE id==(?)", [id])
        data_one_pizza = self.cursor.fetchone()
        self.close_pizzas()
        return data_one_pizza
    
    def add_order_pizza(self, *data):
        self.open_pizzas()
        self.cursor.execute('''INSERT INTO orders (item_id, name, phone, email, city, address, cost) VALUES((?), (?), (?), (?), (?), (?), (?))''', [*data])
        self.conn.commit()
        self.close_pizzas()

    def get_categories(self):
        self.open_pizzas()
        self.cursor.execute("SELECT * FROM categories")
        data = self.cursor.fetchall()
        self.close()
        return data
    

    def get_category_pizza(self, id):
        self.open_pizzas()
        self.cursor.execute("SELECT * FROM items WHERE category_id==(?)", [id])
        data = self.cursor.fetchall()
        self.close_pizzas()
        return data
    
    
class ShopDB_Drinks:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.db_name = "drinks.db"

    def open_drinks(self): #функція що відкриває базу даних
        self.conn =sqlite3.connect(self.db_name) # з'єднання з базою даних (БД)
        self.cursor = self.conn.cursor() #курсор (посилання) на БД


    def close_drinks(self): #функція що закриває базу даних
        self.cursor.close()
        self.conn.close()
    def get_all_drinks(self):
        self.open_drinks()
        self.cursor.execute("SELECT * FROM drink")
        data_all_drinks = self.cursor.fetchall()
        self.close_drinks()
        return data_all_drinks

    def get_drink(self, id):
        self.open_drinks()
        self.cursor.execute("SELECT * FROM drink WHERE id==(?)", [id])
        data_one_drink = self.cursor.fetchone()
        self.close_drinks()
        return data_one_drink
    def add_order_drink(self, *data):
        self.open_drinks()
        self.cursor.execute('''INSET INTO order (drink_id, phone, name, email, city, cost) VALUES((?), (?), (?), (?), (?), (?))''', [*data])
        self.conn.commit()
        self.close()

    def get_categories_drink(self):
        self.open_drinks()
        self.cursor.execute("SELECT * FROM categories")
        data = self.cursor.fetchall()
        self.close()
        return data
    

    def get_category_drinks(self, id):
        self.open_drinks()
        self.cursor.execute("SELECT * FROM drink WHERE category_id==(?)", [id])
        data = self.cursor.fetchall()
        self.close()
        return data
    
