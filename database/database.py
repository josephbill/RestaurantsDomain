import sqlite3

conn = sqlite3.connect("restaurants.db")

conn.execute('''CREATE TABLE IF NOT EXISTS restaurants(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 price INTEGER NOT NULL 
    )''')


conn.execute('''CREATE TABLE IF NOT EXISTS customers(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 first_name TEXT NOT NULL,
                 last_name INTEGER NOT NULL 
    )''')

conn.execute('''CREATE TABLE IF NOT EXISTS reviews(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 restaurant_id INTEGER NOT NULL,
                 customer_id INTEGER NOT NULL,
                 star_rating TEXT NOT NULL, 
                 FOREIGN KEY (restaurant_id) REFERENCES restaurants(id),
                 FOREIGN KEY (customer_id) REFERENCES customers(id)
    )''')

conn.commit()
    





